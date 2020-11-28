import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()
        self.coords = [150, 150]
        self.s = 0
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.flag = False

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.btn_draw.clicked.connect(self.rands)
        self.show()

    def rands(self):
        self.s = randint(1, 200)
        self.paint()

    def paint(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.qp.setBrush(self.color)
        self.qp.drawEllipse(self.coords[0] - self.s // 2, self.coords[1] - self.s // 2, self.s, self.s)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()