from recordingFrame_View import recordingFrame_View
from upcomingEvent_View import upcomingEvent_view

class recordingPage_View():
    def __init__(self):
        super(recordingPage_View, self).__init__()

        #connect with ctr
    
    def show(self):
        self.window.show()
    
    def hide(self):
        self.window.hide()

    def setMainWindow(self, mainwindow):
        self.window = mainwindow
        self.setupMyUI()
    
    def setupMyUI(self):
        self.recordingFrame = recordingFrame_View()
        
        self.recordingFrame.setupUi(self.window.frame1)
        self.window.frame_2.hide()