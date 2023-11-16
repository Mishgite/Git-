from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import random


class CircleButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500)

        self.button = QPushButton("Рисовать", self)
        self.button.setGeometry(0, 0, 50, 20)
        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        size = random.randint(1, 500)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        qp.setBrush(color)
        qp.drawEllipse(random.randint(1, 500), random.randint(1, 500), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleButton()
    window.show()
    sys.exit(app.exec_())
