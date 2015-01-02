'''
Created on Jan 1, 2015

@author: akira
'''
from utilsmain import mycommon,mygenerator
from PyQt4 import QtGui
import sys 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = mycommon.Downloader()
    window.show()
    sys.exit(app.exec_())
