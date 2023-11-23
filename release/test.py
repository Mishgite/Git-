import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, \
    QMainWindow, QLabel, QLineEdit, QComboBox, QPlainTextEdit
import sqlite3


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('Фильмотека')

        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        self.addButton = QPushButton('добавить')
        self.layout.addWidget(self.addButton)

        self.setLayout(self.layout)

        self.addButton.clicked.connect(self.adding)

        self.load_data()

    def load_data(self):
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.cur.execute('''SELECT coffe.id, coffe.variety, coffe.roasting, view.view, 
        coffe.taste_description, coffe.price, coffe.packing_volume 
        FROM coffe INNER JOIN view ON view.ID = coffe.view''')
        films = self.cur.fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(films))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
             'Описание вкуса', 'Цена', 'Объем упаковки'])

        self.cur.execute('''SELECT * FROM roasting''')
        data0 = self.cur.fetchall()
        data1 = {}
        for i, j in data0:
            data1[str(i)] = j
        row = 0
        for data in films:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(data[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(data[1])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(data1[str(data[2])]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(data[3])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(data[4])))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(data[5])))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(data[6])))

            row += 1

    def adding(self):

        self.add_form = AddWidget(self)
        self.add_form.show()

    def update_result(self):
        self.load_data()


class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        self.setWindowTitle('Add Film')

        self.central_widget = QWidget()

        self.layout = QVBoxLayout()

        self.variety = QLabel("Название сорта")
        self.title = QPlainTextEdit()
        self.layout.addWidget(self.variety)
        self.layout.addWidget(self.title)

        self.roasting = QLabel("Степень обжарки")
        self.roastingBox = QComboBox()
        self.params = {}
        result = cur.execute('''SELECT * FROM roasting''').fetchall()
        for i in result:
            self.params[i[1]] = i[0]
            self.roastingBox.addItem(i[1])
        self.layout.addWidget(self.roasting)
        self.layout.addWidget(self.roastingBox)

        self.durationLabel = QLabel("Молотый/в зернах")
        self.durationBox = QComboBox()
        self.params1 = {}
        result = cur.execute('''SELECT * FROM view''').fetchall()
        for i in result:
            self.params1[i[1]] = i[0]
            self.durationBox.addItem(i[1])
        self.layout.addWidget(self.durationLabel)
        self.layout.addWidget(self.durationBox)

        self.genreLabel = QLabel('Описание вкуса')
        self.description = QPlainTextEdit()
        self.layout.addWidget(self.genreLabel)
        self.layout.addWidget(self.description)

        self.genreLabel = QLabel('Цена')
        self.price = QPlainTextEdit()
        self.layout.addWidget(self.genreLabel)
        self.layout.addWidget(self.price)

        self.genreLabel = QLabel('Объем упаковки')
        self.packing_volume = QPlainTextEdit()
        self.layout.addWidget(self.genreLabel)
        self.layout.addWidget(self.packing_volume)

        self.pushButton = QPushButton('Добавить')
        self.layout.addWidget(self.pushButton)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.adding_verdict = True

        self.pushButton.clicked.connect(self.add_film)

    def get_adding_verdict(self):
        if self.adding_verdict:
            return True
        else:
            return False

    def add_film(self):
        if (self.title.toPlainText() == '' or self.description.toPlainText() == ''
                or self.price.toPlainText() == '' or self.packing_volume.toPlainText() == ''):
            self.adding_verdict = False
            self.get_adding_verdict()
            self.statusBar().showMessage('Не верно заполнина форма')
        else:
            self.con = sqlite3.connect('coffee.sqlite')
            self.cur = self.con.cursor()
            self.adding_verdict = True
            self.get_adding_verdict()
            ib = 0
            for i in self.cur.execute("SELECT id from coffe ORDER BY id DESC").fetchall():
                ib = i[0]
                break
            title = self.title.toPlainText()
            genre = self.params[self.roastingBox.currentText()]
            duration = self.params1[self.durationBox.currentText()]
            description = self.description.toPlainText()
            price = self.price.toPlainText()
            packing_volume = self.packing_volume.toPlainText()

            self.cur.execute("""INSERT INTO coffe (id, variety, roasting, 
            view, taste_description, price, packing_volume) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                             (ib + 1, title, genre, duration, description, price, packing_volume))
            self.con.commit()
            self.parent().update_result()
            self.con.close()

            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
