import subprocess, os
import docker

from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWidget,
    QGridLayout,
    QPushButton
)

from setup_logger import logging

class Docker:
    def __init__(self):
        super().__init__()

    def start_ros(self):
        logging.info("Starting ROS (maybe)...")
        print("Starting ROS (maybe)...")

    def getADEVersion(self) -> str:
        path = '/usr/local/bin/ade'
        if os.path.isfile(path):
            ade_version = subprocess.run([path, '--version'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        else:
            return "ADE not found"
        logging.info("ADE version: {version}".format(version=ade_version))
        return ade_version


class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width/5

        Gridlayout = QGridLayout()

        button_start_ros = QPushButton("Start ROS")
        button_start_ros.clicked.connect(Docker.start_ros)
        button_start_ros.setFixedSize(btn_size, btn_size)

        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        ade_version = QLabel("ADE Version: {version}".format(version=Docker.getADEVersion(self)))
        ade_version.setAlignment(QtCore.Qt.AlignCenter)
        version = QLabel("Docker Version: {version}".format(version=self.getDockerVersion()))
        version.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(ade_version)
        layout.addWidget(version)
        layout.addWidget(self.getDockerImages())

        Gridlayout.addWidget(button_start_ros, 0, 0)
        Gridlayout.addLayout(layout, 0, 1)

        self.setLayout(Gridlayout)

    def getDockerImages(self):
        widget = QWidget()
        layout = QGridLayout()
        list = self.client.images.list()

        label = QLabel("Index")
        label.setAlignment(QtCore.Qt.AlignRight)
        layout.addWidget(label, 0, 0)
        label = QLabel("Image Tag")
        label.setAlignment(QtCore.Qt.AlignLeft)
        layout.addWidget(label, 0, 1)

        for index, image in enumerate(list):
            if(len(image.tags)) > 0:
                label = QLabel("{image}".format(image=image.tags[0]))
                label.setAlignment(QtCore.Qt.AlignLeft)
                indexLabel = QLabel(str(index))
                indexLabel.setAlignment(QtCore.Qt.AlignRight)
                layout.addWidget(indexLabel, index+1, 0)
                layout.addWidget(label, index+1, 1)

        widget.setLayout(layout)

        return widget

    def getDockerVersion(self):
        version = self.client.version()['Components'][0]['Version']
        logging.info("Docker Server version: {version}".format(version=version))
        return version


