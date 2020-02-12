from PyQt5.QtWidgets import QMainWindow, QApplication,QFrame
from moduleFrame1_View import moduleFrame1_view
from upcomingEvent_View import upcomingEvent_view
from ModulePage_ctr import ModulePage_ctr
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore

class modulePage_view(QMainWindow):
    enterSessionPage_Signal = pyqtSignal()

    def __init__(self):
        super(modulePage_view, self).__init__()
        self.window = None
        #connect with Ctr
        self.modulePageCtr = ModulePage_ctr()
        self.modulePageCtr.setCtr(self)

    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()

    def setMainWindow(self,mainWindow):
        
        self.window = mainWindow
        self.setupMyUI()

    def setupMyUI(self):
        self.moduleFrame = moduleFrame1_view()
        self.upcomingFrame = upcomingEvent_view()
        '''
        self.moduleFrameCtr = moduleFrame1_ctr()
        self.upcomingFrameCtr = upcomingEvent_ctr()
        '''
        self.moduleFrame.setupUi(self.window.frame1)
        self.moduleFrame.refresh()
        self.upcomingFrame.setupUi(self.window.frame_2)


        #test button
        self.btn = QtWidgets.QPushButton(self.window)
        self.btn.setText("Jump1")
        self.btn.setGeometry(40,150,650,50)
        self.btn.clicked.connect(self.goSession)
        #test button

    def goSession(self):
        print("Session")
        self.enterSessionPage_Signal.emit()


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = modulePage_view()
    mainWindow.show()
    sys.exit(app.exec_())