# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qadd_admin(object):
    def setupUi(self, Qadd_admin):
        Qadd_admin.setObjectName("Qadd_admin")
        Qadd_admin.resize(490, 219)
        self.name_cinema_wr_9 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_9.setGeometry(QtCore.QRect(260, 50, 111, 21))
        self.name_cinema_wr_9.setObjectName("name_cinema_wr_9")
        self.name_cinema_wr_8 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_8.setGeometry(QtCore.QRect(260, 80, 111, 21))
        self.name_cinema_wr_8.setObjectName("name_cinema_wr_8")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(0, 110, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")
        self.familyname = QtWidgets.QLineEdit(Qadd_admin)
        self.familyname.setGeometry(QtCore.QRect(120, 50, 131, 20))
        self.familyname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.familyname.setObjectName("familyname")
        self.fathername = QtWidgets.QLineEdit(Qadd_admin)
        self.fathername.setGeometry(QtCore.QRect(120, 110, 131, 20))
        self.fathername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fathername.setObjectName("fathername")
        self.name_cinema_wr = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr.setGeometry(QtCore.QRect(0, 50, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(0, 80, 81, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.textBrowser = QtWidgets.QTextBrowser(Qadd_admin)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 511, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.name_cinema_wr_5 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_5.setGeometry(QtCore.QRect(0, 150, 81, 21))
        self.name_cinema_wr_5.setObjectName("name_cinema_wr_5")
        self.number = QtWidgets.QLineEdit(Qadd_admin)
        self.number.setGeometry(QtCore.QRect(120, 180, 131, 20))
        self.number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number.setObjectName("number")
        self.name = QtWidgets.QLineEdit(Qadd_admin)
        self.name.setGeometry(QtCore.QRect(120, 80, 131, 20))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.name_cinema_wr_6 = QtWidgets.QLabel(Qadd_admin)
        self.name_cinema_wr_6.setGeometry(QtCore.QRect(0, 180, 91, 21))
        self.name_cinema_wr_6.setObjectName("name_cinema_wr_6")
        self.btnadd_hostel = QtWidgets.QPushButton(Qadd_admin)
        self.btnadd_hostel.setGeometry(QtCore.QRect(390, 180, 81, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.Hotels = QtWidgets.QComboBox(Qadd_admin)
        self.Hotels.setGeometry(QtCore.QRect(120, 140, 131, 31))
        self.Hotels.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Hotels.setObjectName("Hotels")
        self.login = QtWidgets.QLineEdit(Qadd_admin)
        self.login.setGeometry(QtCore.QRect(350, 50, 131, 20))
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(Qadd_admin)
        self.password.setGeometry(QtCore.QRect(350, 80, 131, 20))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setObjectName("password")

        self.retranslateUi(Qadd_admin)
        QtCore.QMetaObject.connectSlotsByName(Qadd_admin)

    def retranslateUi(self, Qadd_admin):
        _translate = QtCore.QCoreApplication.translate
        Qadd_admin.setWindowTitle(_translate("Qadd_admin", "Form"))
        self.name_cinema_wr_9.setText(_translate("Qadd_admin", "Login"))
        self.name_cinema_wr_8.setText(_translate("Qadd_admin", "Password"))
        self.name_cinema_wr_3.setText(_translate("Qadd_admin", "Отчество"))
        self.name_cinema_wr.setText(_translate("Qadd_admin", "Фамилия"))
        self.name_cinema_wr_2.setText(_translate("Qadd_admin", "Имя"))
        self.textBrowser.setHtml(_translate("Qadd_admin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добавление администратора</p></body></html>"))
        self.name_cinema_wr_5.setText(_translate("Qadd_admin", "Гостиница"))
        self.name_cinema_wr_6.setText(_translate("Qadd_admin", "Номер телефона"))
        self.btnadd_hostel.setText(_translate("Qadd_admin", "Заселить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qadd_admin = QtWidgets.QWidget()
    ui = Ui_Qadd_admin()
    ui.setupUi(Qadd_admin)
    Qadd_admin.show()
    sys.exit(app.exec_())

