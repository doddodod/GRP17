from PyQt5.QtWidgets import QApplication
from ModuleFrame1_View import moduleFrame1_view
from ModuleFrame1_Model import moduleFrame1_Model
from upcomingEvent_View import upcomingEvent_view
from upcomingEvent_Model import upcomingEvent_Model
import sys


class modulePage_view():

    def __init__(self):
        super(modulePage_view, self).__init__()
        self.window = None

    def show(self):
       self.window.show()

    def setMainWindow(self,mainWindow):
        self.window = mainWindow
        self.setupMyUI()

    def setupMyUI(self):
        self.moduleFrame = moduleFrame1_view()
        self.upcomingFrame = upcomingEvent_view()

        self.moduleFrame.setupUi(self.window.frame1)
        self.moduleFrame.refresh()
        moduleModel = moduleFrame1_Model()
        self.moduleFrame.listView.setModel(moduleModel)

        self.upcomingFrame.setupUi(self.window.frame_2)
        upModel = upcomingEvent_Model()
        self.upcomingFrame.listView_2.setModel(upModel)



# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = modulePage_view()
    mainWindow.show()
    sys.exit(app.exec_())
