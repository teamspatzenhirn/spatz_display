import PySide6.QtCore
from PySide6.QtWidgets import (
        QApplication,
        QWidget,
        QMainWindow,
        QPushButton,
        QGridLayout,
        QToolBar,
        QDialog,
        QVBoxLayout,
        QLabel
)

from PySide6.QtGui import QAction

import sys
import subprocess
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)



toolbar_height = 100


def start_ros():
    logging.info("Starting ROS (maybe)...")

def yeet():
    logging.info("YEET")
def shutdown():
    logging.info("Shutting down...")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spatz GUI")

        layout = QGridLayout()

        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFixedHeight(toolbar_height)
        self.addToolBar(toolbar)

        button_docker = QPushButton("Docker")
        button_docker.clicked.connect(self.docker_version)
        button_docker.setFixedHeight(toolbar_height - toolbar_height * .1)

        button_exit = QPushButton("Exit")
        button_exit.clicked.connect(shutdown)
        button_exit.setFixedHeight(toolbar_height-toolbar_height*.1)

        button_startros = QPushButton("Start ROS")
        button_startros.clicked.connect(start_ros)
        button_startros.setFixedSize(500, 500)

        button_yeet = QPushButton("YEET")
        button_yeet.clicked.connect(yeet)
        button_yeet.setFixedSize(500, 500)


        layout.addWidget(button_startros, 0, 0)
        layout.addWidget(button_yeet, 0, 1)

        toolbar.addWidget(button_docker)
        toolbar.addSeparator()
        toolbar.addWidget(button_exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def docker_version(self):
        docker_version = subprocess.run(['docker', 'version', '--format', "'{{.Server.Version}}'"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        docker_images = subprocess.run(['docker', 'images'], stdout=subprocess.PIPE).stdout.decode("utf-8")
        logging.info("Docker images: {images}".format(images=docker_images))
        logging.info("Docker Server version: {version}".format(version=docker_version))

        dlg = QDialog(self)
        dlg.setWindowTitle("Docker")
        dlg.layout = QVBoxLayout()
        dlg.layout.addWidget(QLabel("Version: {version}".format(version=docker_version)))
        dlg.layout.addWidget(QLabel("Images: \n{version}".format(version=docker_images)))
        dlg.setLayout(dlg.layout)
        dlg.exec()

app = QApplication(sys.argv)

window = MainWindow()
window.showFullScreen()
window.show()

app.exec()

