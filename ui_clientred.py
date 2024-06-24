# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientRed.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DialogClient(object):
    def setupUi(self, DialogClient):
        if not DialogClient.objectName():
            DialogClient.setObjectName(u"DialogClient")
        DialogClient.resize(400, 600)
        DialogClient.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.label_6 = QLabel(DialogClient)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 10, 181, 31))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_4 = QLabel(DialogClient)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 10, 311, 351))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.lineEditName = QLineEdit(DialogClient)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setGeometry(QRect(80, 70, 251, 24))
        self.lineEditSurname = QLineEdit(DialogClient)
        self.lineEditSurname.setObjectName(u"lineEditSurname")
        self.lineEditSurname.setGeometry(QRect(80, 120, 251, 24))
        self.label_9 = QLabel(DialogClient)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 40, 41, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_8 = QLabel(DialogClient)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 410, 21, 24))
        font2 = QFont()
        font2.setFamilies([u"Roboto 54"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.pushButton = QPushButton(DialogClient)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 460, 241, 41))
        self.pushButton.setStyleSheet(u"font: 300 11pt \"Roboto\";")
        self.lineEditDelIDCl = QLineEdit(DialogClient)
        self.lineEditDelIDCl.setObjectName(u"lineEditDelIDCl")
        self.lineEditDelIDCl.setGeometry(QRect(90, 410, 251, 24))
        self.label_7 = QLabel(DialogClient)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 380, 181, 24))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_5 = QLabel(DialogClient)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 370, 311, 81))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_10 = QLabel(DialogClient)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 90, 121, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_11 = QLabel(DialogClient)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 140, 121, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_12 = QLabel(DialogClient)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(170, 190, 61, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditPhone = QLineEdit(DialogClient)
        self.lineEditPhone.setObjectName(u"lineEditPhone")
        self.lineEditPhone.setGeometry(QRect(80, 270, 251, 24))
        self.label_13 = QLabel(DialogClient)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(170, 240, 71, 31))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditPasport = QLineEdit(DialogClient)
        self.lineEditPasport.setObjectName(u"lineEditPasport")
        self.lineEditPasport.setGeometry(QRect(80, 220, 251, 24))
        self.lineEditEmail = QLineEdit(DialogClient)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setGeometry(QRect(80, 320, 251, 24))
        self.label_14 = QLabel(DialogClient)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(180, 290, 41, 31))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.dateEdit = QDateEdit(DialogClient)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(80, 170, 251, 22))
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lineEditName.raise_()
        self.lineEditSurname.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
        self.lineEditDelIDCl.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEditPhone.raise_()
        self.label_13.raise_()
        self.lineEditPasport.raise_()
        self.lineEditEmail.raise_()
        self.label_14.raise_()
        self.dateEdit.raise_()

        self.retranslateUi(DialogClient)

        QMetaObject.connectSlotsByName(DialogClient)
    # setupUi

    def retranslateUi(self, DialogClient):
        DialogClient.setWindowTitle(QCoreApplication.translate("DialogClient", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("DialogClient", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_4.setText("")
        self.label_9.setText(QCoreApplication.translate("DialogClient", u"\u0418\u043c\u044f", None))
        self.label_8.setText(QCoreApplication.translate("DialogClient", u"ID", None))
        self.pushButton.setText(QCoreApplication.translate("DialogClient", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("DialogClient", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_5.setText("")
        self.label_10.setText(QCoreApplication.translate("DialogClient", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("DialogClient", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_12.setText(QCoreApplication.translate("DialogClient", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442", None))
        self.label_13.setText(QCoreApplication.translate("DialogClient", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_14.setText(QCoreApplication.translate("DialogClient", u"Email", None))
    # retranslateUi

