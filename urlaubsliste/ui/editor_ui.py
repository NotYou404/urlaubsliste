# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dominik\code\projects\Urlaubsliste Deluxe\urlaubsliste\ui\editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(364, 322)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.setAutoFillBackground(True)
        self.list.setStyleSheet("")
        self.list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 2, 0, 1, 2)
        self.categoriesLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.categoriesLabel.setFont(font)
        self.categoriesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.categoriesLabel.setObjectName("categoriesLabel")
        self.gridLayout.addWidget(self.categoriesLabel, 1, 0, 1, 2)
        self.header = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.createCategoryButton = QtWidgets.QPushButton(Dialog)
        self.createCategoryButton.setObjectName("createCategoryButton")
        self.gridLayout.addWidget(self.createCategoryButton, 3, 0, 1, 1)
        self.delCategoryButton = QtWidgets.QPushButton(Dialog)
        self.delCategoryButton.setObjectName("delCategoryButton")
        self.gridLayout.addWidget(self.delCategoryButton, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.categoriesLabel.setText(_translate("Dialog", "Kategorien"))
        self.header.setText(_translate("Dialog", "Editor"))
        self.createCategoryButton.setText(_translate("Dialog", "Kategorie erstellen..."))
        self.delCategoryButton.setText(_translate("Dialog", "Kategorie löschen"))