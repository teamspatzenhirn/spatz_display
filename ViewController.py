from PySide6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QWidget
)

from Docker import DockerTab
from IOBoard import IOBoardTab
from System import SystemTab


class ViewController(QWidget):

    def __init__(self, app):
        self.app = app
        super(ViewController, self).__init__()

        self.initUI(app)

    def initUI(self, app):

        app = self.app
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()
        tab_size = round(self.disp_height/5)

        tab_widget = QTabWidget()

        tab_widget.addTab(DockerTab(self), "Docker")
        tab_widget.addTab(IOBoardTab(self), "IOBoard")
        tab_widget.addTab(SystemTab(self), "System")
        tab_widget.setStyleSheet(f"QTabBar::tab {{ height: {tab_size}px; width: {tab_size}px;}}")
        #tab_widget.setStyleSheet("QTabBar::tab { height: 200px; width: 200px;}")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Spatz GUI")
        self.showFullScreen()
