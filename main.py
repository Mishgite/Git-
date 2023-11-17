import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sqlite3


class CoffeeInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Coffee Info')
        self.setGeometry(100, 100, 600, 500)
        self.layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

        self.connection = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connection.cursor()

        self.get_coffee_info()

    def get_coffee_info(self):
        self.cursor.execute('SELECT * FROM coffe')
        coffee_data = self.cursor.fetchall()

        self.table_widget.setRowCount(len(coffee_data))
        self.table_widget.setColumnCount(7)

        self.table_widget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                      'Описание вкуса', 'Цена', 'Объем упаковки'])

        row = 0
        for data in coffee_data:
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(data[0])))
            self.table_widget.setItem(row, 1, QTableWidgetItem(data[1]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(data[2]))
            self.table_widget.setItem(row, 3, QTableWidgetItem(data[3]))
            self.table_widget.setItem(row, 4, QTableWidgetItem(data[4]))
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(data[5])))
            self.table_widget.setItem(row, 6, QTableWidgetItem(str(data[6])))

            row += 1

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeInfoApp()
    window.show()
    sys.exit(app.exec_())
