# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_hostel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 241)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.nlevel = QtWidgets.QLineEdit(Form)
        self.nlevel.setGeometry(QtCore.QRect(100, 40, 131, 20))
        self.nlevel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nlevel.setObjectName("nlevel")
        self.nroom = QtWidgets.QLineEdit(Form)
        self.nroom.setGeometry(QtCore.QRect(100, 70, 131, 20))
        self.nroom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nroom.setObjectName("nroom")
        self.country = QtWidgets.QLineEdit(Form)
        self.country.setGeometry(QtCore.QRect(100, 120, 131, 20))
        self.country.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.country.setObjectName("country")
        self.city = QtWidgets.QLineEdit(Form)
        self.city.setGeometry(QtCore.QRect(100, 150, 131, 20))
        self.city.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.city.setObjectName("city")
        self.sreet = QtWidgets.QLineEdit(Form)
        self.sreet.setGeometry(QtCore.QRect(100, 180, 131, 20))
        self.sreet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sreet.setObjectName("sreet")
        self.house = QtWidgets.QLineEdit(Form)
        self.house.setGeometry(QtCore.QRect(100, 210, 131, 20))
        self.house.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.house.setObjectName("house")
        self.name_cinema_wr = QtWidgets.QLabel(Form)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(30, 120, 51, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")
        self.name_cinema_wr_4 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_4.setGeometry(QtCore.QRect(30, 150, 51, 21))
        self.name_cinema_wr_4.setObjectName("name_cinema_wr_4")
        self.name_cinema_wr_5 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_5.setGeometry(QtCore.QRect(30, 180, 51, 21))
        self.name_cinema_wr_5.setObjectName("name_cinema_wr_5")
        self.name_cinema_wr_6 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_6.setGeometry(QtCore.QRect(30, 210, 51, 21))
        self.name_cinema_wr_6.setObjectName("name_cinema_wr_6")
        self.adm_login = QtWidgets.QLineEdit(Form)
        self.adm_login.setGeometry(QtCore.QRect(330, 70, 131, 20))
        self.adm_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adm_login.setObjectName("adm_login")
        self.name_cinema_wr_9 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_9.setGeometry(QtCore.QRect(260, 100, 51, 21))
        self.name_cinema_wr_9.setObjectName("name_cinema_wr_9")
        self.name_cinema_wr_8 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_8.setGeometry(QtCore.QRect(260, 70, 51, 21))
        self.name_cinema_wr_8.setObjectName("name_cinema_wr_8")
        self.name_cinema_wr_7 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_7.setGeometry(QtCore.QRect(260, 40, 201, 21))
        self.name_cinema_wr_7.setObjectName("name_cinema_wr_7")
        self.adm_password = QtWidgets.QLineEdit(Form)
        self.adm_password.setGeometry(QtCore.QRect(330, 100, 131, 20))
        self.adm_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adm_password.setObjectName("adm_password")
        self.btnadd_hostel = QtWidgets.QPushButton(Form)
        self.btnadd_hostel.setGeometry(QtCore.QRect(390, 210, 81, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добавление гостиницы</p></body></html>"))
        self.name_cinema_wr.setText(_translate("Form", "Кол-во этажей"))
        self.name_cinema_wr_2.setText(_translate("Form", "Кол-во комнат"))
        self.name_cinema_wr_3.setText(_translate("Form", "Страна"))
        self.name_cinema_wr_4.setText(_translate("Form", "Город"))
        self.name_cinema_wr_5.setText(_translate("Form", "Улица"))
        self.name_cinema_wr_6.setText(_translate("Form", "Дом"))
        self.name_cinema_wr_9.setText(_translate("Form", "password"))
        self.name_cinema_wr_8.setText(_translate("Form", "login"))
        self.name_cinema_wr_7.setText(_translate("Form", "Добавление Администратора"))
        self.btnadd_hostel.setText(_translate("Form", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

