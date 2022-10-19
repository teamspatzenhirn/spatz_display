import socket, time

from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout
)

from setup_logger import logging

import container_pb2, setpoint_pb2, time_pb2


class IOBoardTab(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        logging.info("Open Socket to IOBoard")

        app = self.parent().app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        btn_size = self.disp_width / 5

        layout = QGridLayout()

        button_yeet = QPushButton("YEET")
        button_yeet.clicked.connect(self.yeet)
        button_yeet.setFixedSize(btn_size, btn_size)

        layout.addWidget(button_yeet, 0, 0)
        self.setLayout(layout)

    def yeet(self):
        msg = container_pb2.NUCtoIOBoardContainer()
        t = time_pb2.TimeStamp()
        t.nanoseconds = int(time.time()) * 10 ** 9  # time since epoch in ns
        msg.yeetSetpoint.CopyFrom(setpoint_pb2.YeetSetpoint())
        msg.timeStamp.CopyFrom(t)
        binary = msg.SerializeToString()
        # send UDP packet to IOBoard
        self.sock.sendto(bytes(binary), ('10.0.0.2', 1337))
        logging.info("YEET")
