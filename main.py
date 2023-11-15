from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF
from random import randint
import sys


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle('Жёлтый круг')
        self.circles = []

        self.draw = QPushButton(self)
        self.draw.move(300, 10)
        self.draw.setText("Рисовать")
        self.draw.clicked.connect(self.generate_circle)

    def generate_circle(self):
        self.circles.append((randint(1, 200), randint(0, 1000), randint(0, 1000)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for diameter, x, y in self.circles:
            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.yellow)
            painter.drawEllipse(QRectF(x - diameter / 2, y - diameter / 2, diameter, diameter))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circle()
    window.show()
    sys.exit(app.exec_())
