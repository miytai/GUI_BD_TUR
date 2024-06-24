# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typered.ui'
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

class Ui_typeroom(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 515)
        Dialog.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 410, 21, 24))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(10)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(120, 40, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 10, 311, 301))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 10, 181, 31))
        font2 = QFont()
        font2.setFamilies([u"Roboto 54"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 460, 241, 41))
        self.pushButton.setStyleSheet(u"font: 300 11pt \"Roboto\";")
        self.lineEditNameRoom = QLineEdit(Dialog)
        self.lineEditNameRoom.setObjectName(u"lineEditNameRoom")
        self.lineEditNameRoom.setGeometry(QRect(70, 70, 251, 24))
        self.lineEditDelIDtyperoom = QLineEdit(Dialog)
        self.lineEditDelIDtyperoom.setObjectName(u"lineEditDelIDtyperoom")
        self.lineEditDelIDtyperoom.setGeometry(QRect(80, 410, 251, 24))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 380, 181, 24))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 370, 311, 81))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 90, 81, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.comboBoxCAt = QComboBox(Dialog)
        self.comboBoxCAt.addItem("")
        self.comboBoxCAt.addItem("")
        self.comboBoxCAt.addItem("")
        self.comboBoxCAt.addItem("")
        self.comboBoxCAt.setObjectName(u"comboBoxCAt")
        self.comboBoxCAt.setGeometry(QRect(70, 120, 251, 22))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 140, 111, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditIdpans = QLineEdit(Dialog)
        self.lineEditIdpans.setObjectName(u"lineEditIdpans")
        self.lineEditIdpans.setGeometry(QRect(70, 170, 251, 24))
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 190, 151, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditzilysl = QLineEdit(Dialog)
        self.lineEditzilysl.setObjectName(u"lineEditzilysl")
        self.lineEditzilysl.setGeometry(QRect(70, 220, 251, 24))
        self.lineEditcost = QLineEdit(Dialog)
        self.lineEditcost.setObjectName(u"lineEditcost")
        self.lineEditcost.setGeometry(QRect(70, 270, 251, 24))
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(160, 240, 151, 31))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.lineEditNameRoom.raise_()
        self.lineEditDelIDtyperoom.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.comboBoxCAt.raise_()
        self.label_11.raise_()
        self.lineEditIdpans.raise_()
        self.label_12.raise_()
        self.lineEditzilysl.raise_()
        self.lineEditcost.raise_()
        self.label_13.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0422\u0438\u043f\u044b \u043a\u043e\u043c\u043d\u0430\u0442", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043d\u0430\u0442\u044b", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_5.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.comboBoxCAt.setItemText(0, QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442", None))
        self.comboBoxCAt.setItemText(1, QCoreApplication.translate("Dialog", u"\u041b\u044e\u043a\u0441", None))
        self.comboBoxCAt.setItemText(2, QCoreApplication.translate("Dialog", u"\u0412\u0438\u043f", None))
        self.comboBoxCAt.setItemText(3, QCoreApplication.translate("Dialog", u"\u0411\u0438\u0437\u043d\u0435\u0441", None))

        self.label_11.setText(QCoreApplication.translate("Dialog", u"ID \u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u0430", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0416\u0438\u043b\u0438\u0449\u043d\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
    # retranslateUi

