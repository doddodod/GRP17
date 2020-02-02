from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.upcomingEvents_frame2 import Ui_Frame
import sys


class upcomingEvent(QFrame, Ui_Frame):

    login_Signal = pyqtSignal()

    def __init__(self):
        # setup UI
        super(upcomingEvent, self).__init__()
        # self.setupUi(self)

    def login(self):
        print("login")
        self.login_Signal.emit()
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

# test code

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(500,500)

    frame2 = QFrame(mainWindow)
    frame2.setGeometry(QtCore.QRect(20, 30, 300, 400))

    test = upcomingEvent()
    test.setupUi(frame2)
    mainWindow.show()
    sys.exit(app.exec_())