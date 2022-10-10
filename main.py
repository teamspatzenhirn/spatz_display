import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QToolBar
from PySide6.QtGui import QAction

import sys

def start_ros():
    print("Starting ROS (maybe)...")

def shutdown():
    print("Shutting down...")
    sys.exit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spatz GUI")

        layout = QGridLayout()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        button_startros = QPushButton("Start ROS")
        button_startros.clicked.connect(start_ros)
        button_startros.setFixedSize(500, 500)


        button_exit = QAction("Exit", self)
        button_exit.triggered.connect(shutdown)

        layout.addWidget(button_startros, 0, 0)
        toolbar.addAction(button_exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.showFullScreen()
window.show()

app.exec()

