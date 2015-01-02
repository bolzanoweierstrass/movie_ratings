'''
Created on Jan 2, 2015

@author: akira
'''
from guimain.about import Ui_Form
from PyQt4 import QtGui 
from guimain.usage import Ui_myusage


class kera(QtGui.QWidget,Ui_Form):
    def __init__(self,parent=QtGui.QMainWindow):
        QtGui.QWidget.__init__(self,parent=None)
        self.setupUi(self)
class Bulb(QtGui.QWidget,Ui_myusage):
    def __init__(self,parent=QtGui.QMainWindow):
        QtGui.QWidget.__init__(self,parent=None)
        self.setupUi(self)