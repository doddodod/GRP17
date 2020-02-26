from basicMainWindow_View import basicMainWindow_view

from basicMainWindow_Ctr import basicMainWindow_Ctr

from oneStudentPage_View import oneStudentPage_View

from upcomingEvent_View import upcomingEvent_view

from upcomingEvent_Model import upcomingEvent_Model

class searchResult_Ctr():
    def setCtr(self, searchResultView, mainwindow):
        self.searchResultView = searchResultView
        self.mainwindow = mainwindow
        self.connectSlot()
    
    def connectSlot(self):
        self.searchResultView.OneStudentInfo_Signal.connect(self.OneStudentInfo)
    
    def OneStudentInfo(self):
        print("One Student")
        self.upcomingModel = upcomingEvent_Model()
        self.searchResultView.logCtr.oneStudentPage_View.upcomingFrame.listView.setModel(self.upcomingModel)
        '''
        Load student info model here
        self.searchResultView.logCtr.oneStudentPage_View.Frame1.listView
        '''
        self.mainwindow.stackedWidget.setCurrentIndex(4)
        
