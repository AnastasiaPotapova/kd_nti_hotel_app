# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'to_csv.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToCSV(object):
    def setupUi(self, ToCSV):
        ToCSV.setObjectName("ToCSV")
        ToCSV.resize(330, 229)
        self.textBrowser_3 = QtWidgets.QTextBrowser(ToCSV)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.textBrowser_3.setStyleSheet("background-color: transparent;")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.btnto_csv = QtWidgets.QPushButton(ToCSV)
        self.btnto_csv.setGeometry(QtCore.QRect(220, 190, 91, 31))
        self.btnto_csv.setStyleSheet("")
        self.btnto_csv.setObjectName("btnto_csv")
        self.textBrowser_4 = QtWidgets.QTextBrowser(ToCSV)
        self.textBrowser_4.setGeometry(QtCore.QRect(210, 50, 111, 141))
        self.textBrowser_4.setStyleSheet("background-color: transparent;")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.lodger_session = QtWidgets.QLabel(ToCSV)
        self.lodger_session.setGeometry(QtCore.QRect(10, 50, 191, 131))
        self.lodger_session.setMaximumSize(QtCore.QSize(271, 131))
        self.lodger_session.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lodger_session.setMouseTracking(True)
        self.lodger_session.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lodger_session.setFrameShape(QtWidgets.QFrame.Box)
        self.lodger_session.setText("")
        self.lodger_session.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lodger_session.setObjectName("lodger_session")
        self.status = QtWidgets.QTextBrowser(ToCSV)
        self.status.setGeometry(QtCore.QRect(10, 180, 181, 41))
        self.status.setStyleSheet("background-color: transparent;")
        self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.status.setObjectName("status")

        self.retranslateUi(ToCSV)
        QtCore.QMetaObject.connectSlotsByName(ToCSV)

    def retranslateUi(self, ToCSV):
        _translate = QtCore.QCoreApplication.translate
        ToCSV.setWindowTitle(_translate("ToCSV", "Form"))
        self.textBrowser_3.setHtml(_translate("ToCSV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выгрузить в csv формат</p></body></html>"))
        self.btnto_csv.setText(_translate("ToCSV", "Выгрузить"))
        self.textBrowser_4.setHtml(_translate("ToCSV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Нажмите на имена постояльцев, которых вы бы хотели выгрузить</p></body></html>"))
        self.status.setHtml(_translate("ToCSV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToCSV = QtWidgets.QWidget()
    ui = Ui_ToCSV()
    ui.setupUi(ToCSV)
    ToCSV.show()
    sys.exit(app.exec_())

