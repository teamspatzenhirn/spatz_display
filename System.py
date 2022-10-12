import sys

from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton
)

from setup_logger import logging


class System:
    def __init__(self):
        super().__init__()

    def exitGUI(self):
        logging.info("Exit GUI")
        sys.exit()

    def shutdown(self):
        logging.info("Shutting down...")


class SystemTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        layout = QGridLayout()

        button_exit = QPushButton("Exit GUI")
        button_exit.clicked.connect(System.exitGUI)
        button_exit.setFixedSize(500, 500)

        button_shutdown = QPushButton("Shutdown")
        button_shutdown.clicked.connect(System.shutdown)
        button_shutdown.setFixedSize(500, 500)

        layout.addWidget(button_exit, 0, 0)
        layout.addWidget(button_shutdown, 0, 1)

        self.setLayout(layout)
