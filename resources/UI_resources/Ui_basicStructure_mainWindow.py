# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/derrickyu/Desktop/GRP17-master/resources/UI_resources/basicStructure_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1397, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(-1, 11, -1, 11)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 0, 6, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        self.toolButton_2.setStyleSheet("border-image: url(:/all/images/homeIcon.png)")
        self.toolButton_2.setText("")
        self.toolButton_2.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.widget)
        self.toolButton_3.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 4, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setStyleSheet("border-image: url(:/all/images/backIcon.png);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(438, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, 20, 15, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Module = QtWidgets.QWidget()
        self.Module.setObjectName("Module")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Module)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.moduleFrame1 = QtWidgets.QFrame(self.Module)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moduleFrame1.sizePolicy().hasHeightForWidth())
        self.moduleFrame1.setSizePolicy(sizePolicy)
        self.moduleFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moduleFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.moduleFrame1.setObjectName("moduleFrame1")
        self.horizontalLayout_4.addWidget(self.moduleFrame1)
        self.moduleFrame2 = QtWidgets.QFrame(self.Module)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moduleFrame2.sizePolicy().hasHeightForWidth())
        self.moduleFrame2.setSizePolicy(sizePolicy)
        self.moduleFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moduleFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.moduleFrame2.setObjectName("moduleFrame2")
        self.horizontalLayout_4.addWidget(self.moduleFrame2)
        self.stackedWidget.addWidget(self.Module)
        self.Session = QtWidgets.QWidget()
        self.Session.setObjectName("Session")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Session)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sessionFrame1 = QtWidgets.QFrame(self.Session)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sessionFrame1.sizePolicy().hasHeightForWidth())
        self.sessionFrame1.setSizePolicy(sizePolicy)
        self.sessionFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sessionFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sessionFrame1.setObjectName("sessionFrame1")
        self.horizontalLayout_5.addWidget(self.sessionFrame1)
        self.sessionFrame2 = QtWidgets.QFrame(self.Session)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sessionFrame2.sizePolicy().hasHeightForWidth())
        self.sessionFrame2.setSizePolicy(sizePolicy)
        self.sessionFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sessionFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sessionFrame2.setObjectName("sessionFrame2")
        self.horizontalLayout_5.addWidget(self.sessionFrame2)
        self.stackedWidget.addWidget(self.Session)
        self.Recording = QtWidgets.QWidget()
        self.Recording.setObjectName("Recording")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Recording)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.recordingFrame = QtWidgets.QFrame(self.Recording)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordingFrame.sizePolicy().hasHeightForWidth())
        self.recordingFrame.setSizePolicy(sizePolicy)
        self.recordingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recordingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.recordingFrame.setObjectName("recordingFrame")
        self.horizontalLayout_6.addWidget(self.recordingFrame)
        self.stackedWidget.addWidget(self.Recording)
        self.SearchResult = QtWidgets.QWidget()
        self.SearchResult.setObjectName("SearchResult")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.SearchResult)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.resultFrame1 = QtWidgets.QFrame(self.SearchResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultFrame1.sizePolicy().hasHeightForWidth())
        self.resultFrame1.setSizePolicy(sizePolicy)
        self.resultFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame1.setObjectName("resultFrame1")
        self.horizontalLayout_7.addWidget(self.resultFrame1)
        self.resultFrame2 = QtWidgets.QFrame(self.SearchResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultFrame2.sizePolicy().hasHeightForWidth())
        self.resultFrame2.setSizePolicy(sizePolicy)
        self.resultFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame2.setObjectName("resultFrame2")
        self.horizontalLayout_7.addWidget(self.resultFrame2)
        self.stackedWidget.addWidget(self.SearchResult)
        self.OneStudent = QtWidgets.QWidget()
        self.OneStudent.setObjectName("OneStudent")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.OneStudent)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.oneStudentFrame1 = QtWidgets.QFrame(self.OneStudent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneStudentFrame1.sizePolicy().hasHeightForWidth())
        self.oneStudentFrame1.setSizePolicy(sizePolicy)
        self.oneStudentFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.oneStudentFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.oneStudentFrame1.setObjectName("oneStudentFrame1")
        self.horizontalLayout_8.addWidget(self.oneStudentFrame1)
        self.oneStudentFrame2 = QtWidgets.QFrame(self.OneStudent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneStudentFrame2.sizePolicy().hasHeightForWidth())
        self.oneStudentFrame2.setSizePolicy(sizePolicy)
        self.oneStudentFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.oneStudentFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.oneStudentFrame2.setObjectName("oneStudentFrame2")
        self.horizontalLayout_8.addWidget(self.oneStudentFrame2)
        self.stackedWidget.addWidget(self.OneStudent)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teacherInfoFrame1 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacherInfoFrame1.sizePolicy().hasHeightForWidth())
        self.teacherInfoFrame1.setSizePolicy(sizePolicy)
        self.teacherInfoFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teacherInfoFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teacherInfoFrame1.setObjectName("teacherInfoFrame1")
        self.horizontalLayout.addWidget(self.teacherInfoFrame1)
        self.teacherInfoFrame2 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacherInfoFrame2.sizePolicy().hasHeightForWidth())
        self.teacherInfoFrame2.setSizePolicy(sizePolicy)
        self.teacherInfoFrame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teacherInfoFrame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teacherInfoFrame2.setObjectName("teacherInfoFrame2")
        self.horizontalLayout.addWidget(self.teacherInfoFrame2)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1397, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setGeometry(QtCore.QRect(355, 266, 126, 96))
        self.menuAbout.setObjectName("menuAbout")
        self.menuPrint = QtWidgets.QMenu(self.menuBar)
        self.menuPrint.setObjectName("menuPrint")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionHelo = QtWidgets.QAction(MainWindow)
        self.actionHelo.setObjectName("actionHelo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionhui = QtWidgets.QAction(MainWindow)
        self.actionhui.setObjectName("actionhui")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionGuide = QtWidgets.QAction(MainWindow)
        self.actionGuide.setObjectName("actionGuide")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuAbout.addAction(self.actionHelo)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menuPrint.addAction(self.actionOpen)
        self.menuPrint.addAction(self.actionGuide)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuBar.addAction(self.menuPrint.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.toolButton.clicked.connect(MainWindow.backTo)
        self.toolButton_2.clicked.connect(MainWindow.home)
        self.toolButton_3.clicked.connect(MainWindow.searchStudent)
        self.toolButton_4.clicked.connect(MainWindow.clickTeacherInfo)
        self.actionOpen.triggered.connect(MainWindow.printInfo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_4.setText(_translate("MainWindow", "TeacherInfo"))
        self.menuFile.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionHelo.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionhui.setText(_translate("MainWindow", "hui"))
        self.actionopen.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionGuide.setText(_translate("MainWindow", "Guide"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())