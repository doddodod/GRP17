from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr
from recordDialog_View import recordDialog_View
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtCore, QtWidgets


class sessionPage_ctr():

    def setCtr(self, sessionPageView):
        self.sessionPageView = sessionPageView
        self.connectSlot()
    
    def connectSlot(self):
        self.sessionPageView.recordDialog_Signal.connect(self.recordDialog)

    def recordDialog(self):
        self.dialog = recordDialog_View()
        self.dialog.show()