# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usage.ui'
#
# Created: Fri Jan  2 13:18:25 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_myusage(object):
    def setupUi(self, myusage):
        myusage.setObjectName(_fromUtf8("myusage"))
        myusage.setWindowModality(QtCore.Qt.WindowModal)
        myusage.resize(291, 450)
        myusage.setMaximumSize(QtCore.QSize(291, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/page.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        myusage.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(myusage)
        self.pushButton.setGeometry(QtCore.QRect(90, 410, 111, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/heart.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(myusage)
        self.textBrowser.setGeometry(QtCore.QRect(0, 260, 289, 151))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.widget = QtGui.QWidget(myusage)
        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 261))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(120, 120))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/ico/head.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(myusage)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), myusage.close)
        QtCore.QMetaObject.connectSlotsByName(myusage)

    def retranslateUi(self, myusage):
        myusage.setWindowTitle(_translate("myusage", "usage", None))
        self.pushButton.setToolTip(_translate("myusage", "click to exit this window", None))
        self.pushButton.setText(_translate("myusage", "ok", None))
        self.textBrowser.setHtml(_translate("myusage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Just a random pic that was in my computer</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this is the first program i have written and it\'s fairly simple to use</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">just type the name of the movie in the search bar and click the search button or just press enter and it will give you the movie details, ie ratings,critics,poster etc.</p></body></html>", None))

import resource
