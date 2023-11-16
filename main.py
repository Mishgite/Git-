from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import random


class CircleButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 1000)

        self.button = QPushButton("Рисовать", self)
        self.button.setGeometry(10, 50, 80, 40)
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
        color = QColor(Qt.yellow)
        qp.setBrush(color)
        qp.drawEllipse(150, 150, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleButton()
    window.show()
    sys.exit(app.exec_())
