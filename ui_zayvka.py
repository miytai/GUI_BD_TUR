# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateZap.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 450)
        Dialog.setMinimumSize(QSize(400, 450))
        Dialog.setMaximumSize(QSize(400, 450))
        Dialog.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 300, 241, 41))
        self.pushButton.setStyleSheet(u"font: 300 11pt \"Roboto\";")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 0, 311, 201))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 210, 311, 81))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 10, 181, 21))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 220, 181, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditDelID = QLineEdit(Dialog)
        self.lineEditDelID.setObjectName(u"lineEditDelID")
        self.lineEditDelID.setGeometry(QRect(80, 250, 251, 21))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 250, 21, 21))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.lineEditNameTur = QLineEdit(Dialog)
        self.lineEditNameTur.setObjectName(u"lineEditNameTur")
        self.lineEditNameTur.setGeometry(QRect(70, 60, 251, 21))
        self.lineEditTypeTransp = QLineEdit(Dialog)
        self.lineEditTypeTransp.setObjectName(u"lineEditTypeTransp")
        self.lineEditTypeTransp.setGeometry(QRect(70, 110, 251, 21))
        self.lineEditCatgaoryAccomd = QLineEdit(Dialog)
        self.lineEditCatgaoryAccomd.setObjectName(u"lineEditCatgaoryAccomd")
        self.lineEditCatgaoryAccomd.setGeometry(QRect(70, 160, 251, 21))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 30, 121, 31))
        font2 = QFont()
        font2.setFamilies([u"Roboto 54"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 80, 121, 31))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 130, 141, 31))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0422\u0443\u0440\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0422\u0443\u0440\u0430", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043d\u0430 \u043d\u043e\u0447\u044c", None))
    # retranslateUi

