# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qlogin(object):
    def setupUi(self, Qlogin):
        Qlogin.setObjectName("Qlogin")
        Qlogin.resize(321, 225)
        self.centralwidget = QtWidgets.QWidget(Qlogin)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(0, 0, 21, 21))
        self.settings_button.setAutoFillBackground(False)
        self.settings_button.setStyleSheet("")
        self.settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Users/лала/Desktop/яндекс/repo\'s/Cinematic/Gear_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QtCore.QSize(21, 21))
        self.settings_button.setObjectName("settings_button")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 30, 321, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(110, 60, 201, 20))
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 90, 201, 20))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.name_cinema_wr = QtWidgets.QLabel(self.centralwidget)
        self.name_cinema_wr.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.name_cinema_wr.setObjectName("name_cinema_wr")
        self.name_cinema_wr_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_cinema_wr_2.setGeometry(QtCore.QRect(10, 90, 91, 21))
        self.name_cinema_wr_2.setObjectName("name_cinema_wr_2")
        self.btnlogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnlogin.setGeometry(QtCore.QRect(50, 120, 61, 23))
        self.btnlogin.setStyleSheet("")
        self.btnlogin.setObjectName("btnlogin")
        self.status = QtWidgets.QTextBrowser(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 140, 201, 51))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")
        self.btnexit = QtWidgets.QPushButton(self.centralwidget)
        self.btnexit.setGeometry(QtCore.QRect(120, 120, 61, 23))
        self.btnexit.setStyleSheet("")
        self.btnexit.setObjectName("btnexit")
        Qlogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Qlogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 25))
        self.menubar.setObjectName("menubar")
        Qlogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Qlogin)
        self.statusbar.setObjectName("statusbar")
        Qlogin.setStatusBar(self.statusbar)

        self.retranslateUi(Qlogin)
        QtCore.QMetaObject.connectSlotsByName(Qlogin)

    def retranslateUi(self, Qlogin):
        _translate = QtCore.QCoreApplication.translate
        Qlogin.setWindowTitle(_translate("Qlogin", "MainWindow"))
        self.textBrowser.setHtml(_translate("Qlogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600;\">Войдите в систему</span></p></body></html>"))
        self.name_cinema_wr.setText(_translate("Qlogin", "login"))
        self.name_cinema_wr_2.setText(_translate("Qlogin", "password"))
        self.btnlogin.setText(_translate("Qlogin", "Вход"))
        self.status.setHtml(_translate("Qlogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnexit.setText(_translate("Qlogin", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Qlogin = QtWidgets.QMainWindow()
    ui = Ui_Qlogin()
    ui.setupUi(Qlogin)
    Qlogin.show()
    sys.exit(app.exec_())

