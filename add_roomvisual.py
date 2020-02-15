# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_room.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 155)
        self.btnadd_hostel = QtWidgets.QPushButton(Form)
        self.btnadd_hostel.setGeometry(QtCore.QRect(270, 120, 61, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.country = QtWidgets.QLineEdit(Form)
        self.country.setGeometry(QtCore.QRect(130, 120, 131, 20))
        self.country.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.country.setObjectName("country")
        self.nroom = QtWidgets.QLineEdit(Form)
        self.nroom.setGeometry(QtCore.QRect(130, 70, 131, 20))
        self.nroom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nroom.setObjectName("nroom")
        self.nlevel = QtWidgets.QLineEdit(Form)
        self.nlevel.setGeometry(QtCore.QRect(130, 40, 131, 20))
        self.nlevel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nlevel.setObjectName("nlevel")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr = QtWidgets.QLabel(Form)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(10, 120, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnadd_hostel.setText(_translate("Form", "Готово"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Добавление комнаты</span></p></body></html>"))
        self.name_cinema_wr_2.setText(_translate("Form", "Кол-во комнат"))
        self.name_cinema_wr.setText(_translate("Form", "Номер комнаты"))
        self.name_cinema_wr_3.setText(_translate("Form", "Площадь"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

