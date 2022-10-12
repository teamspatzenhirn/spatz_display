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


class DockerTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        Gridlayout = QGridLayout()

        button_start_ros = QPushButton("Start ROS")
        button_start_ros.clicked.connect(Docker.start_ros)
        button_start_ros.setFixedSize(500, 500)

        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        version = QLabel("Version: {version}".format(version=Docker.getVersion(self)))
        version.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(version)
        images = QLabel("Images: {images}".format(images=Docker.getImages(self)))
        images.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(images)

        Gridlayout.addWidget(button_start_ros, 0, 0)
        Gridlayout.addLayout(layout, 0, 1)

        self.setLayout(Gridlayout)


