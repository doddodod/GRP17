# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upcomingEvents_frame2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class upcomingEvents_frame2(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(394, 556)
        self.gridLayout_2 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setMargin(20)
        self.verticalLayout.addWidget(self.label_3)
        self.listView_2 = QtWidgets.QListView(Frame)
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout.addWidget(self.listView_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leftPage_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPage_pushButton.sizePolicy().hasHeightForWidth())
        self.leftPage_pushButton.setSizePolicy(sizePolicy)
        self.leftPage_pushButton.setMaximumSize(QtCore.QSize(30, 20))
        self.leftPage_pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.leftPage_pushButton.setObjectName("leftPage_pushButton")
        self.horizontalLayout_4.addWidget(self.leftPage_pushButton)
        self.rightPage_pushButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightPage_pushButton.sizePolicy().hasHeightForWidth())
        self.rightPage_pushButton.setSizePolicy(sizePolicy)
        self.rightPage_pushButton.setMaximumSize(QtCore.QSize(30, 20))
        self.rightPage_pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.rightPage_pushButton.setObjectName("rightPage_pushButton")
        self.horizontalLayout_4.addWidget(self.rightPage_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.showNum_lineEdit = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showNum_lineEdit.sizePolicy().hasHeightForWidth())
        self.showNum_lineEdit.setSizePolicy(sizePolicy)
        self.showNum_lineEdit.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showNum_lineEdit.setFont(font)
        self.showNum_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.showNum_lineEdit.setObjectName("showNum_lineEdit")
        self.horizontalLayout.addWidget(self.showNum_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        self.showNum_lineEdit.returnPressed.connect(self.editShowNum)
        self.leftPage_pushButton.clicked.connect(self.leftPage)
        self.rightPage_pushButton.clicked.connect(self.rightPage)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_3.setText(_translate("Frame", "Upcoming Events"))
        self.leftPage_pushButton.setText(_translate("Frame", "<"))
        self.rightPage_pushButton.setText(_translate("Frame", ">"))
        self.label_7.setText(_translate("Frame", "Show"))
        self.showNum_lineEdit.setText(_translate("Frame", "5"))
