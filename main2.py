import sys

from PyQt5.QtCore import Qt
import random
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import *
import ui_file_2


class Example(QWidget, ui_file_2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.qpm = QPixmap(self.label.width(), self.label.height())
        self.qpm.fill(Qt.transparent)
        qp = QPainter(self.qpm)
        for i in range(15):
            qp.setBrush(QColor(random.randrange(0, 255),
                               random.randrange(0, 255),
                               random.randrange(0, 255)))
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
