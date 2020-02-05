# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManagerW(object):
    def setupUi(self, ManagerW):
        ManagerW.setObjectName("ManagerW")
        ManagerW.resize(430, 199)
        self.textBrowser = QtWidgets.QTextBrowser(ManagerW)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 391, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.btnadd_hostel = QtWidgets.QPushButton(ManagerW)
        self.btnadd_hostel.setGeometry(QtCore.QRect(350, 60, 61, 23))
        self.btnadd_hostel.setStyleSheet("")
        self.btnadd_hostel.setObjectName("btnadd_hostel")
        self.hotel_session = QtWidgets.QLabel(ManagerW)
        self.hotel_session.setGeometry(QtCore.QRect(140, 60, 191, 131))
        self.hotel_session.setMaximumSize(QtCore.QSize(271, 131))
        self.hotel_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.hotel_session.setMouseTracking(True)
        self.hotel_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hotel_session.setFrameShape(QtWidgets.QFrame.Box)
        self.hotel_session.setText("")
        self.hotel_session.setObjectName("hotel_session")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ManagerW)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 134, 131))
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
        self.id = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.id.setChecked(False)
        self.id.setObjectName("id")
        self.sorts.addWidget(self.id)
        self.textBrowser_2 = QtWidgets.QTextBrowser(ManagerW)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.textBrowser_2.setStyleSheet("background-color: transparent;")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(ManagerW)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 40, 191, 21))
        self.textBrowser_3.setStyleSheet("background-color: transparent;")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(ManagerW)
        QtCore.QMetaObject.connectSlotsByName(ManagerW)

    def retranslateUi(self, ManagerW):
        _translate = QtCore.QCoreApplication.translate
        ManagerW.setWindowTitle(_translate("ManagerW", "Form"))
        self.textBrowser.setHtml(_translate("ManagerW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Управляющий </p></body></html>"))
        self.btnadd_hostel.setText(_translate("ManagerW", "Добавить"))
        self.adress_sort.setText(_translate("ManagerW", "адресу"))
        self.nroom_sort.setText(_translate("ManagerW", "колличеству комнат"))
        self.id.setText(_translate("ManagerW", "времени регистрации"))
        self.textBrowser_2.setHtml(_translate("ManagerW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сортировать по:</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("ManagerW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список гостиниц</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManagerW = QtWidgets.QWidget()
    ui = Ui_ManagerW()
    ui.setupUi(ManagerW)
    ManagerW.show()
    sys.exit(app.exec_())

