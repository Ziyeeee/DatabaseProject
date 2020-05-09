# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAddressDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 216)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Recipient = QtWidgets.QLabel(self.widget)
        self.Recipient.setObjectName("Recipient")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Recipient)
        self.Tel = QtWidgets.QLabel(self.widget)
        self.Tel.setObjectName("Tel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Tel)
        self.address = QtWidgets.QLabel(self.widget)
        self.address.setObjectName("address")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.address)
        self.postcode = QtWidgets.QLabel(self.widget)
        self.postcode.setObjectName("postcode")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.postcode)
        self.infoAddressTextBrowser = QtWidgets.QTextBrowser(self.widget)
        self.infoAddressTextBrowser.setMaximumSize(QtCore.QSize(1000, 80))
        self.infoAddressTextBrowser.setReadOnly(False)
        self.infoAddressTextBrowser.setObjectName("infoAddressTextBrowser")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infoAddressTextBrowser)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.RnameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.RnameLineEdit.setObjectName("RnameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RnameLineEdit)
        self.TelLineEdit = QtWidgets.QLineEdit(self.widget)
        self.TelLineEdit.setObjectName("TelLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TelLineEdit)
        self.postcodeLineEdit = QtWidgets.QLineEdit(self.widget)
        self.postcodeLineEdit.setObjectName("postcodeLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.postcodeLineEdit)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Recipient.setText(_translate("Dialog", "收件人"))
        self.Tel.setText(_translate("Dialog", "电话"))
        self.address.setText(_translate("Dialog", "地址"))
        self.postcode.setText(_translate("Dialog", "邮编"))
        self.pushButton.setText(_translate("Dialog", "确定"))

