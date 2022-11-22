from PySide6.QtGui import (
    QFont,
    QIcon
)

from PySide6.QtCore import (
    QSize
)
from PySide6.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from Docker import DockerTab
from IOBoard import IOBoardTab
from System import SystemTab

from setup_logger import logging

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
        logging.info(f"Display size: {self.disp_width}x{self.disp_height}")

        tab_widget = QTabWidget()
        tab_index1 = tab_widget.addTab(DockerTab(self), "Docker")
        tab_widget.setTabIcon(tab_index1, QIcon('img/docker.webp'))
        tab_widget.setIconSize(QSize(100, 100))
        tab_index2 = tab_widget.addTab(IOBoardTab(self), "IOBoard")
        tab_widget.setTabIcon(tab_index2, QIcon('img/pcbnew.png'))
        tab_widget.setIconSize(QSize(100, 100))
        tab_widget.addTab(SystemTab(self), "System")
        tab_widget.setStyleSheet(f"QTabBar::tab {{ height: {tab_size}px; width: {tab_size}px;}}")
        #tab_widget.setStyleSheet("QTabBar::tab { height: 200px; width: 200px;}")

        #tab_widget.setFont(QFont('Arial', 20))

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
        self.setWindowTitle("Spatz GUI")
        #self.showFullScreen()
