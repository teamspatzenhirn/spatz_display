import subprocess

from PySide6 import QtCore
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

    def getVersion(self) -> str:
        docker_version = subprocess.run(['docker', 'version', '--format', "'{{.Server.Version}}'"],
                                        stdout=subprocess.PIPE).stdout.decode("utf-8")
        logging.info("Docker Server version: {version}".format(version=docker_version))
        return docker_version

    def getImages(self) -> str:
        docker_images = subprocess.run(['docker', 'images'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        logging.info("Docker images: {images}".format(images=docker_images))
        return docker_images

    def getADEVersion(self) -> str:
        ade_version = subprocess.run(['/usr/local/bin/ade', '--version'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        logging.info("ADE version: {version}".format(version=ade_version))
        return ade_version


class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

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
        version = QLabel("Docker Version: {version}".format(version=Docker.getVersion(self)))
        version.setAlignment(QtCore.Qt.AlignCenter)
        images = QLabel("Images: {images}".format(images=Docker.getImages(self)))
        images.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(ade_version)
        layout.addWidget(version)
        layout.addWidget(images)

        Gridlayout.addWidget(button_start_ros, 0, 0)
        Gridlayout.addLayout(layout, 0, 1)

        self.setLayout(Gridlayout)


