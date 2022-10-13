import sys
import random, math
import numpy as np

from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QPropertyAnimation, QPoint


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

    def __init__(self, app):
        super().__init__()

        # display size
        self.disp_width = app.primaryScreen().size().width()
        self.disp_height = app.primaryScreen().size().height()

        self.setStyleSheet("background-color:black")
        self.child = QSvgWidget("img/spatz.svg", self)
        self.child.resize(Screensaver.spatz_width, Screensaver.spatz_height)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.finished.connect(self.moveSpatz)
        self.moveSpatz()

    def moveSpatz(self):

        disp_width = self.disp_width
        disp_height = self.disp_height

        # last target
        p1 = np.array([Screensaver.last_pos[0], Screensaver.last_pos[1]])

        # current pos
        p2 = np.array([self.child.pos().x(), self.child.pos().y()])

        # last movement
        v1 = p2-p1

        # corner top left
        if (p2==np.array([0, 0])).all():
            xy = random.choice(['x', 'y'])
            if xy == 'x':
                x = random.randint(disp_width / 4, disp_width - Screensaver.spatz_width - disp_width / 4)
                y = disp_height - Screensaver.spatz_height
            if xy == 'y':
                x = self.disp_width - Screensaver.spatz_width
                y = random.randint(disp_height / 4, disp_height - Screensaver.spatz_height - disp_height / 4)
        # corner bottom left
        if (p2==np.array([0, disp_height-Screensaver.spatz_height])).all():
            xy = random.choice(['x', 'y'])
            if xy == 'x':
                x = random.randint(disp_width / 4, disp_width - Screensaver.spatz_width - disp_width / 4)
                y = disp_height - Screensaver.spatz_height
            if xy == 'y':
                x = disp_width - Screensaver.spatz_width
                y = random.randint(disp_height / 4, disp_height - Screensaver.spatz_height - disp_height / 4)

        # corner top right
        if (p2==np.array([disp_width-Screensaver.spatz_width, 0])).all():
            xy = random.choice(['x', 'y'])
            if xy == 'x':
                x = random.randint(disp_width / 4, disp_width - Screensaver.spatz_width - disp_width / 4)
                y = disp_height - Screensaver.spatz_height
            if xy == 'y':
                x = disp_width - Screensaver.spatz_width
                y = random.randint(disp_height / 4, disp_height - Screensaver.spatz_height - disp_height / 4)
        # corner bottom right
        if (p2==np.array([disp_width-Screensaver.spatz_width, disp_height-Screensaver.spatz_height])).all():
            xy = random.choice(['x', 'y'])
            if xy == 'x':
                x = random.randint(disp_width / 4, disp_width - Screensaver.spatz_width - disp_width / 4)
                y = disp_height - Screensaver.spatz_height
            if xy == 'y':
                x = disp_width - Screensaver.spatz_width
                y = random.randint(disp_height / 4, disp_height - Screensaver.spatz_height - disp_height / 4)


        # hits Y right
        elif (p2[0] == disp_width-Screensaver.spatz_width):
            v2 = v1 * np.array([-1, 1])
            # possible new target: x top
            target1 = get_intersect(p2, p2 + v2, [0, 0], [disp_width - Screensaver.spatz_width, 0])
            if (target1[0] >= 0 and target1[0] <= disp_width - Screensaver.spatz_width):
                x, y = target1
            # possible new target: x bottom
            target2 = get_intersect(p2, p2 + v2, [0, disp_height-Screensaver.spatz_height], [disp_width-Screensaver.spatz_width, disp_height-Screensaver.spatz_height])
            if(target2[0] >= 0 and target2[0] <= disp_width-Screensaver.spatz_width):
                x, y = target2
            # possible new target: y left
            target3 = get_intersect(p2, p2 + v2, [0, 0], [0, disp_height-Screensaver.spatz_height])
            if(target3[1] >= 0 and target3[1] <= disp_height-Screensaver.spatz_height):
                x, y = target3

        # hits Y left
        elif (p2[0] == 0):
            v2 = v1 * np.array([-1, 1])
            # possible new target: x top
            target1 = get_intersect(p2, p2 + v2, [0, 0], [disp_width - Screensaver.spatz_width, 0])
            if (target1[0] >= 0 and target1[0] <= disp_width - Screensaver.spatz_width):
                x, y = target1
            # possible new target: x bottom
            target2 = get_intersect(p2, p2 + v2, [0, disp_height-Screensaver.spatz_height], [disp_width-Screensaver.spatz_width, disp_height-Screensaver.spatz_height])
            if(target2[0] >= 0 and target2[0] <= disp_width-Screensaver.spatz_width):
                x, y = target2
            # possible new target: y right
            target3 = get_intersect(p2, p2 + v2, [disp_width-Screensaver.spatz_width, 0], [disp_width-Screensaver.spatz_width, disp_height])
            if(target3[1] >= 0 and target3[1] <= disp_height-Screensaver.spatz_height):
                x, y = target3

        # hits X bottom
        elif (p2[1] == disp_height-Screensaver.spatz_height):
            v2 = v1 * np.array([1, -1])
            # possible new target: x top
            target1 = get_intersect(p2, p2+v2, [0, 0], [disp_width-Screensaver.spatz_width, 0])
            if(target1[0] >= 0 and target1[0] <= disp_width-Screensaver.spatz_width):
                x, y = target1
            # possible new target: y right
            target2 = get_intersect(p2, p2 + v2, [disp_width-Screensaver.spatz_width, 0], [disp_width-Screensaver.spatz_width, disp_height])
            if(target2[1] >= 0 and target2[1] <= disp_height-Screensaver.spatz_height):
                x, y = target2
            # possible new target: y left
            target3 = get_intersect(p2, p2 + v2, [0, 0], [0, disp_height-Screensaver.spatz_height])
            if(target3[1] >= 0 and target3[1] <= disp_height-Screensaver.spatz_height):
                x, y = target3

        # hits X top
        elif (p2[1] == 0):
            v2 = v1 * np.array([1, -1])
            # possible new target: x bottom
            target1 = get_intersect(p2, p2 + v2, [0, disp_height-Screensaver.spatz_height], [disp_width-Screensaver.spatz_width, disp_height-Screensaver.spatz_height])
            if(target1[0] >= 0 and target1[0] <= disp_width-Screensaver.spatz_width):
                x, y = target1
            # possible new target: y right
            target2 = get_intersect(p2, p2 + v2, [disp_width-Screensaver.spatz_width, 0], [disp_width-Screensaver.spatz_width, disp_height])
            if(target2[1] >= 0 and target2[1] <= disp_height-Screensaver.spatz_height):
                x, y = target2
            # possible new target: y left
            target3 = get_intersect(p2, p2 + v2, [0, 0], [0, disp_height-Screensaver.spatz_height])
            if(target3[1] >= 0 and target3[1] <= disp_height-Screensaver.spatz_height):
                x, y = target3

        speed = 1
        distance = math.sqrt((self.child.pos().x() - x) ** 2 + (self.child.pos().y() - y) ** 2)
        time = round(distance / speed)

        print("Target: " + str(x) + ", " + str(y))
        self.anim.setEndValue(QPoint(x, y))
        self.anim.setDuration(time)
        self.anim.start()

        Screensaver.last_pos = p2


    def mousePressEvent(self, e):
        print("Closing Screensaver")
        self.running = False
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screensaver = Screensaver(app)
    screensaver.showFullScreen()
    screensaver.show()
    app.exec()
