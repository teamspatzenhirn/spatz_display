import sys
import random, math
import numpy as np

from PySide6 import QtSvg, QtSvgWidgets
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QApplication, QLabel
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve


def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)


class Screensaver(QWidget):
    spatz_width, spatz_height = 300, 300

    last_pos = (0, 0)

    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color:black")
        self.child = QSvgWidget("img/spatz.svg", self)
        self.child.resize(Screensaver.spatz_width, Screensaver.spatz_height)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.finished.connect(self.moveSpatz)
        self.moveSpatz()

    def moveSpatz(self):
        width = app.primaryScreen().size().width()
        height = app.primaryScreen().size().height()

        # Ziel vom letzen mal
        a1 = np.array([Screensaver.last_pos[0], Screensaver.last_pos[1]])

        # Aktuelle pos
        a2 = np.array([self.child.pos().x(), self.child.pos().y()])

        print("a1: " + str(a1))
        print("a2: " + str(a2))

        # TODO: drei letzen Ecken prüfen
        if (a2==np.array([0, 0])).all():
            xy = random.choice(['x', 'y'])
            if xy == 'x':
                x = random.randint(width / 4, width - Screensaver.spatz_width - width / 4)
                y = height - Screensaver.spatz_height
            if xy == 'y':
                x = width - Screensaver.spatz_width
                y = random.randint(height / 4, height - Screensaver.spatz_height - height / 4)


        if (a2[0] == width-Screensaver.spatz_width): #schneidet Y rechts
            print("Y rechts gehittet")
            print(get_intersect(a2, (a2[0], -a2[1]), (0, height), (width, height)))

        if (a2[0] == 0): #schneidet Y links
            print("Y links gehittet")

        if (a2[1] == height-Screensaver.spatz_height): #schneidet X unten
            print("X unten gehittet")
            # Schnittpunkt Y Achse
            print(get_intersect(a2, (-a2[0]-a1, a2[1]-a1), (0, width), (width, height)))
            # Schnittpunkt X Achse
            print(get_intersect(a2, (-a2[0], a2[1]), (0, 0), (width, 0)))

        if (a2[1] == 0): #schneidet X oben
            print("X oben gehittet")

        speed = 1
        distance = math.sqrt((self.child.pos().x() - x) ** 2 + (self.child.pos().y() - y) ** 2)
        time = round(distance / speed)

        print("Ziel: " + str(x) + ", " + str(y))
        self.anim.setEndValue(QPoint(x, y))
        self.anim.setDuration(time)
        self.anim.start()

        Screensaver.last_pos = a2

    def mousePressEvent(self, e):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensaver = Screensaver()
    screensaver.showFullScreen()
    screensaver.show()
    app.exec()
