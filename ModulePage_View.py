from PyQt5.QtWidgets import QApplication
from moduleFrame1_View import moduleFrame1_view
from upcomingEvent_View import upcomingEvent_view
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
        self.upcomingFrame.setupUi(self.window.frame_2)


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = modulePage_view()
    mainWindow.show()
    sys.exit(app.exec_())