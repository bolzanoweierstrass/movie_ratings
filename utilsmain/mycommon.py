'''
Created on Jan 1, 2015

@author: akira
'''
import sys
from guimain.mainWindow import Ui_MainWindow
from guimain import myAbout
from PyQt4 import QtGui


class Downloader(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupsignals()
        self.abbout = None
        self.usage = None
    def setupsignals(self):
        self.ui.actionAbout.triggered.connect(self.openAbout)
        self.ui.actionUsage.triggered.connect(self.openUsage)
        self.ui.btn_search.clicked.connect(self.showImage)
    
    def showImage(self):
        mypixmap = QtGui.QPixmap('/tmp/t.jpg')
        if not mypixmap.isNull():
            myscaled = mypixmap.scaled(self.ui.lbl_pic.size())
            self.ui.lbl_pic.setPixmap(myscaled)
        else:
            self.ui.lbl_pic.setText('unable to show the picture\n sorry for inconvinece')
        

    def openAbout(self):
        if self.abbout is None:
            self.abbout = myAbout.kera(self)
        self.abbout.show()
    def openUsage(self):
        if self.usage is None:
            self.usage = myAbout.Bulb(self)
        self.usage.show()   
        

    
        