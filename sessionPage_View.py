from sessionFrame1_View import sessionFrame1_View
from upcomingEvent_View import upcomingEvent_view
from sessionPage_ctr import sessionPage_ctr
from recordDialog_ctr import recordDialog_ctr
from PyQt5.QtWidgets import QMainWindow, QApplication,QFrame
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import pyqtSignal

class sessionPage_View(QMainWindow):
    recordDialog_Signal = pyqtSignal()

    def __init__(self):
        super(sessionPage_View, self).__init__()
        self.window = None
        #connect with Ctr
        self.sessionPageCtr = sessionPage_ctr()
        self.sessionPageCtr.setCtr(self)
    
    def show(self):
        self.window.show()

    def setMainWindow(self, mainWindow):
        self.window = mainWindow
        self.setupMyUI()

    def setupMyUI(self):
        self.sessionFrame = sessionFrame1_View()
        self.upcomingFrame = upcomingEvent_view()

        self.sessionFrame.setupUi(self.window.frame1)
        self.sessionFrame.refresh()
        self.upcomingFrame.setupUi(self.window.frame_2)

        #test button
        self.btn = QtWidgets.QPushButton(self.window)
        self.btn.setText("Jump1")
        self.btn.setGeometry(40,150,650,50)
        self.btn.clicked.connect(self.recordDialog)
        #test button
    
    def recordDialog(self):
        print("dialog")
        self.recordDialog_Signal.emit()
