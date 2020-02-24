from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.print_frame import Ui_Frame
import sys


class printFrame_view(QFrame, Ui_Frame):

    def __init__(self):
        # setup UI
        super(printFrame_view, self).__init__()
        self.setupUi(self)


# test code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    mainWindow.resize(800,500)

    frame1 = QFrame(mainWindow)
    frame1.setGeometry(QtCore.QRect(0, 30, 300, 400))

    test = printFrame_view()
    test.setupUi(frame1)

    mainWindow.show()

    sys.exit(app.exec_())