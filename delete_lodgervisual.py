# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_lodger.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 148)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 511, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr_9 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_9.setGeometry(QtCore.QRect(270, 50, 111, 21))
        self.name_cinema_wr_9.setObjectName("name_cinema_wr_9")
        self.fathername = QtWidgets.QLineEdit(Form)
        self.fathername.setGeometry(QtCore.QRect(130, 110, 131, 20))
        self.fathername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fathername.setObjectName("fathername")
        self.familyname = QtWidgets.QLineEdit(Form)
        self.familyname.setGeometry(QtCore.QRect(130, 50, 131, 20))
        self.familyname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.familyname.setObjectName("familyname")
        self.name_cinema_wr = QtWidgets.QLabel(Form)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(130, 80, 131, 20))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.date = QtWidgets.QDateEdit(Form)
        self.date.setGeometry(QtCore.QRect(390, 50, 131, 22))
        self.date.setObjectName("date")
        self.btnadd_hostel = QtWidgets.QPushButton(Form)
        self.btnadd_hostel.setGeometry(QtCore.QRect(440, 110, 81, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Form)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выселение постояльца</p></body></html>"))
        self.name_cinema_wr_2.setText(_translate("Form", "Имя"))
        self.name_cinema_wr_9.setText(_translate("Form", "Дата выселения"))
        self.name_cinema_wr.setText(_translate("Form", "Фамилия"))
        self.btnadd_hostel.setText(_translate("Form", "Выселить"))
        self.name_cinema_wr_3.setText(_translate("Form", "Отчество"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

