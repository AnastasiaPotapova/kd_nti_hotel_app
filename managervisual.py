# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qmanager(object):
    def setupUi(self, Qmanager):
        Qmanager.setObjectName("Qmanager")
        Qmanager.resize(534, 388)
        self.textBrowser = QtWidgets.QTextBrowser(Qmanager)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 461, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.btnadd_hostel = QtWidgets.QPushButton(Qmanager)
        self.btnadd_hostel.setGeometry(QtCore.QRect(400, 70, 131, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.hotel_session = QtWidgets.QLabel(Qmanager)
        self.hotel_session.setGeometry(QtCore.QRect(200, 70, 191, 131))
        self.hotel_session.setMaximumSize(QtCore.QSize(271, 131))
        self.hotel_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.hotel_session.setMouseTracking(True)
        self.hotel_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hotel_session.setFrameShape(QtWidgets.QFrame.Box)
        self.hotel_session.setText("")
        self.hotel_session.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hotel_session.setObjectName("hotel_session")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Qmanager)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 185, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.sorts = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.sorts.setContentsMargins(0, 0, 0, 0)
        self.sorts.setObjectName("sorts")
        self.adress_sort = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.adress_sort.setChecked(False)
        self.adress_sort.setObjectName("adress_sort")
        self.sorts.addWidget(self.adress_sort)
        self.nroom_sort = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.nroom_sort.setChecked(False)
        self.nroom_sort.setObjectName("nroom_sort")
        self.sorts.addWidget(self.nroom_sort)
        self.time = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.time.setChecked(False)
        self.time.setObjectName("time")
        self.sorts.addWidget(self.time)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Qmanager)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.textBrowser_2.setStyleSheet("background-color: transparent;")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Qmanager)
        self.textBrowser_3.setGeometry(QtCore.QRect(200, 40, 191, 31))
        self.textBrowser_3.setStyleSheet("background-color: transparent;")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.admin_session = QtWidgets.QLabel(Qmanager)
        self.admin_session.setGeometry(QtCore.QRect(200, 240, 191, 131))
        self.admin_session.setMaximumSize(QtCore.QSize(271, 131))
        self.admin_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.admin_session.setMouseTracking(True)
        self.admin_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_session.setFrameShape(QtWidgets.QFrame.Box)
        self.admin_session.setText("")
        self.admin_session.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.admin_session.setObjectName("admin_session")
        self.btnadd_admin = QtWidgets.QPushButton(Qmanager)
        self.btnadd_admin.setGeometry(QtCore.QRect(400, 240, 131, 23))
        self.btnadd_admin.setStyleSheet("")
        self.btnadd_admin.setObjectName("btnadd_admin")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Qmanager)
        self.textBrowser_4.setGeometry(QtCore.QRect(200, 210, 191, 31))
        self.textBrowser_4.setStyleSheet("background-color: transparent;")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.status = QtWidgets.QTextBrowser(Qmanager)
        self.status.setGeometry(QtCore.QRect(10, 320, 181, 31))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")
        self.btnin_admin = QtWidgets.QPushButton(Qmanager)
        self.btnin_admin.setGeometry(QtCore.QRect(400, 270, 131, 23))
        self.btnin_admin.setStyleSheet("")
        self.btnin_admin.setObjectName("btnin_admin")
        self.btnaapply = QtWidgets.QPushButton(Qmanager)
        self.btnaapply.setGeometry(QtCore.QRect(20, 210, 91, 23))
        self.btnaapply.setStyleSheet("")
        self.btnaapply.setObjectName("btnaapply")
        self.btnblock = QtWidgets.QPushButton(Qmanager)
        self.btnblock.setGeometry(QtCore.QRect(400, 300, 131, 23))
        self.btnblock.setStyleSheet("")
        self.btnblock.setObjectName("btnblock")

        self.retranslateUi(Qmanager)
        QtCore.QMetaObject.connectSlotsByName(Qmanager)

    def retranslateUi(self, Qmanager):
        _translate = QtCore.QCoreApplication.translate
        Qmanager.setWindowTitle(_translate("Qmanager", "Form"))
        self.textBrowser.setHtml(_translate("Qmanager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Управляющий </span></p></body></html>"))
        self.btnadd_hostel.setText(_translate("Qmanager", "Добавить"))
        self.adress_sort.setText(_translate("Qmanager", "адресу"))
        self.nroom_sort.setText(_translate("Qmanager", "колличеству комнат"))
        self.time.setText(_translate("Qmanager", "времени регистрации"))
        self.textBrowser_2.setHtml(_translate("Qmanager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Сортировать по:</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Qmanager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Список гостиниц</span></p></body></html>"))
        self.btnadd_admin.setText(_translate("Qmanager", "Добавить"))
        self.textBrowser_4.setHtml(_translate("Qmanager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Список администраторов</span></p></body></html>"))
        self.status.setHtml(_translate("Qmanager", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnin_admin.setText(_translate("Qmanager", "Назначить"))
        self.btnaapply.setText(_translate("Qmanager", "Применить"))
        self.btnblock.setText(_translate("Qmanager", "Заблокировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qmanager = QtWidgets.QWidget()
    ui = Ui_Qmanager()
    ui.setupUi(Qmanager)
    Qmanager.show()
    sys.exit(app.exec_())

