# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 149)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.que1Label = QtWidgets.QLabel(Dialog)
        self.que1Label.setObjectName("que1Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.que1Label)
        self.ans1LineEdit = QtWidgets.QLineEdit(Dialog)
        self.ans1LineEdit.setObjectName("ans1LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ans1LineEdit)
        self.que2Label = QtWidgets.QLabel(Dialog)
        self.que2Label.setObjectName("que2Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.que2Label)
        self.ans2LineEdit = QtWidgets.QLineEdit(Dialog)
        self.ans2LineEdit.setObjectName("ans2LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ans2LineEdit)
        self.keyLable = QtWidgets.QLabel(Dialog)
        self.keyLable.setObjectName("keyLable")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.keyLable)
        self.keyLineEdit = QtWidgets.QLineEdit(Dialog)
        self.keyLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.keyLineEdit)
        self.confirmLabel = QtWidgets.QLabel(Dialog)
        self.confirmLabel.setObjectName("confirmLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.confirmLabel)
        self.confirmLineEdit = QtWidgets.QLineEdit(Dialog)
        self.confirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLineEdit.setObjectName("confirmLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirmLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.que1Label.setText(_translate("Dialog", "“问题1”"))
        self.que2Label.setText(_translate("Dialog", "“问题2”"))
        self.keyLable.setText(_translate("Dialog", "新密码"))
        self.confirmLabel.setText(_translate("Dialog", "确认密码"))
        self.pushButton.setText(_translate("Dialog", "确认"))

