# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicStructure_frame1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(730, 571)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.printTButton_TBS = QtWidgets.QToolButton(Frame)
        self.printTButton_TBS.setStyleSheet("border-image:url(:/all/images/printIcon.png)")
        self.printTButton_TBS.setText("")
        self.printTButton_TBS.setObjectName("printTButton_TBS")
        self.horizontalLayout.addWidget(self.printTButton_TBS)
        self.frameName_TBS = QtWidgets.QLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameName_TBS.sizePolicy().hasHeightForWidth())
        self.frameName_TBS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.frameName_TBS.setFont(font)
        self.frameName_TBS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frameName_TBS.setObjectName("frameName_TBS")
        self.horizontalLayout.addWidget(self.frameName_TBS)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(50, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.search_horizontalLayout = QtWidgets.QHBoxLayout()
        self.search_horizontalLayout.setObjectName("search_horizontalLayout")
        self.search_lineEdit = QtWidgets.QLineEdit(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_lineEdit.setSizePolicy(sizePolicy)
        self.search_lineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.search_horizontalLayout.addWidget(self.search_lineEdit)
        self.search_toolButton = QtWidgets.QToolButton(Frame)
        self.search_toolButton.setStyleSheet("border-image:url(:/all/images/searchIcon.png)")
        self.search_toolButton.setText("")
        self.search_toolButton.setObjectName("search_toolButton")
        self.search_horizontalLayout.addWidget(self.search_toolButton)
        self.horizontalLayout_3.addLayout(self.search_horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(218, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.addButton = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.addButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_3.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.listView = QtWidgets.QListView(Frame)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        self.printTButton_TBS.clicked.connect(self.print)
        self.comboBox.currentTextChanged['QString'].connect(self.sort)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.frameName_TBS.setText(_translate("Frame", "FrameName"))
        self.comboBox.setItemText(0, _translate("Frame", "All"))
        self.comboBox.setItemText(1, _translate("Frame", "In Progress"))
        self.comboBox.setItemText(2, _translate("Frame", "Future"))
        self.comboBox.setItemText(3, _translate("Frame", "Past"))
        self.comboBox.setItemText(4, _translate("Frame", "Starred"))
        self.addButton.setText(_translate("Frame", "Add"))
import resources.images_rc
