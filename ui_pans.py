# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pansred.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_pansionat(object):
    def setupUi(self, pansionat):
        if not pansionat.objectName():
            pansionat.setObjectName(u"pansionat")
        pansionat.resize(400, 764)
        pansionat.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.pushButton = QPushButton(pansionat)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 710, 241, 41))
        self.pushButton.setStyleSheet(u"font: 300 11pt \"Roboto\";")
        self.label_9 = QLabel(pansionat)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 40, 171, 31))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(12)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_6 = QLabel(pansionat)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 10, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_7 = QLabel(pansionat)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 630, 181, 24))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditDelIDpans = QLineEdit(pansionat)
        self.lineEditDelIDpans.setObjectName(u"lineEditDelIDpans")
        self.lineEditDelIDpans.setGeometry(QRect(93, 660, 251, 24))
        self.label_8 = QLabel(pansionat)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 660, 21, 24))
        font2 = QFont()
        font2.setFamilies([u"Roboto 54"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_4 = QLabel(pansionat)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 10, 311, 561))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.lineEditNamePans = QLineEdit(pansionat)
        self.lineEditNamePans.setObjectName(u"lineEditNamePans")
        self.lineEditNamePans.setGeometry(QRect(80, 70, 251, 24))
        self.label_5 = QLabel(pansionat)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 620, 311, 81))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_10 = QLabel(pansionat)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 90, 51, 31))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditAdres = QLineEdit(pansionat)
        self.lineEditAdres.setObjectName(u"lineEditAdres")
        self.lineEditAdres.setGeometry(QRect(80, 120, 251, 24))
        self.lineEditCity = QLineEdit(pansionat)
        self.lineEditCity.setObjectName(u"lineEditCity")
        self.lineEditCity.setGeometry(QRect(80, 170, 251, 24))
        self.label_11 = QLabel(pansionat)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(170, 140, 61, 31))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditCountry = QLineEdit(pansionat)
        self.lineEditCountry.setObjectName(u"lineEditCountry")
        self.lineEditCountry.setGeometry(QRect(80, 220, 251, 24))
        self.label_12 = QLabel(pansionat)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(170, 190, 61, 31))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_13 = QLabel(pansionat)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 240, 161, 31))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditCountry_2 = QLineEdit(pansionat)
        self.lineEditCountry_2.setObjectName(u"lineEditCountry_2")
        self.lineEditCountry_2.setGeometry(QRect(80, 270, 251, 24))
        self.lineEditColvoRoom = QLineEdit(pansionat)
        self.lineEditColvoRoom.setObjectName(u"lineEditColvoRoom")
        self.lineEditColvoRoom.setGeometry(QRect(80, 320, 251, 24))
        self.label_14 = QLabel(pansionat)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 290, 161, 31))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_15 = QLabel(pansionat)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(160, 340, 161, 31))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.comboBoxBassein = QComboBox(pansionat)
        self.comboBoxBassein.addItem("")
        self.comboBoxBassein.addItem("")
        self.comboBoxBassein.setObjectName(u"comboBoxBassein")
        self.comboBoxBassein.setGeometry(QRect(80, 370, 251, 22))
        self.label_16 = QLabel(pansionat)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(160, 390, 161, 31))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.comboBoxSpaSalon = QComboBox(pansionat)
        self.comboBoxSpaSalon.addItem("")
        self.comboBoxSpaSalon.addItem("")
        self.comboBoxSpaSalon.setObjectName(u"comboBoxSpaSalon")
        self.comboBoxSpaSalon.setGeometry(QRect(80, 420, 251, 22))
        self.label_17 = QLabel(pansionat)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(160, 440, 161, 31))
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditColvoRoom_2 = QLineEdit(pansionat)
        self.lineEditColvoRoom_2.setObjectName(u"lineEditColvoRoom_2")
        self.lineEditColvoRoom_2.setGeometry(QRect(80, 470, 251, 24))
        self.lineEditDistofsea = QLineEdit(pansionat)
        self.lineEditDistofsea.setObjectName(u"lineEditDistofsea")
        self.lineEditDistofsea.setGeometry(QRect(80, 520, 251, 24))
        self.label_18 = QLabel(pansionat)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(140, 490, 161, 31))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_5.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEditDelIDpans.raise_()
        self.label_8.raise_()
        self.lineEditNamePans.raise_()
        self.label_10.raise_()
        self.lineEditAdres.raise_()
        self.lineEditCity.raise_()
        self.label_11.raise_()
        self.lineEditCountry.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.lineEditCountry_2.raise_()
        self.lineEditColvoRoom.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.comboBoxBassein.raise_()
        self.label_16.raise_()
        self.comboBoxSpaSalon.raise_()
        self.label_17.raise_()
        self.lineEditColvoRoom_2.raise_()
        self.lineEditDistofsea.raise_()
        self.label_18.raise_()

        self.retranslateUi(pansionat)

        QMetaObject.connectSlotsByName(pansionat)
    # setupUi

    def retranslateUi(self, pansionat):
        pansionat.setWindowTitle(QCoreApplication.translate("pansionat", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("pansionat", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("pansionat", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("pansionat", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_7.setText(QCoreApplication.translate("pansionat", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_8.setText(QCoreApplication.translate("pansionat", u"ID", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_10.setText(QCoreApplication.translate("pansionat", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.lineEditCity.setText("")
        self.label_11.setText(QCoreApplication.translate("pansionat", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.lineEditCountry.setText("")
        self.label_12.setText(QCoreApplication.translate("pansionat", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.label_13.setText(QCoreApplication.translate("pansionat", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u0438", None))
        self.lineEditCountry_2.setText("")
        self.lineEditColvoRoom.setText("")
        self.label_14.setText(QCoreApplication.translate("pansionat", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043d\u0430\u0442", None))
        self.label_15.setText(QCoreApplication.translate("pansionat", u"\u0411\u0430\u0441\u0441\u0435\u0439\u043d", None))
        self.comboBoxBassein.setItemText(0, QCoreApplication.translate("pansionat", u"\u0415\u0441\u0442\u044c", None))
        self.comboBoxBassein.setItemText(1, QCoreApplication.translate("pansionat", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0432\u0443\u0435\u0442", None))

        self.label_16.setText(QCoreApplication.translate("pansionat", u"\u0421\u043f\u0430-\u0421\u0430\u043b\u043e\u043d", None))
        self.comboBoxSpaSalon.setItemText(0, QCoreApplication.translate("pansionat", u"\u0415\u0441\u0442\u044c", None))
        self.comboBoxSpaSalon.setItemText(1, QCoreApplication.translate("pansionat", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0432\u0443\u0435\u0442", None))

        self.label_17.setText(QCoreApplication.translate("pansionat", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.lineEditColvoRoom_2.setText("")
        self.lineEditDistofsea.setText("")
        self.label_18.setText(QCoreApplication.translate("pansionat", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u044f \u0434\u043e \u043c\u043e\u0440\u044f", None))
    # retranslateUi

