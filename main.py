import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from ViewController import ViewController

import qdarktheme

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    app.setFont(QFont('Arial', 20), "QLabel")
    app.setFont(QFont('Arial', 20), "QPushButton")
    app.setFont(QFont('Arial', 20), "QTabWidget")


    vc = ViewController(app)
    vc.showFullScreen()

    app.exec()


if __name__ == '__main__':
    main()
