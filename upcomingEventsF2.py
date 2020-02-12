from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QMainWindow, QApplication, QVBoxLayout, QLabel
from resources.teacherUIPY.upcomingEvents_frame2 import UpcomingEvents_Frame
import sys


class UpcomingEventF2(QFrame, UpcomingEvents_Frame):

    login_Signal = pyqtSignal()

    def __init__(self):
        # setup UI
        super(UpcomingEventF2, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.login)

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
    # frame = UpcomingEventF2()
    button = QLabel()
    button.setText("hahaha")
    label = QLabel()
    label.setText("hehehe")
    # mainWindow.addDockWidget(self,mainWindow.centralWidget(),frame)
    mainLayout = QVBoxLayout()
    # mainLayout.addWidget(frame)
    mainLayout.addWidget(label)
    # frame.setGeometry(QtCore.QRect(20, 30, 691, 521))
    mainWindow.setCentralWidget(button)
    mainWindow.show()
    sys.exit(app.exec_())