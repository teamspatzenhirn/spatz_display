from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout
)

from setup_logger import logging

import protobuf_generated.container_pb2 as Container_pb2
from protobuf_generated import setpoint_pb2

import socket


class IOBoard:
    def __init__(self):
        super().__init__()

    def yeet(self):
        logging.info("YEET")
        msg = Container_pb2.NUCtoIOBoardContainer()
        msg.yeetSetpoint = setpoint_pb2.YeetSetpoint()
        binary = msg.SerializeToString()
        # send UDP packet to IOBoard
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(binary, "utf-8"), ('10.0.0.2', 1337))


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
