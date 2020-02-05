# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(297, 209)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.textBrowser.setStyleSheet("background-color: transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.btnadd_lodger = QtWidgets.QPushButton(Form)
        self.btnadd_lodger.setGeometry(QtCore.QRect(210, 60, 81, 23))
        self.btnadd_lodger.setStyleSheet("")
        self.btnadd_lodger.setObjectName("btnadd_lodger")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 40, 191, 21))
        self.textBrowser_3.setStyleSheet("background-color: transparent;")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.hotel_session = QtWidgets.QLabel(Form)
        self.hotel_session.setGeometry(QtCore.QRect(10, 60, 191, 131))
        self.hotel_session.setMaximumSize(QtCore.QSize(271, 131))
        self.hotel_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.hotel_session.setMouseTracking(True)
        self.hotel_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hotel_session.setFrameShape(QtWidgets.QFrame.Box)
        self.hotel_session.setText("")
        self.hotel_session.setObjectName("hotel_session")
        self.btndelete_lodger = QtWidgets.QPushButton(Form)
        self.btndelete_lodger.setGeometry(QtCore.QRect(210, 90, 81, 23))
        self.btndelete_lodger.setStyleSheet("")
        self.btndelete_lodger.setObjectName("btndelete_lodger")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Администратор</p></body></html>"))
        self.btnadd_lodger.setText(_translate("Form", "Заселить"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список постояльцев</p></body></html>"))
        self.btndelete_lodger.setText(_translate("Form", "Выселить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

