from teacherModule_View import teacherModule_View
from teacherModule_Ctr import teacherModule_Ctr

class login_Ctr():

    def __init__(self):
        # bindModel = login_Model()
        self.loginView = None
        self.tmView = teacherModule_View()
        self.tmCtr = teacherModule_Ctr()


    def setView(self,loginView):
        self.loginView = loginView
        self.connectSlot()

    def connectSlot(self):
        self.loginView.login_Signal.connect(self.enterMainPage)


    def enterMainPage(self):
        self.loginView.hide()
        self.tmCtr.setView(self.tmView)
        self.tmView.show()




