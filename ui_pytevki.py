# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pytred.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_petevki(object):
    def setupUi(self, petevki):
        if not petevki.objectName():
            petevki.setObjectName(u"petevki")
        petevki.resize(400, 530)
        petevki.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.label_8 = QLabel(petevki)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 420, 21, 24))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(10)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditIDClient = QLineEdit(petevki)
        self.lineEditIDClient.setObjectName(u"lineEditIDClient")
        self.lineEditIDClient.setGeometry(QRect(70, 80, 251, 24))
        self.label_9 = QLabel(petevki)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 50, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_6 = QLabel(petevki)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 20, 181, 31))
        font2 = QFont()
        font2.setFamilies([u"Roboto 54"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_7 = QLabel(petevki)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 390, 181, 24))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_5 = QLabel(petevki)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 380, 311, 81))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.lineEditDelIDPt = QLineEdit(petevki)
        self.lineEditDelIDPt.setObjectName(u"lineEditDelIDPt")
        self.lineEditDelIDPt.setGeometry(QRect(80, 420, 251, 24))
        self.label_4 = QLabel(petevki)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 20, 311, 351))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.pushButton = QPushButton(petevki)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 470, 241, 41))
        self.pushButton.setStyleSheet(u"font: 300 11pt \"Roboto\";")
        self.label_10 = QLabel(petevki)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(160, 100, 101, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditIDTur = QLineEdit(petevki)
        self.lineEditIDTur.setObjectName(u"lineEditIDTur")
        self.lineEditIDTur.setGeometry(QRect(70, 130, 251, 24))
        self.dateEditstart = QDateEdit(petevki)
        self.dateEditstart.setObjectName(u"dateEditstart")
        self.dateEditstart.setGeometry(QRect(70, 180, 251, 22))
        self.label_11 = QLabel(petevki)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 150, 121, 31))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.dateEditend = QDateEdit(petevki)
        self.dateEditend.setObjectName(u"dateEditend")
        self.dateEditend.setGeometry(QRect(70, 230, 251, 22))
        self.label_12 = QLabel(petevki)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(140, 200, 121, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditCost = QLineEdit(petevki)
        self.lineEditCost.setObjectName(u"lineEditCost")
        self.lineEditCost.setGeometry(QRect(70, 280, 251, 24))
        self.label_13 = QLabel(petevki)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(170, 250, 101, 31))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_14 = QLabel(petevki)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 300, 101, 31))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.comboBoxStatus = QComboBox(petevki)
        self.comboBoxStatus.addItem("")
        self.comboBoxStatus.addItem("")
        self.comboBoxStatus.addItem("")
        self.comboBoxStatus.setObjectName(u"comboBoxStatus")
        self.comboBoxStatus.setGeometry(QRect(70, 330, 251, 22))
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.lineEditIDClient.raise_()
        self.label_9.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lineEditDelIDPt.raise_()
        self.pushButton.raise_()
        self.label_10.raise_()
        self.lineEditIDTur.raise_()
        self.dateEditstart.raise_()
        self.label_11.raise_()
        self.dateEditend.raise_()
        self.label_12.raise_()
        self.lineEditCost.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.comboBoxStatus.raise_()

        self.retranslateUi(petevki)

        QMetaObject.connectSlotsByName(petevki)
    # setupUi

    def retranslateUi(self, petevki):
        petevki.setWindowTitle(QCoreApplication.translate("petevki", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u041f\u0443\u0442\u0435\u0432\u043a\u0438", None))
        self.label_8.setText(QCoreApplication.translate("petevki", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("petevki", u"ID \u041a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("petevki", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_7.setText(QCoreApplication.translate("petevki", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_5.setText("")
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("petevki", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("petevki", u"ID \u0422\u0443\u0440\u0430", None))
        self.label_11.setText(QCoreApplication.translate("petevki", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_12.setText(QCoreApplication.translate("petevki", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.label_13.setText(QCoreApplication.translate("petevki", u"\u0426\u0435\u043d\u0430", None))
        self.label_14.setText(QCoreApplication.translate("petevki", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.comboBoxStatus.setItemText(0, QCoreApplication.translate("petevki", u"\u041e\u0442\u043c\u0435\u043d\u0435\u043d\u0430", None))
        self.comboBoxStatus.setItemText(1, QCoreApplication.translate("petevki", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u0430", None))
        self.comboBoxStatus.setItemText(2, QCoreApplication.translate("petevki", u"\u0417\u0430\u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0430", None))

    # retranslateUi

