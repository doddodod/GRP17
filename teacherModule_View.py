from PyQt5.QtWidgets import QMainWindow, QApplication
from resources.teacherUIPY.basicStructure_mainWindow import basicStructure
import sys


class teacherModule_View(QMainWindow, basicStructure):
    def __init__(self):
        super(teacherModule_View, self).__init__()
        self.tmCtr = None
        self.setupUi(self)


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = teacherModule_View()
    mainWindow.show()
    sys.exit(app.exec_())