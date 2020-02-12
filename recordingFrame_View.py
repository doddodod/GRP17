from resources.teacherUIPY.recording_totalframe import recording_totalframe
import sys
from PyQt5.QtCore import pyqtSignal
from recordingFrame_ctr import recordingFrame_ctr
from PyQt5.QtWidgets import QFrame, QApplication


class recordingFrame_View(QFrame, recording_totalframe):
    start_Signal = pyqtSignal()
    

    def __init__(self):
        super(recordingFrame_View, self).__init__()
        self.setupUi(self)

        #connect with ctr
        self.recordingFrameCtr = recordingFrame_ctr()
        self.recordingFrameCtr.setCtr(self)
        
        self.pushButton.clicked.connect(self.recording)

    def recording(self):
        print("works")
        self.start_Signal.emit()
    