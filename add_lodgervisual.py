# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_lodger.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qadd_lodger(object):
    def setupUi(self, Qadd_lodger):
        Qadd_lodger.setObjectName("Qadd_lodger")
        Qadd_lodger.resize(391, 283)
        self.title = QtWidgets.QTextBrowser(Qadd_lodger)
        self.title.setGeometry(QtCore.QRect(10, 10, 511, 31))
        self.title.setStyleSheet("background-color: transparent;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setObjectName("title")
        self.familyname = QtWidgets.QLineEdit(Qadd_lodger)
        self.familyname.setGeometry(QtCore.QRect(130, 50, 131, 20))
        self.familyname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.familyname.setObjectName("familyname")
        self.number = QtWidgets.QLineEdit(Qadd_lodger)
        self.number.setGeometry(QtCore.QRect(130, 220, 131, 20))
        self.number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number.setObjectName("number")
        self.name = QtWidgets.QLineEdit(Qadd_lodger)
        self.name.setGeometry(QtCore.QRect(130, 80, 131, 20))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.name_cinema_wr = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.sex = QtWidgets.QLineEdit(Qadd_lodger)
        self.sex.setGeometry(QtCore.QRect(130, 190, 131, 20))
        self.sex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sex.setObjectName("sex")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.birt = QtWidgets.QLineEdit(Qadd_lodger)
        self.birt.setGeometry(QtCore.QRect(130, 150, 131, 20))
        self.birt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.birt.setObjectName("birt")
        self.name_cinema_wr_4 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_4.setGeometry(QtCore.QRect(10, 150, 81, 21))
        self.name_cinema_wr_4.setObjectName("name_cinema_wr_4")
        self.name_cinema_wr_5 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_5.setGeometry(QtCore.QRect(10, 190, 81, 21))
        self.name_cinema_wr_5.setObjectName("name_cinema_wr_5")
        self.name_cinema_wr_6 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_6.setGeometry(QtCore.QRect(10, 220, 91, 21))
        self.name_cinema_wr_6.setObjectName("name_cinema_wr_6")
        self.fathername = QtWidgets.QLineEdit(Qadd_lodger)
        self.fathername.setGeometry(QtCore.QRect(130, 110, 131, 20))
        self.fathername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fathername.setObjectName("fathername")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")
        self.name_cinema_wr_7 = QtWidgets.QLabel(Qadd_lodger)
        self.name_cinema_wr_7.setGeometry(QtCore.QRect(10, 250, 111, 21))
        self.name_cinema_wr_7.setObjectName("name_cinema_wr_7")
        self.passport = QtWidgets.QLineEdit(Qadd_lodger)
        self.passport.setGeometry(QtCore.QRect(130, 250, 131, 20))
        self.passport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passport.setObjectName("passport")
        self.btnadd_hostel = QtWidgets.QPushButton(Qadd_lodger)
        self.btnadd_hostel.setGeometry(QtCore.QRect(270, 240, 111, 31))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.status = QtWidgets.QTextBrowser(Qadd_lodger)
        self.status.setGeometry(QtCore.QRect(280, 50, 101, 181))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")

        self.retranslateUi(Qadd_lodger)
        QtCore.QMetaObject.connectSlotsByName(Qadd_lodger)

    def retranslateUi(self, Qadd_lodger):
        _translate = QtCore.QCoreApplication.translate
        Qadd_lodger.setWindowTitle(_translate("Qadd_lodger", "Form"))
        self.title.setHtml(_translate("Qadd_lodger", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.name_cinema_wr.setText(_translate("Qadd_lodger", "Фамилия"))
        self.name_cinema_wr_2.setText(_translate("Qadd_lodger", "Имя"))
        self.name_cinema_wr_4.setText(_translate("Qadd_lodger", "Дата рождения"))
        self.name_cinema_wr_5.setText(_translate("Qadd_lodger", "Пол"))
        self.name_cinema_wr_6.setText(_translate("Qadd_lodger", "Номер телефона"))
        self.name_cinema_wr_3.setText(_translate("Qadd_lodger", "Отчество"))
        self.name_cinema_wr_7.setText(_translate("Qadd_lodger", "Пасспортные данные"))
        self.btnadd_hostel.setText(_translate("Qadd_lodger", "Добавление"))
        self.status.setHtml(_translate("Qadd_lodger", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qadd_lodger = QtWidgets.QWidget()
    ui = Ui_Qadd_lodger()
    ui.setupUi(Qadd_lodger)
    Qadd_lodger.show()
    sys.exit(app.exec_())

