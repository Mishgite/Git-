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
        self.cursor.execute('''SELECT coffe.id, coffe.variety, coffe.roasting, view.view, 
        coffe.taste_description, coffe.price, coffe.packing_volume 
        FROM coffe INNER JOIN view ON view.ID = coffe.view''')
        coffee_data = self.cursor.fetchall()

        self.cursor.execute('''SELECT * FROM roasting''')
        data0 = self.cursor.fetchall()
        data1 = {}
        for i, j in data0:
            data1[str(i)] = j
        print(data1)

        self.table_widget.setRowCount(len(coffee_data))
        self.table_widget.setColumnCount(7)

        self.table_widget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                    'Описание вкуса', 'Цена', 'Объем упаковки'])

        row = 0
        for data in coffee_data:
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(data[0])))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(data[1])))
            self.table_widget.setItem(row, 2, QTableWidgetItem(data1[str(data[2])]))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(data[3])))
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(data[4])))
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
