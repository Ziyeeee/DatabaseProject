# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buyerUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(468, 417)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buyerTabWidget = QtWidgets.QTabWidget(Form)
        self.buyerTabWidget.setObjectName("buyerTabWidget")
        self.commodityTab = QtWidgets.QWidget()
        self.commodityTab.setObjectName("commodityTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.commodityTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commoditySearchLineEdit = QtWidgets.QLineEdit(self.commodityTab)
        self.commoditySearchLineEdit.setObjectName("commoditySearchLineEdit")
        self.horizontalLayout.addWidget(self.commoditySearchLineEdit)
        self.commoditySearchPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commoditySearchPushButton.setObjectName("commoditySearchPushButton")
        self.horizontalLayout.addWidget(self.commoditySearchPushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.commodityTableWidget = QtWidgets.QTableWidget(self.commodityTab)
        self.commodityTableWidget.setShowGrid(True)
        self.commodityTableWidget.setCornerButtonEnabled(True)
        self.commodityTableWidget.setRowCount(3)
        self.commodityTableWidget.setColumnCount(5)
        self.commodityTableWidget.setObjectName("commodityTableWidget")
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
        self.commodityTableWidget.horizontalHeader().setVisible(False)
        self.commodityTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.commodityTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.commodityTableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.commodityTableWidget.verticalHeader().setVisible(False)
        self.commodityTableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.commodityTableWidget.verticalHeader().setDefaultSectionSize(75)
        self.verticalLayout_8.addWidget(self.commodityTableWidget)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.commodityPageLabel = QtWidgets.QLabel(self.commodityTab)
        self.commodityPageLabel.setObjectName("commodityPageLabel")
        self.horizontalLayout_17.addWidget(self.commodityPageLabel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.addCartPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.addCartPushButton.setObjectName("addCartPushButton")
        self.horizontalLayout_15.addWidget(self.addCartPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.commodityLastPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityLastPushButton.setObjectName("commodityLastPushButton")
        self.horizontalLayout_15.addWidget(self.commodityLastPushButton)
        self.commodityNextPushButton = QtWidgets.QPushButton(self.commodityTab)
        self.commodityNextPushButton.setObjectName("commodityNextPushButton")
        self.horizontalLayout_15.addWidget(self.commodityNextPushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.buyerTabWidget.addTab(self.commodityTab, "")
        self.cartTab = QtWidgets.QWidget()
        self.cartTab.setObjectName("cartTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.cartTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cartWidget = QtWidgets.QWidget(self.cartTab)
        self.cartWidget.setObjectName("cartWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.cartWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cartSnameLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartSnameLabel.setObjectName("cartSnameLabel")
        self.horizontalLayout_12.addWidget(self.cartSnameLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.cartRefreshPushButton = QtWidgets.QPushButton(self.cartWidget)
        self.cartRefreshPushButton.setObjectName("cartRefreshPushButton")
        self.horizontalLayout_12.addWidget(self.cartRefreshPushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.cartCnameLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartCnameLabel.setObjectName("cartCnameLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cartCnameLabel)
        self.cartDescribeTextBrowser = QtWidgets.QTextBrowser(self.cartWidget)
        self.cartDescribeTextBrowser.setMaximumSize(QtCore.QSize(16777215, 80))
        self.cartDescribeTextBrowser.setObjectName("cartDescribeTextBrowser")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cartDescribeTextBrowser)
        self.verticalLayout_6.addLayout(self.formLayout_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(27, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.cartSize = QtWidgets.QLabel(self.cartWidget)
        self.cartSize.setObjectName("cartSize")
        self.horizontalLayout_13.addWidget(self.cartSize)
        self.cartSizeLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartSizeLabel.setObjectName("cartSizeLabel")
        self.horizontalLayout_13.addWidget(self.cartSizeLabel)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.cartNum = QtWidgets.QLabel(self.cartWidget)
        self.cartNum.setObjectName("cartNum")
        self.horizontalLayout_13.addWidget(self.cartNum)
        self.cartNumLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartNumLabel.setObjectName("cartNumLabel")
        self.horizontalLayout_13.addWidget(self.cartNumLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.cartPrice = QtWidgets.QLabel(self.cartWidget)
        self.cartPrice.setObjectName("cartPrice")
        self.horizontalLayout_14.addWidget(self.cartPrice)
        self.cartPriseLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartPriseLabel.setObjectName("cartPriseLabel")
        self.horizontalLayout_14.addWidget(self.cartPriseLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem10)
        self.cartPageLabel = QtWidgets.QLabel(self.cartWidget)
        self.cartPageLabel.setObjectName("cartPageLabel")
        self.horizontalLayout_16.addWidget(self.cartPageLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.verticalLayout_7.addWidget(self.cartWidget)
        spacerItem11 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cartBuyPushButton = QtWidgets.QPushButton(self.cartTab)
        self.cartBuyPushButton.setObjectName("cartBuyPushButton")
        self.horizontalLayout_11.addWidget(self.cartBuyPushButton)
        self.cartDeletePushButton = QtWidgets.QPushButton(self.cartTab)
        self.cartDeletePushButton.setObjectName("cartDeletePushButton")
        self.horizontalLayout_11.addWidget(self.cartDeletePushButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem13)
        self.cartLastPagePushButton = QtWidgets.QPushButton(self.cartTab)
        self.cartLastPagePushButton.setObjectName("cartLastPagePushButton")
        self.horizontalLayout_11.addWidget(self.cartLastPagePushButton)
        self.cartNextPagePushButton = QtWidgets.QPushButton(self.cartTab)
        self.cartNextPagePushButton.setObjectName("cartNextPagePushButton")
        self.horizontalLayout_11.addWidget(self.cartNextPagePushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.buyerTabWidget.addTab(self.cartTab, "")
        self.orderTab = QtWidgets.QWidget()
        self.orderTab.setObjectName("orderTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.orderTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem14)
        self.orderRefreshPushButton = QtWidgets.QPushButton(self.orderTab)
        self.orderRefreshPushButton.setObjectName("orderRefreshPushButton")
        self.horizontalLayout_18.addWidget(self.orderRefreshPushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.orderWidget = QtWidgets.QWidget(self.orderTab)
        self.orderWidget.setObjectName("orderWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.orderWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.orderSnameLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderSnameLabel.setObjectName("orderSnameLabel")
        self.horizontalLayout_5.addWidget(self.orderSnameLabel)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.orderIdLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderIdLabel.setObjectName("orderIdLabel")
        self.horizontalLayout_5.addWidget(self.orderIdLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.orderCnameLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderCnameLabel.setObjectName("orderCnameLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.orderCnameLabel)
        self.orderDescribeTextBrowser = QtWidgets.QTextBrowser(self.orderWidget)
        self.orderDescribeTextBrowser.setMaximumSize(QtCore.QSize(16777215, 80))
        self.orderDescribeTextBrowser.setObjectName("orderDescribeTextBrowser")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.orderDescribeTextBrowser)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(27, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.orderSize = QtWidgets.QLabel(self.orderWidget)
        self.orderSize.setObjectName("orderSize")
        self.horizontalLayout_6.addWidget(self.orderSize)
        self.orderSizeLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderSizeLabel.setObjectName("orderSizeLabel")
        self.horizontalLayout_6.addWidget(self.orderSizeLabel)
        spacerItem17 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.orderNum = QtWidgets.QLabel(self.orderWidget)
        self.orderNum.setObjectName("orderNum")
        self.horizontalLayout_6.addWidget(self.orderNum)
        self.orderNumLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderNumLabel.setObjectName("orderNumLabel")
        self.horizontalLayout_6.addWidget(self.orderNumLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.orderPrice = QtWidgets.QLabel(self.orderWidget)
        self.orderPrice.setObjectName("orderPrice")
        self.horizontalLayout_7.addWidget(self.orderPrice)
        self.orderPriceLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderPriceLabel.setObjectName("orderPriceLabel")
        self.horizontalLayout_7.addWidget(self.orderPriceLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem20)
        self.orderStatusLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderStatusLabel.setObjectName("orderStatusLabel")
        self.horizontalLayout_8.addWidget(self.orderStatusLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem21)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.orderPageLabel = QtWidgets.QLabel(self.orderWidget)
        self.orderPageLabel.setObjectName("orderPageLabel")
        self.horizontalLayout_9.addWidget(self.orderPageLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addWidget(self.orderWidget)
        spacerItem24 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem25)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.orderDeletePushButton = QtWidgets.QPushButton(self.orderTab)
        self.orderDeletePushButton.setObjectName("orderDeletePushButton")
        self.horizontalLayout_10.addWidget(self.orderDeletePushButton)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem26)
        self.orderLastPagePushButton = QtWidgets.QPushButton(self.orderTab)
        self.orderLastPagePushButton.setObjectName("orderLastPagePushButton")
        self.horizontalLayout_10.addWidget(self.orderLastPagePushButton)
        self.orderNextPagePushButton = QtWidgets.QPushButton(self.orderTab)
        self.orderNextPagePushButton.setObjectName("orderNextPagePushButton")
        self.horizontalLayout_10.addWidget(self.orderNextPagePushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.buyerTabWidget.addTab(self.orderTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.infoTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem27 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem27)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem28)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem29)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Bname = QtWidgets.QLabel(self.infoTab)
        self.Bname.setObjectName("Bname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Bname)
        self.credit = QtWidgets.QLabel(self.infoTab)
        self.credit.setObjectName("credit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.credit)
        self.infoCreditLabel = QtWidgets.QLabel(self.infoTab)
        self.infoCreditLabel.setObjectName("infoCreditLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infoCreditLabel)
        self.infoBnameLabel = QtWidgets.QLabel(self.infoTab)
        self.infoBnameLabel.setObjectName("infoBnameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infoBnameLabel)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem30)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem31)
        self.frame = QtWidgets.QFrame(self.infoTab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Recipient = QtWidgets.QLabel(self.groupBox)
        self.Recipient.setObjectName("Recipient")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Recipient)
        self.infoRnameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.infoRnameLineEdit.setObjectName("infoRnameLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infoRnameLineEdit)
        self.Tel = QtWidgets.QLabel(self.groupBox)
        self.Tel.setObjectName("Tel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Tel)
        self.infoTelLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.infoTelLineEdit.setObjectName("infoTelLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infoTelLineEdit)
        self.address = QtWidgets.QLabel(self.groupBox)
        self.address.setObjectName("address")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.address)
        self.infoAddressTextBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.infoAddressTextBrowser.setMaximumSize(QtCore.QSize(1000, 80))
        self.infoAddressTextBrowser.setReadOnly(False)
        self.infoAddressTextBrowser.setObjectName("infoAddressTextBrowser")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.infoAddressTextBrowser)
        self.postcode = QtWidgets.QLabel(self.groupBox)
        self.postcode.setObjectName("postcode")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.postcode)
        self.infoPostcodeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.infoPostcodeLineEdit.setObjectName("infoPostcodeLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.infoPostcodeLineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem32)
        self.infoPageLabel = QtWidgets.QLabel(self.groupBox)
        self.infoPageLabel.setObjectName("infoPageLabel")
        self.horizontalLayout_4.addWidget(self.infoPageLabel)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem33)
        self.infoRefreshPushButton = QtWidgets.QPushButton(self.groupBox)
        self.infoRefreshPushButton.setObjectName("infoRefreshPushButton")
        self.horizontalLayout_20.addWidget(self.infoRefreshPushButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infoAddPushButton = QtWidgets.QPushButton(self.frame)
        self.infoAddPushButton.setObjectName("infoAddPushButton")
        self.horizontalLayout_2.addWidget(self.infoAddPushButton)
        self.infoUpdatePushButton = QtWidgets.QPushButton(self.frame)
        self.infoUpdatePushButton.setObjectName("infoUpdatePushButton")
        self.horizontalLayout_2.addWidget(self.infoUpdatePushButton)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem34)
        self.infoLastPagePushButton = QtWidgets.QPushButton(self.frame)
        self.infoLastPagePushButton.setObjectName("infoLastPagePushButton")
        self.horizontalLayout_2.addWidget(self.infoLastPagePushButton)
        self.infoNextPagePushButton = QtWidgets.QPushButton(self.frame)
        self.infoNextPagePushButton.setObjectName("infoNextPagePushButton")
        self.horizontalLayout_2.addWidget(self.infoNextPagePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem35)
        self.buyerTabWidget.addTab(self.infoTab, "")
        self.verticalLayout_3.addWidget(self.buyerTabWidget)

        self.retranslateUi(Form)
        self.buyerTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.commoditySearchPushButton.setText(_translate("Form", "搜索/刷新"))
        self.commodityTableWidget.setSortingEnabled(False)
        item = self.commodityTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "选择"))
        item = self.commodityTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "品名"))
        item = self.commodityTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "描述"))
        item = self.commodityTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "尺寸"))
        item = self.commodityTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "价格"))
        self.commodityPageLabel.setText(_translate("Form", "“页码”"))
        self.addCartPushButton.setText(_translate("Form", "加入购物车"))
        self.commodityLastPushButton.setText(_translate("Form", "上一页"))
        self.commodityNextPushButton.setText(_translate("Form", "下一页"))
        self.buyerTabWidget.setTabText(self.buyerTabWidget.indexOf(self.commodityTab), _translate("Form", "商品"))
        self.cartSnameLabel.setText(_translate("Form", "“商店名”"))
        self.cartRefreshPushButton.setText(_translate("Form", "刷新"))
        self.cartCnameLabel.setText(_translate("Form", "“商品名”"))
        self.cartSize.setText(_translate("Form", "尺码："))
        self.cartSizeLabel.setText(_translate("Form", "“尺码”"))
        self.cartNum.setText(_translate("Form", "数量："))
        self.cartNumLabel.setText(_translate("Form", "“数量”"))
        self.cartPrice.setText(_translate("Form", "价格："))
        self.cartPriseLabel.setText(_translate("Form", "“价格”"))
        self.cartPageLabel.setText(_translate("Form", "“页码”"))
        self.cartBuyPushButton.setText(_translate("Form", "购买"))
        self.cartDeletePushButton.setText(_translate("Form", "删除"))
        self.cartLastPagePushButton.setText(_translate("Form", "上一页"))
        self.cartNextPagePushButton.setText(_translate("Form", "下一页"))
        self.buyerTabWidget.setTabText(self.buyerTabWidget.indexOf(self.cartTab), _translate("Form", "购物车"))
        self.orderRefreshPushButton.setText(_translate("Form", "刷新"))
        self.orderSnameLabel.setText(_translate("Form", "“商店名”"))
        self.orderIdLabel.setText(_translate("Form", "“订单号”"))
        self.orderCnameLabel.setText(_translate("Form", "“商品名”"))
        self.orderSize.setText(_translate("Form", "尺码："))
        self.orderSizeLabel.setText(_translate("Form", "“尺码”"))
        self.orderNum.setText(_translate("Form", "数量："))
        self.orderNumLabel.setText(_translate("Form", "“数量”"))
        self.orderPrice.setText(_translate("Form", "价格："))
        self.orderPriceLabel.setText(_translate("Form", "“价格”"))
        self.orderStatusLabel.setText(_translate("Form", "“状态”"))
        self.orderPageLabel.setText(_translate("Form", "“页码”"))
        self.orderDeletePushButton.setText(_translate("Form", "删除"))
        self.orderLastPagePushButton.setText(_translate("Form", "上一页"))
        self.orderNextPagePushButton.setText(_translate("Form", "下一页"))
        self.buyerTabWidget.setTabText(self.buyerTabWidget.indexOf(self.orderTab), _translate("Form", "订单"))
        self.Bname.setText(_translate("Form", "昵称"))
        self.credit.setText(_translate("Form", "信誉度"))
        self.infoCreditLabel.setText(_translate("Form", "TextLabel"))
        self.infoBnameLabel.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "地址簿"))
        self.Recipient.setText(_translate("Form", "收件人"))
        self.Tel.setText(_translate("Form", "电话"))
        self.address.setText(_translate("Form", "地址"))
        self.postcode.setText(_translate("Form", "邮编"))
        self.infoPageLabel.setText(_translate("Form", "“页码”"))
        self.infoRefreshPushButton.setText(_translate("Form", "刷新"))
        self.infoAddPushButton.setText(_translate("Form", "添加"))
        self.infoUpdatePushButton.setText(_translate("Form", "修改"))
        self.infoLastPagePushButton.setText(_translate("Form", "上一页"))
        self.infoNextPagePushButton.setText(_translate("Form", "下一页"))
        self.buyerTabWidget.setTabText(self.buyerTabWidget.indexOf(self.infoTab), _translate("Form", "个人信息"))

