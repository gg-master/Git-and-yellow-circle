import sys

from PyQt5.QtCore import Qt
import random
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_file.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.qpm = QPixmap(self.label.width(), self.label.height())
        self.qpm.fill(Qt.transparent)
        qp = QPainter(self.qpm)
        qp.setBrush(Qt.yellow)

        for i in range(15):
            r = random.randrange(5, 100)
            x, y = \
                random.randrange(0, self.label.width() - r), \
                random.randrange(0, self.label.height() - r)
            qp.drawEllipse(x, y, r, r)
        qp.end()

        self.label.setPixmap(self.qpm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
