import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QMainWindow, QTableWidgetItem
from ui_log import Ui_MainWindow
import pyodbc


server = r'DESKTOP-MMT3L9P\MSSQLSERVER01'
database = r'TurAgenstvo'

class SQLTreakerNewLog(QMainWindow):
    def __init__(self):
        super(SQLTreakerNewLog, self).__init__()
        self.ui = Ui_MainWindow()
        self.connection = pyodbc.connect(
            f"Driver={{SQL Server}};"
            f"Server={server}; "
            f"Database={database}")
        self.cursor = self.connection.cursor()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.data_tur)
        self.ui.pushButton_2.clicked.connect(self.data_pans)
        self.ui.pushButton_3.clicked.connect(self.data_client)
        self.ui.pushButton_5.clicked.connect(self.data_pytevki)
        self.ui.pushButton_4.clicked.connect(self.data_typecomnat)
        self.ui.comboBox_2.currentTextChanged.connect(self.ifselect)
    def ifselect(self):
        selectbox = self.ui.comboBox_2.currentText()
        if selectbox=="Выборка по количеству комнат":
            self.selectcolvoroom()
        elif selectbox=="Выборка по цене комнат":
            self.selectcosttyperoom()
        elif selectbox=="Выборка Тура по транспорту":
            self.selecttransport()
        elif selectbox=="Выборка Пансионата по городу Сочи и наличию бассейна":
            self.selectcountrybass()
        elif selectbox=="Выборка Пансионата по Городу Анапа или наличию спа-салона":
            self.selectspasalon()
        elif selectbox=="Декатово произведение двух таблиц":
            self.decart()
        elif selectbox=="Сравнение таблиц по равенству 1":
            self.selectjoin1()
        elif selectbox=="Сравнение таблиц по равенству 2":
            self.selectjoin2()
        elif selectbox=="Right join":
            self.selectjoiright()
        elif selectbox=="Left join":
            self.selectjoileft()
        elif selectbox=="Количество клиентов":
            self.selectcolvoclient()
        elif selectbox=="Сумма цены":
            self.selectsumcost()
        elif selectbox=="Группировка по одному столбцу":
            self.groupscolumn()
        else:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)


    def groupscolumn(self):
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID Тура', 'Средняя цена'])
        query = self.cursor.execute("""SELECT
                                         ID_tur,
                                         AVG(Cost) AS Average_Cost
                                        FROM Pytevki
                                        GROUP BY ID_tur;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectsumcost(self):
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Сумма цены'])
        query = self.cursor.execute("""SELECT SUM(Cost) AS total_cost FROM TypeRoom;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectcolvoclient(self):
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Количество клиентов'])
        query = self.cursor.execute("""SELECT COUNT(ID_client) AS clientcount FROM Client;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectjoileft(self):
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'ID Клиента', 'ID Тура', 'Дата начала', 'Дата окончания', 'Цена', 'Статус', 'Имя', 'Фамилия'])
        query = self.cursor.execute("""SELECT Pytevki.*, Client.name, Client.surname
                                                    FROM Pytevki
                                                    LEFT JOIN Client ON Pytevki.ID_Pytevki = Client.ID_client;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectjoiright(self):
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'ID Клиента', 'ID Тура', 'Дата начала', 'Дата окончания', 'Цена', 'Статус', 'Имя', 'Фамилия'])
        query = self.cursor.execute("""SELECT Pytevki.*, Client.name, Client.surname
                                            FROM Pytevki
                                            RIGHT JOIN Client ON Pytevki.ID_Pytevki = Client.ID_client;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))

    def selectjoin2(self):
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Имя', 'Фамилия','Дата начала'])
        query = self.cursor.execute("""
        SELECT Client.name, Client.surname, Pytevki.Date_start
        FROM Pytevki
        JOIN Client ON Pytevki.ID_Pytevki = Client.ID_client;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectjoin1(self):
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'ID Клиента', 'ID Тура', 'Дата начала', 'Дата окончания', 'Цена', 'Статус','Имя','Фамилия'])
        query = self.cursor.execute("""SELECT Pytevki.*, Client.name, Client.surname
                                    FROM Pytevki
                                    JOIN Client ON Pytevki.ID_Pytevki = Client.ID_client;""")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def decart(self):
        self.ui.tableWidget.setColumnCount(14)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'ID Клиента', 'ID Тура', 'Дата начала', 'Дата окончания', 'Цена', 'Статус','ID', 'Имя', 'Фамилия', 'Дата рождения', 'Паспорт', 'Телефон', 'Email'])
        query = self.cursor.execute("SELECT * FROM Pytevki, Client;")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def selectspasalon(self):
        query = f"""SELECT *
        FROM Pansionat
        WHERE City = 'Анапа' OR Spa_salon = 'Да';"""
        self.cursor = self.connection.cursor()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Адрес', 'Город', 'Страна', 'Описание территории', 'Количество комнат', 'Бассейн',
             'Спа-салон', 'Рейтинг', 'Дистанция до моря'])
        query1 = self.cursor.execute(query)
        result = query1.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def selectcountrybass(self):
        query = f"""SELECT *
        FROM Pansionat
        WHERE city = 'Барнаул' AND Bassein = 'Есть';"""
        self.cursor = self.connection.cursor()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Адрес', 'Город', 'Страна', 'Описание территории', 'Количество комнат', 'Бассейн',
             'Спа-салон', 'Рейтинг', 'Дистанция до моря'])
        query1 = self.cursor.execute(query)
        result = query1.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    def selecttransport(self):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Тип транспорта', 'Категория жилья на ночь'])

        query = self.cursor.execute("SELECT * FROM Turi WHERE Type_transport = 'Поезд';")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))

    def selectcosttyperoom(self):
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название комнаты', 'Категория', 'ID пансионата', 'Жилищные условия', 'Цена'])
        query = self.cursor.execute("SELECT * FROM TypeRoom WHERE Cost < 1500;")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))


    def selectcolvoroom(self):
        query = f"""SELECT * FROM Pansionat WHERE Colvo_room > 15;"""
        self.cursor = self.connection.cursor()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Адрес', 'Город', 'Страна', 'Описание территории', 'Количество комнат', 'Бассейн',
             'Спа-салон', 'Рейтинг', 'Дистанция до моря'])
        query1 = self.cursor.execute(query)
        result = query1.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
##функции для показа таблиц
    def data_typecomnat(self):
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название комнаты', 'Категория', 'ID пансионата', 'Жилищные условия', 'Цена'])
        query = self.cursor.execute("SELECT * FROM TypeRoom")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def data_pytevki(self):

        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'ID Клиента', 'ID Тура', 'Дата начала', 'Дата окончания', 'Цена', 'Статус'])
        query = self.cursor.execute("SELECT * FROM  Pytevki")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def data_client(self):

        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Имя', 'Фамилия', 'Дата рождения', 'Паспорт', 'Телефон','Email' ])
        query = self.cursor.execute("SELECT * FROM  Client")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))
    def data_pans(self):

        self.cursor = self.connection.cursor()
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Адрес', 'Город', 'Страна', 'Описание территории', 'Количество комнат', 'Бассейн', 'Спа-салон', 'Рейтинг', 'Дистанция до моря'])
        query = self.cursor.execute("SELECT * FROM  Pansionat")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_nmber, QTableWidgetItem(str(data)))

    def data_tur(self):

        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Тип транспорта', 'Категория жилья на ночь'])

        query = self.cursor.execute("SELECT * FROM Turi")
        result = query.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_nmber, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number,column_nmber, QTableWidgetItem(str(data)))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SQLTreakerNewLog()
    window.show()

    sys.exit(app.exec())
