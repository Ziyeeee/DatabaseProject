# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storeUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(483, 396)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.storeTabWidget = QtWidgets.QTabWidget(Form)
        self.storeTabWidget.setObjectName("storeTabWidget")
        self.commodityTab = QtWidgets.QWidget()
        self.commodityTab.setObjectName("commodityTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.commodityTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.commoditySearchLineEdit = QtWidgets.QLineEdit(self.commodityTab)
        self.commoditySearchLineEdit.setObjectName("commoditySearchLineEdit")
        self.horizontalLayout_4.addWidget(self.commoditySearchLineEdit)
        self.commoditySearchPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commoditySearchPushButton.setObjectName("commoditySearchPushButton")
        self.horizontalLayout_4.addWidget(self.commoditySearchPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.commodityTableWidget = QtWidgets.QTableWidget(self.commodityTab)
        self.commodityTableWidget.setObjectName("commodityTableWidget")
        self.commodityTableWidget.setColumnCount(7)
        self.commodityTableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.commodityTableWidget.setHorizontalHeaderItem(6, item)
        self.commodityTableWidget.horizontalHeader().setVisible(True)
        self.commodityTableWidget.verticalHeader().setVisible(False)
        self.commodityTableWidget.verticalHeader().setDefaultSectionSize(100)
        self.verticalLayout_2.addWidget(self.commodityTableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.commodityPageLabel = QtWidgets.QLabel(self.commodityTab)
        self.commodityPageLabel.setObjectName("commodityPageLabel")
        self.horizontalLayout.addWidget(self.commodityPageLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.commodityAddPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityAddPushButton.setObjectName("commodityAddPushButton")
        self.horizontalLayout_2.addWidget(self.commodityAddPushButton)
        self.commodityUpdatePushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityUpdatePushButton.setObjectName("commodityUpdatePushButton")
        self.horizontalLayout_2.addWidget(self.commodityUpdatePushButton)
        self.commodityDeletePushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityDeletePushButton.setObjectName("commodityDeletePushButton")
        self.horizontalLayout_2.addWidget(self.commodityDeletePushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.commodityLastPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityLastPushButton.setObjectName("commodityLastPushButton")
        self.horizontalLayout_3.addWidget(self.commodityLastPushButton)
        self.commodityNextPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityNextPushButton.setObjectName("commodityNextPushButton")
        self.horizontalLayout_3.addWidget(self.commodityNextPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.storeTabWidget.addTab(self.commodityTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.infoTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Sname = QtWidgets.QLabel(self.infoTab)
        self.Sname.setObjectName("Sname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Sname)
        self.infoSnameLabel = QtWidgets.QLabel(self.infoTab)
        self.infoSnameLabel.setObjectName("infoSnameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infoSnameLabel)
        self.credit = QtWidgets.QLabel(self.infoTab)
        self.credit.setObjectName("credit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.credit)
        self.infoCreditLabel = QtWidgets.QLabel(self.infoTab)
        self.infoCreditLabel.setObjectName("infoCreditLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infoCreditLabel)
        self.principal = QtWidgets.QLabel(self.infoTab)
        self.principal.setObjectName("principal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.principal)
        self.infoPrincipalLabel = QtWidgets.QLabel(self.infoTab)
        self.infoPrincipalLabel.setObjectName("infoPrincipalLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infoPrincipalLabel)
        self.Tel = QtWidgets.QLabel(self.infoTab)
        self.Tel.setObjectName("Tel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Tel)
        self.infoTelLabel = QtWidgets.QLabel(self.infoTab)
        self.infoTelLabel.setObjectName("infoTelLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.infoTelLabel)
        spacerItem6 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.sales = QtWidgets.QLabel(self.infoTab)
        self.sales.setObjectName("sales")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sales)
        self.infoSalesLabel = QtWidgets.QLabel(self.infoTab)
        self.infoSalesLabel.setObjectName("infoSalesLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.infoSalesLabel)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.infoUpdatePushButton = QtWidgets.QPushButton(self.infoTab)
        self.infoUpdatePushButton.setObjectName("infoUpdatePushButton")
        self.horizontalLayout_5.addWidget(self.infoUpdatePushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.storeTabWidget.addTab(self.infoTab, "")
        self.verticalLayout.addWidget(self.storeTabWidget)

        self.retranslateUi(Form)
        self.storeTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.commoditySearchPushButton.setText(_translate("Form", "搜索"))
        item = self.commodityTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新建行"))
        item = self.commodityTableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "新建行"))
        item = self.commodityTableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "新建行"))
        item = self.commodityTableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "新建行"))
        item = self.commodityTableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "新建行"))
        item = self.commodityTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.commodityTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "商品名"))
        item = self.commodityTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "描述"))
        item = self.commodityTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "原价"))
        item = self.commodityTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "折扣"))
        item = self.commodityTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "库存"))
        item = self.commodityTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "销量"))
        self.commodityPageLabel.setText(_translate("Form", "“页码”"))
        self.commodityAddPushButton.setText(_translate("Form", "添加"))
        self.commodityUpdatePushButton.setText(_translate("Form", "更改"))
        self.commodityDeletePushButton.setText(_translate("Form", "删除"))
        self.commodityLastPushButton.setText(_translate("Form", "上一页"))
        self.commodityNextPushButton.setText(_translate("Form", "下一页"))
        self.storeTabWidget.setTabText(self.storeTabWidget.indexOf(self.commodityTab), _translate("Form", "商品管理"))
        self.Sname.setText(_translate("Form", "店铺名"))
        self.infoSnameLabel.setText(_translate("Form", "TextLabel"))
        self.credit.setText(_translate("Form", "信誉度"))
        self.infoCreditLabel.setText(_translate("Form", "TextLabel"))
        self.principal.setText(_translate("Form", "负责人"))
        self.infoPrincipalLabel.setText(_translate("Form", "TextLabel"))
        self.Tel.setText(_translate("Form", "Tel"))
        self.infoTelLabel.setText(_translate("Form", "TextLabel"))
        self.sales.setText(_translate("Form", "销售额"))
        self.infoSalesLabel.setText(_translate("Form", "TextLabel"))
        self.infoUpdatePushButton.setText(_translate("Form", "修改信息"))
        self.storeTabWidget.setTabText(self.storeTabWidget.indexOf(self.infoTab), _translate("Form", "店铺信息"))

