from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QToolBar
)

from Docker import Docker
from IOBoard import IOBoard
from System import System


class ViewController(QMainWindow):

    def __init__(self):
        super(ViewController, self).__init__()

        self.initUI()

    def initUI(self, toolbar_height=100):
        self.setWindowTitle("Spatz GUI")

        layout = QGridLayout()

        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFixedHeight(toolbar_height)
        self.addToolBar(toolbar)

        button_docker = QPushButton("Docker")
        button_docker.clicked.connect(Docker.docker_info)
        button_docker.setFixedHeight(toolbar_height - toolbar_height * .1)

        button_exit = QPushButton("Exit")
        button_exit.clicked.connect(System.shutdown)
        button_exit.setFixedHeight(toolbar_height - toolbar_height * .1)

        button_startros = QPushButton("Start ROS")
        button_startros.clicked.connect(Docker.start_ros)
        button_startros.setFixedSize(500, 500)

        button_yeet = QPushButton("YEET")
        button_yeet.clicked.connect(IOBoard.yeet)
        button_yeet.setFixedSize(500, 500)

        layout.addWidget(button_startros, 0, 0)
        layout.addWidget(button_yeet, 0, 1)

        toolbar.addWidget(button_docker)
        toolbar.addSeparator()
        toolbar.addWidget(button_exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.showFullScreen()
