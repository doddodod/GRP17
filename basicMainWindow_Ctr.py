from basicMainWindow_View import basicMainWindow_view
from upcomingEvent_View import upcomingEvent_view
from upcomingEvent_Model import upcomingEvent_Model
from printFrame_View import printFrame_view
from sessionFrame1_Model import sessionFrame1_model
from sessionFrame1_Delegate import sessionFrame_delegate
class basicMainWindow_Ctr():

    def __init__(self):
        self.bind()

    def bind(self):
        self.bmView = None
        # TODO: bind model
        # self.NameModel =

    def setView(self, bmView, logCtr):
        self.bmView = bmView
        #to get searchResult_View in logCtr
        self.logCtr = logCtr
        self.connectSlot()

    def setWindow(self, window):
        self.window = window

    def connectSlot(self):
        self.bmView.backTo_Sig.connect(self.backTo)
        self.bmView.home_Sig.connect(self.home)
        self.bmView.searchStudent_Sig.connect(self.searchStudent)
        self.bmView.teacherInfo_Sig.connect(self.clickTeacherInfo)
        self.bmView.print_Sig.connect(self.printInfo)

    def backTo(self):
        if self.bmView.stackedWidget.currentIndex() == 1: #session to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 2: #recoridng to session
            #防止一开始从module界面的upcoming直接record, 返回时session界面为空
            self.sessionModel = sessionFrame1_model()
            self.sessionDelegate = sessionFrame_delegate()
            self.logCtr.sessionView.Frame1.listView.setModel(self.sessionModel)
            self.logCtr.sessionView.Frame1.listView.setItemDelegate(self.sessionDelegate)
            self.upcomingModel = upcomingEvent_Model()
            self.logCtr.sessionView.upcomingFrame.listView.setModel(self.upcomingModel)

            self.bmView.stackedWidget.setCurrentIndex(1)
        elif self.bmView.stackedWidget.currentIndex() == 4: #one student to general result
            self.bmView.stackedWidget.setCurrentIndex(3)
        elif self.bmView.stackedWidget.currentIndex() == 3: #general result to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        elif self.bmView.stackedWidget.currentIndex() == 5: #teacher info to module
            self.bmView.stackedWidget.setCurrentIndex(0)
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def home(self):
        print("go home")
        self.bmView.stackedWidget.setCurrentIndex(0)
        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def searchStudent(self):
        print("search student") 

        '''
        load student list View and model here
        self.logCtr.searchResult_View.Frame1.listView
        '''
        # TODO: write the code when connect to the database

        self.upcomingModel = upcomingEvent_Model()
        self.logCtr.searchResult_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.bmView.stackedWidget.setCurrentIndex(3)
        

        """
            Slot documentation goes here.
        """
        # TODO: not implemented yet

    def clickTeacherInfo(self):
        print("Teacher Info")
        '''
        load teacher info here OR load in Login_ctr when set the page
        '''
        self.upcomingModel = upcomingEvent_Model()
        self.logCtr.teacherInfoPage_View.upcomingFrame.listView.setModel(self.upcomingModel)

        self.bmView.stackedWidget.setCurrentIndex(5)
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet

    def printInfo(self):
        print("print")
        







