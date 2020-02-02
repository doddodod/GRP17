from resources.teacherUIPY.Ui_basicStructure_mainWindow import basicStructure
from resources.teacherUIPY.Ui_upcomingEvents_frame2 import UpcomingEvents
from resources.teacherUIPY.Ui_modulePage_frame1 import ModulePage
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class ModulePage_View(QMainWindow, basicStructure):
    def __init__(self):
        super(ModulePage_View, self).__init__()
        self.mpView = None
        self.setupUi(self)
        #self.ui = ModulePage()
        #self.ui.setupUi(basicStructure.frame)
        self.Module = ModulePage()
        self.Module.setupUi(self.frame)
        #self.MaingridLayout.addChildWidget(self.ui)
        #self.pushButton_4.clicked.connect(self.seView)
        self.Event = UpcomingEvents()
        self.Event.setupUi(self.frame_2)
    
    def setView():
        print("work")

#test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ModulePage_View()
    mainWindow.show()
    sys.exit(app.exec_())