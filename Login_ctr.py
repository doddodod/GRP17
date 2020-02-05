from ModulePage_View import modulePage_view
from basicMainWindow_View import basicMainWindow_view
from basicMainWindow_Ctr import basicMainWindow_Ctr

'''Login Controller is used for create main Window and show corresponding frames based on the main Window'''

class login_Ctr():

    def __init__(self):
        # bindModel = login_Model()
        self.loginView = None

        # create main window, set view and controller
        mainWindow = basicMainWindow_view()
        mainWindowCtr = basicMainWindow_Ctr()
        mainWindowCtr.setView(mainWindow)

        # pass main window to corresponding page class for use
        self.tmView = modulePage_view()
        self.tmView.setMainWindow(mainWindow)


    def setView(self,loginView):
        self.loginView = loginView
        self.connectSlot()

    def connectSlot(self):
        self.loginView.login_Signal.connect(self.enterMainPage)


    def enterMainPage(self):
        self.loginView.hide()
        self.tmView.show()




