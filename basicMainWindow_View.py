from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.basicStructure_mainWindow import MainWindow_Structure
import sys


class basicMainWindow_view(QMainWindow,  MainWindow_Structure):

    backTo_Sig = pyqtSignal()
    home_Sig = pyqtSignal()
    searchStudent_Sig = pyqtSignal()

    def __init__(self):
        super(basicMainWindow_view, self).__init__()
        self.setupUi(self)

    # back to last page
    def backTo(self):
        self.backTo_Sig.emit()

    # back to home page
    def home(self):
        self.home_Sig.emit()

    # search student
    def searchStudent(self):
        self.searchStudent_Sig.emit()

    # teacher info button
    def clickTeacherInfo(self):
        print("teacher info")
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = basicMainWindow_view()
    mainWindow.show()
    sys.exit(app.exec_())