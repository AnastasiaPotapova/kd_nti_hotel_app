# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_room.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qadd_room(object):
    def setupUi(self, Qadd_room):
        Qadd_room.setObjectName("Qadd_room")
        Qadd_room.resize(339, 162)
        self.btnadd_hostel = QtWidgets.QPushButton(Qadd_room)
        self.btnadd_hostel.setGeometry(QtCore.QRect(270, 130, 61, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.title = QtWidgets.QTextBrowser(Qadd_room)
        self.title.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.title.setStyleSheet("background-color: transparent;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setObjectName("title")
        self.country = QtWidgets.QLineEdit(Qadd_room)
        self.country.setGeometry(QtCore.QRect(130, 130, 131, 20))
        self.country.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.country.setObjectName("country")
        self.nroom = QtWidgets.QLineEdit(Qadd_room)
        self.nroom.setGeometry(QtCore.QRect(130, 70, 131, 20))
        self.nroom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nroom.setObjectName("nroom")
        self.nlevel = QtWidgets.QLineEdit(Qadd_room)
        self.nlevel.setGeometry(QtCore.QRect(130, 40, 131, 20))
        self.nlevel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nlevel.setObjectName("nlevel")
        self.name_cinema_wr_2 = QtWidgets.QLabel(Qadd_room)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.name_cinema_wr = QtWidgets.QLabel(Qadd_room)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name_cinema_wr_3 = QtWidgets.QLabel(Qadd_room)
        self.name_cinema_wr_3.setGeometry(QtCore.QRect(10, 130, 81, 21))
        self.name_cinema_wr_3.setObjectName("name_cinema_wr_3")
        self.status = QtWidgets.QTextBrowser(Qadd_room)
        self.status.setGeometry(QtCore.QRect(40, 100, 181, 31))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")

        self.retranslateUi(Qadd_room)
        QtCore.QMetaObject.connectSlotsByName(Qadd_room)

    def retranslateUi(self, Qadd_room):
        _translate = QtCore.QCoreApplication.translate
        Qadd_room.setWindowTitle(_translate("Qadd_room", "Form"))
        self.btnadd_hostel.setText(_translate("Qadd_room", "Готово"))
        self.title.setHtml(_translate("Qadd_room", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Добавление комнаты</span></p></body></html>"))
        self.name_cinema_wr_2.setText(_translate("Qadd_room", "Кол-во комнат"))
        self.name_cinema_wr.setText(_translate("Qadd_room", "Номер комнаты"))
        self.name_cinema_wr_3.setText(_translate("Qadd_room", "Площадь"))
        self.status.setHtml(_translate("Qadd_room", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qadd_room = QtWidgets.QWidget()
    ui = Ui_Qadd_room()
    ui.setupUi(Qadd_room)
    Qadd_room.show()
    sys.exit(app.exec_())

