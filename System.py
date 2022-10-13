import sys

from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton
)

from setup_logger import logging
from Screensaver import Screensaver


class System:
    def __init__(self):
        super().__init__()

    def exitGUI(self):
        logging.info("Exit GUI")
        sys.exit()

    def shutdown(self):
        logging.info("Shutting down...")


class SystemTab(QWidget):
    def __init__(self, parent: QWidget, app):
        super().__init__(parent)
        self.app = app

        layout = QGridLayout()

        button_screensaver = QPushButton("Start Screensaver")
        button_screensaver.clicked.connect(self.startScreenSaver)
        button_screensaver.setFixedSize(400, 400)

        button_exit = QPushButton("Exit GUI")
        button_exit.clicked.connect(System.exitGUI)
        button_exit.setFixedSize(400, 400)

        button_shutdown = QPushButton("Shutdown")
        button_shutdown.clicked.connect(System.shutdown)
        button_shutdown.setFixedSize(400, 400)

        layout.addWidget(button_screensaver, 0, 0)
        layout.addWidget(button_exit, 1, 0)
        layout.addWidget(button_shutdown, 1, 1)

        self.setLayout(layout)

    def startScreenSaver(self):
        logging.info("Starting Screensaver")
        self.screensaver = Screensaver(self.app)
        self.screensaver.running = True
        self.screensaver.showFullScreen()