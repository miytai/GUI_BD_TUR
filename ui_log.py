# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uibased2.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 569)
        MainWindow.setMinimumSize(QSize(800, 569))
        MainWindow.setMaximumSize(QSize(800, 569))
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
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 261, 201))
        self.label_2.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(340, 50, 391, 21))
        self.comboBox_2.setStyleSheet(u"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 20, 81, 31))
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
        self.label_4.setGeometry(QRect(10, 240, 781, 321))
        self.label_4.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 250, 761, 301))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 60, 221, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 90, 221, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 120, 221, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 150, 221, 24))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 180, 221, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 20, 411, 71))
        self.label_5.setStyleSheet(u"backhround-color: None;\n"
"border: 5px;\n"
"border-radius: 15px;\n"
"opacity: .3;\n"
"background-color:rgba(196, 196,176 , .5);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_5.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ZRUD", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.label_2.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441...", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u043a\u043e\u043c\u043d\u0430\u0442", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u043f\u043e \u0446\u0435\u043d\u0435 \u043a\u043e\u043c\u043d\u0430\u0442", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u0422\u0443\u0440\u0430 \u043f\u043e \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u0430 \u043f\u043e \u0433\u043e\u0440\u043e\u0434\u0443 \u0411\u0430\u0440\u043d\u0430\u0443\u043b \u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u044e \u0431\u0430\u0441\u0441\u0435\u0439\u043d\u0430", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430 \u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u0430 \u043f\u043e \u0413\u043e\u0440\u043e\u0434\u0443 \u0410\u043d\u0430\u043f\u0430 \u0438\u043b\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u044e \u0441\u043f\u0430-\u0441\u0430\u043b\u043e\u043d\u0430", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u0430\u0442\u043e\u0432\u043e \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u0434\u0432\u0443\u0445 \u0442\u0430\u0431\u043b\u0438\u0446", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446 \u043f\u043e \u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0443 1", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446 \u043f\u043e \u0440\u0430\u0432\u0435\u043d\u0441\u0442\u0432\u0443 2", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Right join", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Left join", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0446\u0435\u043d\u044b", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u0441\u0442\u043e\u043b\u0431\u0446\u0443", None))

#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u044b", None))
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \"\u0422\u0443\u0440\u044b\"", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \"\u041f\u0430\u043d\u0441\u0438\u043e\u043d\u0430\u0442\u044b\"", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \"\u041a\u043b\u0438\u0435\u043d\u0442\u044b\"", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \"\u0422\u0438\u043f\u044b \u043a\u043e\u043c\u043d\u0430\u0442\"", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \"\u041f\u0443\u0442\u0435\u0432\u043a\u0438\"", None))
        self.label_5.setText("")
    # retranslateUi

