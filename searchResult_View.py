from searchStudentFrame_View import searchStudentFrame_View
from upcomingEvent_View import upcomingEvent_view
from PyQt5.QtWidgets import QApplication, QMainWindow
from upcomingEvent_Model import upcomingEvent_Model
from searchResult_Ctr import searchResult_Ctr
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets

class searchResult_View(QMainWindow):
    OneStudentInfo_Signal = pyqtSignal()

    def __init__(self):
        super(searchResult_View, self).__init__()
        
        
    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
    
    def setMainWindow(self, mainWindow, logCtr):
        self.window = mainWindow
        #to get View in class logCtr
        self.logCtr = logCtr
        self.setupMyUI()
    
    def setupMyUI(self):
        ##connect with Ctr
        self.searchResultCtr = searchResult_Ctr()
        self.searchResultCtr.setCtr(self, self.window)

        #build view
        self.Frame1 = searchStudentFrame_View()
        self.upcomingFrame = upcomingEvent_view()

        #set Model when enter the page
        self.Frame1.setupUi(self.window.resultFrame1)
        self.upcomingFrame.setupUi(self.window.resultFrame2)
    
        
        #Test Button
        self.btn = QtWidgets.QPushButton(self.window.resultFrame1)
        self.btn.setText("StudentName       123456")
        self.btn.setGeometry(40,300,650,50)
        self.btn.clicked.connect(self.goStudentInfo)

    def goStudentInfo(self):
        self.OneStudentInfo_Signal.emit()
        



