import sys
from ui_clientred import Ui_DialogClient
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QMainWindow, QTableWidgetItem
from ui_gui2 import Ui_MainWindow
import pyodbc
from ui_zayvka import Ui_Dialog
from ui_pytevki import Ui_petevki
from ui_typeroom import Ui_typeroom
from ui_pans import Ui_pansionat

server = r'DESKTOP-MMT3L9P\MSSQLSERVER01'
database = r'TurAgenstvo'

class SqlTreaker(QMainWindow):
    def __init__(self):
        super(SqlTreaker, self).__init__()
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
        self.ui.pushButton_6.clicked.connect(self.windowturiopen)
        self.ui.pushButton_8.clicked.connect(self.windowclientopen)
        self.ui.pushButton_10.clicked.connect(self.windowpytevkiopen)
        self.ui.pushButton_9.clicked.connect(self.windowopentype)
        self.ui.pushButton_7.clicked.connect(self.windowopenpans)
        self.ui.comboBox_2.currentTextChanged.connect(self.ifselect)


    def windowopenpans(self):
        self.new_window4 = QtWidgets.QDialog()
        self.ui_window4 = Ui_pansionat()
        self.ui_window4.setupUi(self.new_window4)
        self.new_window4.show()
        self.ui_window4.pushButton.clicked.connect(self.red_pansion)

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


    def windowopentype(self):
        self.new_window3 = QtWidgets.QDialog()
        self.ui_window3 = Ui_typeroom()
        self.ui_window3.setupUi(self.new_window3)
        self.new_window3.show()
        self.ui_window3.pushButton.clicked.connect(self.red_typeroom)


    def windowpytevkiopen(self):
        self.new_window2 = QtWidgets.QDialog()
        self.ui_window2 = Ui_petevki()
        self.ui_window2.setupUi(self.new_window2)
        self.new_window2.show()
        self.ui_window2.pushButton.clicked.connect(self.red_pytevki)

    def red_pansion(self):
        name = self.ui_window4.lineEditNamePans.text()
        adres = self.ui_window4.lineEditAdres.text()
        city = self.ui_window4.lineEditCity.text()
        country = self.ui_window4.lineEditCountry.text()
        desc_ter = self.ui_window4.lineEditCountry_2.text()
        colvoroom = self.ui_window4.lineEditColvoRoom.text()
        bass = self.ui_window4.comboBoxBassein.currentText()
        spa = self.ui_window4.comboBoxSpaSalon.currentText()
        lvl = self.ui_window4.lineEditColvoRoom_2.text()
        distofsea = self.ui_window4.lineEditDistofsea.text()
        id = self.ui_window4.lineEditDelIDpans.text()
        if name=="" and adres =="" and city=="" and country=="" and desc_ter=="" and colvoroom=="" and lvl=="" and distofsea=="":
            self.new_window4.close()
        else:
            queryins4 = f"""
            INSERT INTO Pansionat (Name_Pansionat, Adress, City, Country, Desc_terr, Colvo_room, Bassein, Spa_salon, Lvl, Dist_to_sea) 
            VALUES 
            ('{name}', '{adres}', '{city}', '{country}', '{desc_ter}', '{colvoroom}', '{bass}', '{spa}', '{lvl}', '{distofsea}');
            """
            self.cursor.execute(queryins4)
            self.cursor.commit()
            self.new_window4.close()
        if id == "":
            self.new_window4.close()
        else:
            queryins7 = f"DELETE FROM Pansionat WHERE ID_Pansionat = {id}"
            self.cursor.execute(queryins7)
            self.cursor.commit()
            self.new_window4.close()


    def red_typeroom(self):
        nameroom = self.ui_window3.lineEditNameRoom.text()
        category = self. ui_window3.comboBoxCAt.currentText()
        pansID = self.ui_window3.lineEditIdpans.text()
        livcound = self.ui_window3.lineEditzilysl.text()
        cost = self.ui_window3.lineEditcost.text()
        id = self.ui_window3.lineEditDelIDtyperoom.text()
        if nameroom=="" and pansID =="" and cost=="" and livcound=="":
            self.new_window3.close()
        else:
            queryins4 = f"""
            INSERT INTO TypeRoom (NameRoom, Caregory, Pansionat_ID, Living_cound, Cost) 
            VALUES  
            ('{nameroom}', '{category}', '{pansID}', '{livcound}', '{cost}');
            """
            self.cursor.execute(queryins4)
            self.cursor.commit()
            self.new_window3.close()
        if id == "":
            self.new_window3.close()
        else:
            queryins7 = f"DELETE FROM TypeRoom WHERE ID_TypeRoom = {id}"
            self.cursor.execute(queryins7)
            self.cursor.commit()
            self.new_window3.close()
    def red_pytevki(self):
        idclient = self.ui_window2.lineEditIDClient.text()
        idtur = self.ui_window2.lineEditIDTur.text()
        datestart = self.ui_window2.dateEditstart.date()
        formatted_datestart = datestart.toString("yyyy-MM-dd")
        dateend = self.ui_window2.dateEditend.date()
        formatted_dateend = dateend.toString("yyyy-MM-dd")
        cost = self.ui_window2.lineEditCost.text()
        stat = self.ui_window2.comboBoxStatus.currentText()

        id = self.ui_window2.lineEditDelIDPt.text()
        if idclient=="" and idtur =="" and cost=="" :
            self.new_window2.close()
        else:
            queryins3 = f"""
            INSERT INTO Pytevki (ID_Client, ID_tur, Date_start, Date_over, Cost, Status)
            VALUES 
            ('{idclient}', '{idtur}', '{formatted_datestart}', '{formatted_dateend}', '{cost}', '{stat}');
            """
            self.cursor.execute(queryins3)
            self.cursor.commit()
            self.new_window2.close()
        if id == "":
            self.new_window2.close()
        else:
            queryins1 = f"DELETE FROM Pytevki WHERE ID_Pytevki = {id}"
            self.cursor.execute(queryins1)
            self.cursor.commit()
            self.new_window2.close()

    def windowturiopen(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.pushButton.clicked.connect(self.red_turi)

    def windowclientopen(self):
        self.new_window1 = QtWidgets.QDialog()
        self.ui_window1 = Ui_DialogClient()
        self.ui_window1.setupUi(self.new_window1)
        self.new_window1.show()
        self.ui_window1.pushButton.clicked.connect(self.red_client)
    def red_client(self):
        name = self.ui_window1.lineEditName.text()
        surename = self.ui_window1.lineEditSurname.text()

        date=self.ui_window1.dateEdit.date()
        formatted_date = date.toString("yyyy-MM-dd")
        pasport = self.ui_window1.lineEditPasport.text()
        phone = self.ui_window1.lineEditPhone.text()
        email = self.ui_window1.lineEditEmail.text()
        id = self.ui_window1.lineEditDelIDCl.text()
        if id=="":
            self.new_window1.close()
        else:
            queryins = f"DELETE FROM Client WHERE ID_Client = {id}"
            self.cursor.execute(queryins)
            self.cursor.commit()
            self.new_window1.close()
        if name=="" and surename =="" and pasport=="" and phone=="" and email=="":
            self.new_window1.close()
        else:
            queryins2 = f"""
            INSERT INTO Client (Name, Surname, Birthday, Pasport, Phone, Email)
            VALUES 
            ('{name}', '{surename}', '{formatted_date}', '{pasport}', '{phone}', '{email}')
            """
            self.cursor.execute(queryins2)
            self.cursor.commit()
            self.new_window1.close()










    def red_turi(self):
        name = self.ui_window.lineEditNameTur.text()
        typetransport = self.ui_window.lineEditTypeTransp.text()
        categoryaccomd = self.ui_window.lineEditCatgaoryAccomd.text()
        id = self.ui_window.lineEditDelID.text()


        if name=="" and typetransport=="" and categoryaccomd=="":
            self.new_window.close()
        else:
            query = f"""
                        INSERT INTO Turi (Name_Tur, Type_transport, Accommodation_category)
                        VALUES
                        ('{name}', '{typetransport}', '{categoryaccomd}')
                    """
            self.cursor.execute(query)
            self.cursor.commit()
            self.new_window.close()
        if id=="":
            self.new_window.close()
        else:
            query1 = f"DELETE FROM Turi WHERE ID_tur = {id}"
            self.cursor.execute(query1)
            self.cursor.commit()
            self.new_window.close()










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
    window = SqlTreaker()
    window.show()

    sys.exit(app.exec())
