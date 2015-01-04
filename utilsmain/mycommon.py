'''
Created on Jan 1, 2015

@author: akira
'''

from guimain.mainWindow import Ui_MainWindow
from guimain import myAbout
from PyQt4 import QtGui
from utilsmain.mygenerator import  Common

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
        self.ui.btn_search.clicked.connect(self.onBtnClicked)
        
    
    def getData(self):
        title = str(self.ui.lne_url.text())
        plot = str(self.ui.cmb_plot.currentText())
        inp = Common()
        if self.ui.rbtn_title.isChecked():
            data = inp.getDataByTitle(title,plot)
            return data
        else:
            data = inp.getDataBySearch(title)
            return data
   
    def onBtnClicked(self):
        self.ui.txb_title.clear()
        data = self.getData()
        if data.has_key('Title'):
            mylist = ['Title','Released','Genre','Actors','Runtime','imdbRating','tomatoImage','tomatoMeter']
            for i in range(0,len(mylist)):
                self.ui.txb_title.append(mylist[i] + "=" + data[mylist[i]])
            self.ui.txtb_plot.setText(data['Plot'])
        else:
            sdata = data.get('Search')
            for i in range(len(sdata)):
#                 for k,v in sdata[i].items():
                self.ui.txb_title.append("Title = " + sdata[i]['Title'] + "\t" + "Year = " + sdata[i]['Year'])
#                     self.ui.txb_title.append(k + " = " + sdata[i][k])
        
    
    def openAbout(self):
        if self.abbout is None:
            self.abbout = myAbout.kera(self)
        self.abbout.show()
    def openUsage(self):
        if self.usage is None:
            self.usage = myAbout.Bulb(self)
        self.usage.show()   
        

    
        