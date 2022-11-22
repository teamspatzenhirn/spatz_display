import subprocess, os
import docker

from PySide6 import QtCore

from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QWidget,
    QGridLayout,
    QPushButton,
    QPlainTextEdit
)

from setup_logger import logging


class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.ade_path = '/usr/local/bin/ade'

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width / 5

        Gridlayout = QGridLayout()

        button_start_ros = QPushButton("Start ROS")
        button_start_ros.clicked.connect(self.start_ros)
        button_start_ros.setFixedSize(btn_size, btn_size)

        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        ade_version = QLabel(f"ADE Version: {self.getADEVersion()}")
        ade_version.setAlignment(QtCore.Qt.AlignCenter)
        version = QLabel(f"Docker Version: {self.getDockerVersion()}")
        version.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(ade_version)
        layout.addWidget(version)
        layout.addWidget(self.getDockerImages())

        self.terminal = QPlainTextEdit()
        self.terminal.setReadOnly(True)

        self.p = QtCore.QProcess()

        Gridlayout.addWidget(button_start_ros, 0, 0)
        Gridlayout.addLayout(layout, 0, 1)
        Gridlayout.addWidget(self.terminal, 1, 1)

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
            if (len(image.tags)) > 0:
                label = QLabel(f"{image.tags[0]}")
                label.setAlignment(QtCore.Qt.AlignLeft)
                indexLabel = QLabel(str(index))
                indexLabel.setAlignment(QtCore.Qt.AlignRight)
                layout.addWidget(indexLabel, index + 1, 0)
                layout.addWidget(label, index + 1, 1)

        widget.setLayout(layout)

        return widget

    def getDockerVersion(self):
        version = self.client.version()['Components'][0]['Version']
        logging.info(f"Docker Server version: {version}")
        return version

    def start_ros(self):
        logging.info("Starting ROS (maybe)...")
        self.terminal.clear()
        if os.path.isfile(self.ade_path):
            # ~/ade-home/2021$ ade start
            # ~/ade-home/2021$ ade enter
            self.p.start(self.ade_path, ["start"])
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)

        else:
            self.terminal.appendPlainText("ADE not found")
            return "ADE not found"

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.terminal.appendPlainText(stdout)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.terminal.appendPlainText(stderr)

    def getADEVersion(self) -> str:
        if os.path.isfile(self.ade_path):
            ade_version = subprocess.run([self.ade_path, '--version'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        else:
            return "ADE not found"
        logging.info(f"ADE version: {ade_version}")
        return ade_version
