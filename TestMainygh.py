from PyQt5.Qt import *
from ModulePage_View_YGH import ModulePage_view
#from ModulePage_ctr import ModulePage_Ctr
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ModulePage_view()
    mainWindow.show()
    sys.exit(app.exec_())