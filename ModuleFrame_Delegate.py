from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate, QWidget

from lineWidget_View import lineWidget


class moduleFrame_Deletagte(QStyledItemDelegate):

    def __init__(self,parent=None):
        QStyledItemDelegate.__init__(self,parent)

    def createEditor(self, parent: QWidget,
                     option: 'QStyleOptionViewItem',
                     index: QtCore.QModelIndex):
        # edit the lineWidget for module page
        editor = lineWidget()
        editor.toolButton_8.hide()
        editor.toolButton_9.hide()
        editor.setMinimumHeight(45)
        # .toolButton_10.clicked().connect(self.starItem)
        return editor

    # load data to editor from model
    def setEditorData(self, editor: lineWidget, index: QtCore.QModelIndex):
        print("here")
        value = index.model().data(index, Qt.DisplayRole)
        editor.label_6.setText(str(value))

    # load data to model from editor
    def setModelData(self, editor: lineWidget, model, index):
        model.setData(index,editor.label_6.text())

    # set geometry for editor
    def updateEditorGeometry(self, editor: lineWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex):
        editor.setGeometry(option.rect)


    def starItem(self,index):
        print("start item"+index)
