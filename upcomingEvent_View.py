from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.upcomingEvents_frame2 import upcomingEvents_frame2
from upcomingEvent_Model import upcomingEvent_Model
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets

class upcomingEvent_view(QFrame, upcomingEvents_frame2):

    def __init__(self):
        # setup UI
        super(upcomingEvent_view, self).__init__()
        self.setupUi(self)
    
    def connectToRecord(self, mainwindow):
        self.listView.clicked.connect(self.goRecording)
        self.window = mainwindow

    def goRecording(self):
        '''
        connect database depends on different module
        '''
        self.window.stackedWidget.setCurrentIndex(2)

# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    test = upcomingEvent_view()
    model = upcomingEvent_Model()
    test.listView.setModel(model)
    test.show()

    sys.exit(app.exec_())