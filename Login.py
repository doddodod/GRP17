import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from login_pane import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(MainWindow.login)

    def login(self):
        """
               Slot documentation goes here.
        """
        # TODO: not implemented yet


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())