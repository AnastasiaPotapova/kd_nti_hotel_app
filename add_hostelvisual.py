# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_hostel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qadd_hostel(object):
    def setupUi(self, Qadd_hostel):
        Qadd_hostel.setObjectName("Qadd_hostel")
        Qadd_hostel.resize(331, 260)
        self.house = QtWidgets.QLineEdit(Qadd_hostel)
        self.house.setGeometry(QtCore.QRect(120, 230, 131, 20))
        self.house.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.house.setObjectName("house")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(0, 70, 111, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr_5 = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr_5.setGeometry(QtCore.QRect(30, 200, 51, 21))
        self.name_cinema_wr_5.setObjectName("name_cinema_wr_5")
        self.nroom = QtWidgets.QLineEdit(Qadd_hostel)
        self.nroom.setGeometry(QtCore.QRect(120, 70, 131, 20))
        self.nroom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nroom.setObjectName("nroom")
        self.nlevel = QtWidgets.QLineEdit(Qadd_hostel)
        self.nlevel.setGeometry(QtCore.QRect(120, 40, 131, 20))
        self.nlevel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nlevel.setObjectName("nlevel")
        self.sreet = QtWidgets.QLineEdit(Qadd_hostel)
        self.sreet.setGeometry(QtCore.QRect(120, 200, 131, 20))
        self.sreet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sreet.setObjectName("sreet")
        self.name_cinema_wr = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr.setGeometry(QtCore.QRect(0, 40, 111, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.city = QtWidgets.QLineEdit(Qadd_hostel)
        self.city.setGeometry(QtCore.QRect(120, 170, 131, 20))
        self.city.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.city.setObjectName("city")
        self.btnadd_hostel = QtWidgets.QPushButton(Qadd_hostel)
        self.btnadd_hostel.setGeometry(QtCore.QRect(260, 230, 61, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(30, 140, 51, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")
        self.country = QtWidgets.QLineEdit(Qadd_hostel)
        self.country.setGeometry(QtCore.QRect(120, 140, 131, 20))
        self.country.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.country.setObjectName("country")
        self.name_cinema_wr_6 = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr_6.setGeometry(QtCore.QRect(30, 230, 51, 21))
        self.name_cinema_wr_6.setObjectName("name_cinema_wr_6")
        self.title = QtWidgets.QTextBrowser(Qadd_hostel)
        self.title.setGeometry(QtCore.QRect(0, 10, 311, 31))
        self.title.setStyleSheet("background-color: transparent;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setObjectName("title")
        self.name_cinema_wr_4 = QtWidgets.QLabel(Qadd_hostel)
        self.name_cinema_wr_4.setGeometry(QtCore.QRect(30, 170, 51, 21))
        self.name_cinema_wr_4.setObjectName("name_cinema_wr_4")
        self.status = QtWidgets.QTextBrowser(Qadd_hostel)
        self.status.setGeometry(QtCore.QRect(30, 100, 181, 31))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")

        self.retranslateUi(Qadd_hostel)
        QtCore.QMetaObject.connectSlotsByName(Qadd_hostel)

    def retranslateUi(self, Qadd_hostel):
        _translate = QtCore.QCoreApplication.translate
        Qadd_hostel.setWindowTitle(_translate("Qadd_hostel", "Form"))
        self.name_cinema_wr_2.setText(_translate("Qadd_hostel", "Кол-во комнат"))
        self.name_cinema_wr_5.setText(_translate("Qadd_hostel", "Улица"))
        self.name_cinema_wr.setText(_translate("Qadd_hostel", "Кол-во этажей"))
        self.btnadd_hostel.setText(_translate("Qadd_hostel", "Готово"))
        self.name_cinema_wr_3.setText(_translate("Qadd_hostel", "Страна"))
        self.name_cinema_wr_6.setText(_translate("Qadd_hostel", "Дом"))
        self.title.setHtml(_translate("Qadd_hostel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.name_cinema_wr_4.setText(_translate("Qadd_hostel", "Город"))
        self.status.setHtml(_translate("Qadd_hostel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qadd_hostel = QtWidgets.QWidget()
    ui = Ui_Qadd_hostel()
    ui.setupUi(Qadd_hostel)
    Qadd_hostel.show()
    sys.exit(app.exec_())

