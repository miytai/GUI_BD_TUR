# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIBased1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"font-family: Roboto Light;\n"
"background-color:  #F5F5DC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 30, 81, 21))
        font = QFont()
        font.setFamilies([u"Roboto 54"])
        font.setPointSize(15)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;\n"
"")
        self.comboBoxTable = QComboBox(self.centralwidget)
        self.comboBoxTable.addItem("")
        self.comboBoxTable.addItem("")
        self.comboBoxTable.addItem("")
        self.comboBoxTable.addItem("")
        self.comboBoxTable.addItem("")
        self.comboBoxTable.setObjectName(u"comboBoxTable")
        self.comboBoxTable.setGeometry(QRect(30, 60, 221, 22))
        self.comboBoxTable.setAutoFillBackground(False)
        self.comboBoxTable.setStyleSheet(u"font-family: Roboto Light")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 261, 141))
        self.label_2.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 120, 221, 21))
        self.comboBox_2.setStyleSheet(u"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 80, 81, 41))
        font1 = QFont()
        font1.setFamilies([u"Roboto 54"])
        font1.setPointSize(15)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color:None;\n"
"color: #4c4c45;\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 781, 391))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 180, 761, 371))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.comboBoxTable.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZRUD", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.comboBoxTable.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.comboBoxTable.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u044b", None))
        self.comboBoxTable.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.comboBoxTable.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u0435\u0432\u043a\u0438", None))
        self.comboBoxTable.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u041a\u043e\u043c\u043d\u0430\u0442", None))

        self.comboBoxTable.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.label_2.setText("")
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u044b", None))
        self.label_4.setText("")
    # retranslateUi

