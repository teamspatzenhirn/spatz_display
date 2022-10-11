import subprocess
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel
)

from setup_logger import logging


class Docker:
    def __init__(self):
        super().__init__()

    def start_ros(self):
        logging.info("Starting ROS (maybe)...")

    def docker_info(self):
        docker_version = subprocess.run(['docker', 'version', '--format', "'{{.Server.Version}}'"],
                                        stdout=subprocess.PIPE).stdout.decode("utf-8")
        docker_images = subprocess.run(['docker', 'images'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        logging.info("Docker images: {images}".format(images=docker_images))
        logging.info("Docker Server version: {version}".format(version=docker_version))

        dlg = QDialog()
        dlg.setWindowTitle("Docker")
        dlg.layout = QVBoxLayout()
        dlg.layout.addWidget(QLabel("Version: {version}".format(version=docker_version)))
        dlg.layout.addWidget(QLabel("Images: \n{version}".format(version=docker_images)))
        dlg.setLayout(dlg.layout)
        dlg.exec()
