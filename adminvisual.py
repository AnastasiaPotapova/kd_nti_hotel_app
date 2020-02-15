# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qadmin(object):
    def setupUi(self, Qadmin):
        Qadmin.setObjectName("Qadmin")
        Qadmin.resize(587, 209)
        self.textBrowser = QtWidgets.QTextBrowser(Qadmin)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 571, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.btnin_lodger = QtWidgets.QPushButton(Qadmin)
        self.btnin_lodger.setGeometry(QtCore.QRect(210, 60, 81, 23))
        self.btnin_lodger.setStyleSheet("")
        self.btnin_lodger.setObjectName("btnin_lodger")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Qadmin)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 40, 191, 21))
        self.textBrowser_3.setStyleSheet("background-color: transparent;")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.lodger_session = QtWidgets.QLabel(Qadmin)
        self.lodger_session.setGeometry(QtCore.QRect(10, 60, 191, 131))
        self.lodger_session.setMaximumSize(QtCore.QSize(271, 131))
        self.lodger_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lodger_session.setMouseTracking(True)
        self.lodger_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lodger_session.setFrameShape(QtWidgets.QFrame.Box)
        self.lodger_session.setText("")
        self.lodger_session.setObjectName("lodger_session")
        self.btnout_lodger = QtWidgets.QPushButton(Qadmin)
        self.btnout_lodger.setGeometry(QtCore.QRect(210, 90, 81, 23))
        self.btnout_lodger.setStyleSheet("")
        self.btnout_lodger.setObjectName("btnout_lodger")
        self.btnadd_lodger = QtWidgets.QPushButton(Qadmin)
        self.btnadd_lodger.setGeometry(QtCore.QRect(210, 140, 81, 23))
        self.btnadd_lodger.setStyleSheet("")
        self.btnadd_lodger.setObjectName("btnadd_lodger")
        self.btndelete_lodger = QtWidgets.QPushButton(Qadmin)
        self.btndelete_lodger.setGeometry(QtCore.QRect(210, 170, 81, 23))
        self.btndelete_lodger.setStyleSheet("")
        self.btndelete_lodger.setObjectName("btndelete_lodger")
        self.room_session = QtWidgets.QLabel(Qadmin)
        self.room_session.setGeometry(QtCore.QRect(300, 60, 191, 131))
        self.room_session.setMaximumSize(QtCore.QSize(271, 131))
        self.room_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.room_session.setMouseTracking(True)
        self.room_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.room_session.setFrameShape(QtWidgets.QFrame.Box)
        self.room_session.setText("")
        self.room_session.setObjectName("room_session")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Qadmin)
        self.textBrowser_4.setGeometry(QtCore.QRect(300, 40, 191, 21))
        self.textBrowser_4.setStyleSheet("background-color: transparent;")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.btnadd_room = QtWidgets.QPushButton(Qadmin)
        self.btnadd_room.setGeometry(QtCore.QRect(500, 170, 81, 23))
        self.btnadd_room.setStyleSheet("")
        self.btnadd_room.setObjectName("btnadd_room")
        self.btn_checkin = QtWidgets.QPushButton(Qadmin)
        self.btn_checkin.setGeometry(QtCore.QRect(500, 60, 81, 23))
        self.btn_checkin.setStyleSheet("")
        self.btn_checkin.setObjectName("btn_checkin")

        self.retranslateUi(Qadmin)
        QtCore.QMetaObject.connectSlotsByName(Qadmin)

    def retranslateUi(self, Qadmin):
        _translate = QtCore.QCoreApplication.translate
        Qadmin.setWindowTitle(_translate("Qadmin", "Form"))
        self.textBrowser.setHtml(_translate("Qadmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Администратор</span></p></body></html>"))
        self.btnin_lodger.setText(_translate("Qadmin", "Заселить"))
        self.textBrowser_3.setHtml(_translate("Qadmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Список постояльцев</span></p></body></html>"))
        self.btnout_lodger.setText(_translate("Qadmin", "Выселить"))
        self.btnadd_lodger.setText(_translate("Qadmin", "Добавить"))
        self.btndelete_lodger.setText(_translate("Qadmin", "Удалить"))
        self.textBrowser_4.setHtml(_translate("Qadmin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Список свободных номеров</span></p></body></html>"))
        self.btnadd_room.setText(_translate("Qadmin", "Добавить"))
        self.btn_checkin.setText(_translate("Qadmin", "ок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qadmin = QtWidgets.QWidget()
    ui = Ui_Qadmin()
    ui.setupUi(Qadmin)
    Qadmin.show()
    sys.exit(app.exec_())

