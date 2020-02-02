from PyQt5.Qt import *
from ModulePage_view import ModulePage_View
#from ModulePage_ctr import ModulePage_Ctr
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ModulePage_View()
    mainWindow.show()
    sys.exit(app.exec_())