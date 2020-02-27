from PyQt5.QtWidgets import QFrame, QApplication, QMainWindow
from resources.teacherUIPY.studentInfo_frame1 import Ui_Frame


class oneStudentFrame_view(QFrame, Ui_Frame):

    def __init__(self):
        super(oneStudentFrame_view, self).__init__()
        self.setupUi(self)


# test code
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    test = oneStudentFrame_view()
    test.show()
    sys.exit(app.exec_())