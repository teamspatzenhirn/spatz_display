from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout
)

from setup_logger import logging


class IOBoard:
    def __init__(self):
        super().__init__()

    def yeet(self):
        logging.info("YEET")


class IOBoardTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        layout = QGridLayout()

        button_yeet = QPushButton("YEET")
        button_yeet.clicked.connect(IOBoard.yeet)
        button_yeet.setFixedSize(500, 500)

        layout.addWidget(button_yeet, 0, 0)
        self.setLayout(layout)
