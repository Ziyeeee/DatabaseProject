# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(241, 258)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseLable = QtWidgets.QLabel(Form)
        self.chooseLable.setObjectName("chooseLable")
        self.horizontalLayout_2.addWidget(self.chooseLable)
        self.chooseComboBox = QtWidgets.QComboBox(Form)
        self.chooseComboBox.setObjectName("chooseComboBox")
        self.chooseComboBox.addItem("")
        self.chooseComboBox.addItem("")
        self.chooseComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.chooseComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.nameLable = QtWidgets.QLabel(Form)
        self.nameLable.setObjectName("nameLable")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLable)
        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.keyLable = QtWidgets.QLabel(Form)
        self.keyLable.setObjectName("keyLable")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.keyLable)
        self.keyLineEdit = QtWidgets.QLineEdit(Form)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.keyLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.signUpPushButton = QtWidgets.QPushButton(Form)
        self.signUpPushButton.setObjectName("signUpPushButton")
        self.horizontalLayout_3.addWidget(self.signUpPushButton)
        self.signInPushButton = QtWidgets.QPushButton(Form)
        self.signInPushButton.setObjectName("signInPushButton")
        self.horizontalLayout_3.addWidget(self.signInPushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chooseLable.setText(_translate("Form", "选择身份"))
        self.chooseComboBox.setItemText(0, _translate("Form", "用户"))
        self.chooseComboBox.setItemText(1, _translate("Form", "商家"))
        self.chooseComboBox.setItemText(2, _translate("Form", "管理员"))
        self.nameLable.setText(_translate("Form", "昵称"))
        self.keyLable.setText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "忘记密码"))
        self.signUpPushButton.setText(_translate("Form", "注册"))
        self.signInPushButton.setText(_translate("Form", "登录"))

