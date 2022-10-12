from PySide6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QDialog
)

from Docker import DockerTab
from IOBoard import IOBoardTab
from System import SystemTab


class ViewController(QDialog):

    def __init__(self):
        super(ViewController, self).__init__()

        self.initUI()

    def initUI(self):
        tab_widget = QTabWidget()

        tab_widget.addTab(DockerTab(self), "Docker")
        tab_widget.addTab(IOBoardTab(self), "IOBoard")
        tab_widget.addTab(SystemTab(self), "System")
        tab_widget.setStyleSheet("QTabBar::tab { height: 200px; width: 200px;}")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Spatz GUI")
        self.showFullScreen()
