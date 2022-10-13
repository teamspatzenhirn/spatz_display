from PySide6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QDialog
)

from Docker import DockerTab
from IOBoard import IOBoardTab
from System import SystemTab
from Screensaver import Screensaver


class ViewController(QDialog):

    def __init__(self, app):
        self.app = app
        super(ViewController, self).__init__()

        self.initUI(app)

    def initUI(self, app):
        tab_widget = QTabWidget()

        tab_widget.addTab(DockerTab(self), "Docker")
        tab_widget.addTab(IOBoardTab(self), "IOBoard")
        tab_widget.addTab(SystemTab(self, self.app), "System")
        tab_widget.setStyleSheet("QTabBar::tab { height: 200px; width: 200px;}")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Spatz GUI")
        self.showFullScreen()

    def mousePressEvent(self, QMouseEvent):
        # print mouse position
        print(QMouseEvent.pos())
        SystemTab.stopScreenSaver()

