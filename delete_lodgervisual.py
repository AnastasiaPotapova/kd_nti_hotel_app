# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_lodger.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qdelete_lodger(object):
    def setupUi(self, Qdelete_lodger):
        Qdelete_lodger.setObjectName("Qdelete_lodger")
        Qdelete_lodger.resize(532, 148)
        self.textBrowser = QtWidgets.QTextBrowser(Qdelete_lodger)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 511, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Qdelete_lodger)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr_9 = QtWidgets.QLabel(Qdelete_lodger)
        self.name_cinema_wr_9.setGeometry(QtCore.QRect(270, 50, 111, 21))
        self.name_cinema_wr_9.setObjectName("name_cinema_wr_9")
        self.fathername = QtWidgets.QLineEdit(Qdelete_lodger)
        self.fathername.setGeometry(QtCore.QRect(130, 110, 131, 20))
        self.fathername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fathername.setObjectName("fathername")
        self.familyname = QtWidgets.QLineEdit(Qdelete_lodger)
        self.familyname.setGeometry(QtCore.QRect(130, 50, 131, 20))
        self.familyname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.familyname.setObjectName("familyname")
        self.name_cinema_wr = QtWidgets.QLabel(Qdelete_lodger)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name = QtWidgets.QLineEdit(Qdelete_lodger)
        self.name.setGeometry(QtCore.QRect(130, 80, 131, 20))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name.setObjectName("name")
        self.date = QtWidgets.QDateEdit(Qdelete_lodger)
        self.date.setGeometry(QtCore.QRect(390, 50, 131, 22))
        self.date.setObjectName("date")
        self.btnadd_hostel = QtWidgets.QPushButton(Qdelete_lodger)
        self.btnadd_hostel.setGeometry(QtCore.QRect(440, 110, 81, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Qdelete_lodger)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")

        self.retranslateUi(Qdelete_lodger)
        QtCore.QMetaObject.connectSlotsByName(Qdelete_lodger)

    def retranslateUi(self, Qdelete_lodger):
        _translate = QtCore.QCoreApplication.translate
        Qdelete_lodger.setWindowTitle(_translate("Qdelete_lodger", "Form"))
        self.textBrowser.setHtml(_translate("Qdelete_lodger", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Выселение постояльца</span></p></body></html>"))
        self.name_cinema_wr_2.setText(_translate("Qdelete_lodger", "Имя"))
        self.name_cinema_wr_9.setText(_translate("Qdelete_lodger", "Дата выселения"))
        self.name_cinema_wr.setText(_translate("Qdelete_lodger", "Фамилия"))
        self.btnadd_hostel.setText(_translate("Qdelete_lodger", "Выселить"))
        self.name_cinema_wr_3.setText(_translate("Qdelete_lodger", "Отчество"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qdelete_lodger = QtWidgets.QWidget()
    ui = Ui_Qdelete_lodger()
    ui.setupUi(Qdelete_lodger)
    Qdelete_lodger.show()
    sys.exit(app.exec_())

