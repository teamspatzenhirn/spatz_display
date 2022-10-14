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

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width/5

        layout = QGridLayout()

        button_yeet = QPushButton("YEET")
        button_yeet.clicked.connect(IOBoard.yeet)
        button_yeet.setFixedSize(btn_size, btn_size)

        layout.addWidget(button_yeet, 0, 0)
        self.setLayout(layout)
