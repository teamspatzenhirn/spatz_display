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

    def startScreenSaver(self):
        logging.info("Starting Screensaver")
        screensaver = Screensaver()
        screensaver.showFullScreen()
        screensaver.show()

    def exitGUI(self):
        logging.info("Exit GUI")
        sys.exit()

    def shutdown(self):
        logging.info("Shutting down...")


class SystemTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        layout = QGridLayout()

        button_screensaver = QPushButton("Start Screensaver")
        button_screensaver.clicked.connect(System.startScreenSaver)
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
