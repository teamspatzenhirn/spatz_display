import sys
from PySide6.QtWidgets import QApplication
from ViewController import ViewController


def main():
    app = QApplication(sys.argv)
    vc = ViewController()
    vc.show()
    app.exec()


if __name__ == '__main__':
    main()
