# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCommodityDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 355)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.describeLabel = QtWidgets.QLabel(Dialog)
        self.describeLabel.setObjectName("describeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.describeLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.describeTextEdit = QtWidgets.QTextEdit(Dialog)
        self.describeTextEdit.setObjectName("describeTextEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.describeTextEdit)
        self.priceLabel = QtWidgets.QLabel(Dialog)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.priceSpinBox = QtWidgets.QSpinBox(Dialog)
        self.priceSpinBox.setMaximum(1000000)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.priceSpinBox)
        self.discountLabel = QtWidgets.QLabel(Dialog)
        self.discountLabel.setObjectName("discountLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.discountLabel)
        self.discountDoubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.discountDoubleSpinBox.setMaximum(1.0)
        self.discountDoubleSpinBox.setSingleStep(0.05)
        self.discountDoubleSpinBox.setProperty("value", 1.0)
        self.discountDoubleSpinBox.setObjectName("discountDoubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.discountDoubleSpinBox)
        self.sizeLabel = QtWidgets.QLabel(Dialog)
        self.sizeLabel.setObjectName("sizeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sizeLabel)
        self.sizeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.sizeLineEdit.setObjectName("sizeLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sizeLineEdit)
        self.WidLabel = QtWidgets.QLabel(Dialog)
        self.WidLabel.setObjectName("WidLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.WidLabel)
        self.stockLabel = QtWidgets.QLabel(Dialog)
        self.stockLabel.setObjectName("stockLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.stockLabel)
        self.WidLineEdit = QtWidgets.QLineEdit(Dialog)
        self.WidLineEdit.setObjectName("WidLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.WidLineEdit)
        self.stockSpinBox = QtWidgets.QSpinBox(Dialog)
        self.stockSpinBox.setMaximum(10000)
        self.stockSpinBox.setObjectName("stockSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.stockSpinBox)
        self.addressLabel = QtWidgets.QLabel(Dialog)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressTextEdit = QtWidgets.QTextEdit(Dialog)
        self.addressTextEdit.setObjectName("addressTextEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.addressTextEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(148, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.nameLabel.setText(_translate("Dialog", "商品名"))
        self.describeLabel.setText(_translate("Dialog", "描述"))
        self.priceLabel.setText(_translate("Dialog", "价格"))
        self.discountLabel.setText(_translate("Dialog", "折扣"))
        self.sizeLabel.setText(_translate("Dialog", "尺码"))
        self.sizeLineEdit.setText(_translate("Dialog", "-"))
        self.WidLabel.setText(_translate("Dialog", "仓库号"))
        self.stockLabel.setText(_translate("Dialog", "库存数量"))
        self.addressLabel.setText(_translate("Dialog", "仓库地址"))
        self.pushButton.setText(_translate("Dialog", "确定"))
