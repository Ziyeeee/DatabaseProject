# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectBox = QtWidgets.QGroupBox(self.centralwidget)
        self.connectBox.setEnabled(True)
        self.connectBox.setGeometry(QtCore.QRect(10, 10, 231, 171))
        self.connectBox.setMouseTracking(False)
        self.connectBox.setCheckable(False)
        self.connectBox.setObjectName("connectBox")
        self.layoutWidget = QtWidgets.QWidget(self.connectBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 211, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hostLable = QtWidgets.QLabel(self.layoutWidget)
        self.hostLable.setObjectName("hostLable")
        self.gridLayout_3.addWidget(self.hostLable, 0, 0, 1, 1)
        self.hostLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.hostLineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.gridLayout_3.addWidget(self.hostLineEdit, 0, 1, 1, 1)
        self.userNameLable = QtWidgets.QLabel(self.layoutWidget)
        self.userNameLable.setObjectName("userNameLable")
        self.gridLayout_3.addWidget(self.userNameLable, 1, 0, 1, 1)
        self.userNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.userNameLineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.gridLayout_3.addWidget(self.userNameLineEdit, 1, 1, 1, 1)
        self.keyLable = QtWidgets.QLabel(self.layoutWidget)
        self.keyLable.setObjectName("keyLable")
        self.gridLayout_3.addWidget(self.keyLable, 2, 0, 1, 1)
        self.keyLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.keyLineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.keyLineEdit.setInputMask("")
        self.keyLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.gridLayout_3.addWidget(self.keyLineEdit, 2, 1, 1, 1)
        self.databaseLable = QtWidgets.QLabel(self.layoutWidget)
        self.databaseLable.setObjectName("databaseLable")
        self.gridLayout_3.addWidget(self.databaseLable, 3, 0, 1, 1)
        self.databaseLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.databaseLineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.databaseLineEdit.setObjectName("databaseLineEdit")
        self.gridLayout_3.addWidget(self.databaseLineEdit, 3, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.connectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout_4.addWidget(self.connectButton, 1, 0, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout_4.addWidget(self.disconnectButton, 1, 1, 1, 1)
        self.sqlBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sqlBox.setGeometry(QtCore.QRect(250, 10, 491, 171))
        self.sqlBox.setObjectName("sqlBox")
        self.sqlTextBrowser = QtWidgets.QTextBrowser(self.sqlBox)
        self.sqlTextBrowser.setEnabled(True)
        self.sqlTextBrowser.setGeometry(QtCore.QRect(10, 20, 471, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.sqlTextBrowser.setFont(font)
        self.sqlTextBrowser.setObjectName("sqlTextBrowser")
        self.resultBox = QtWidgets.QGroupBox(self.centralwidget)
        self.resultBox.setGeometry(QtCore.QRect(250, 190, 491, 301))
        self.resultBox.setObjectName("resultBox")
        self.resulTableWidget = QtWidgets.QTableWidget(self.resultBox)
        self.resulTableWidget.setGeometry(QtCore.QRect(10, 20, 471, 271))
        self.resulTableWidget.setDragEnabled(False)
        self.resulTableWidget.setAlternatingRowColors(True)
        self.resulTableWidget.setRowCount(0)
        self.resulTableWidget.setColumnCount(0)
        self.resulTableWidget.setObjectName("resulTableWidget")
        self.resulTableWidget.horizontalHeader().setVisible(True)
        self.resulTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.resulTableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.resulTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.resulTableWidget.horizontalHeader().setStretchLastSection(False)
        self.resulTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.resulTableWidget.verticalHeader().setStretchLastSection(False)
        self.functionTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.functionTabWidget.setGeometry(QtCore.QRect(10, 190, 231, 301))
        self.functionTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.functionTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.functionTabWidget.setUsesScrollButtons(True)
        self.functionTabWidget.setDocumentMode(False)
        self.functionTabWidget.setTabsClosable(False)
        self.functionTabWidget.setMovable(False)
        self.functionTabWidget.setObjectName("functionTabWidget")
        self.selectTab = QtWidgets.QWidget()
        self.selectTab.setObjectName("selectTab")
        self.layoutWidget1 = QtWidgets.QWidget(self.selectTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 211, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.superssnLineEditSelect = QtWidgets.QLineEdit(self.layoutWidget1)
        self.superssnLineEditSelect.setObjectName("superssnLineEditSelect")
        self.gridLayout_2.addWidget(self.superssnLineEditSelect, 3, 1, 1, 1)
        self.superssnCheckBoxSelect = QtWidgets.QCheckBox(self.layoutWidget1)
        self.superssnCheckBoxSelect.setObjectName("superssnCheckBoxSelect")
        self.gridLayout_2.addWidget(self.superssnCheckBoxSelect, 3, 0, 1, 1)
        self.dnoLineEditSelect = QtWidgets.QLineEdit(self.layoutWidget1)
        self.dnoLineEditSelect.setObjectName("dnoLineEditSelect")
        self.gridLayout_2.addWidget(self.dnoLineEditSelect, 4, 1, 1, 1)
        self.addressLineEditSelect = QtWidgets.QLineEdit(self.layoutWidget1)
        self.addressLineEditSelect.setObjectName("addressLineEditSelect")
        self.gridLayout_2.addWidget(self.addressLineEditSelect, 2, 1, 1, 1)
        self.addressCheckBoxSelect = QtWidgets.QCheckBox(self.layoutWidget1)
        self.addressCheckBoxSelect.setObjectName("addressCheckBoxSelect")
        self.gridLayout_2.addWidget(self.addressCheckBoxSelect, 2, 0, 1, 1)
        self.dnoCheckBoxSelect = QtWidgets.QCheckBox(self.layoutWidget1)
        self.dnoCheckBoxSelect.setObjectName("dnoCheckBoxSelect")
        self.gridLayout_2.addWidget(self.dnoCheckBoxSelect, 4, 0, 1, 1)
        self.enameCheckBoxSelect = QtWidgets.QCheckBox(self.layoutWidget1)
        self.enameCheckBoxSelect.setObjectName("enameCheckBoxSelect")
        self.gridLayout_2.addWidget(self.enameCheckBoxSelect, 0, 0, 1, 1)
        self.essnCheckBoxSelect = QtWidgets.QCheckBox(self.layoutWidget1)
        self.essnCheckBoxSelect.setObjectName("essnCheckBoxSelect")
        self.gridLayout_2.addWidget(self.essnCheckBoxSelect, 1, 0, 1, 1)
        self.essnLineEditSelect = QtWidgets.QLineEdit(self.layoutWidget1)
        self.essnLineEditSelect.setObjectName("essnLineEditSelect")
        self.gridLayout_2.addWidget(self.essnLineEditSelect, 1, 1, 1, 1)
        self.enameLineEditSelect = QtWidgets.QLineEdit(self.layoutWidget1)
        self.enameLineEditSelect.setObjectName("enameLineEditSelect")
        self.gridLayout_2.addWidget(self.enameLineEditSelect, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.doButtonSelect = QtWidgets.QPushButton(self.layoutWidget1)
        self.doButtonSelect.setObjectName("doButtonSelect")
        self.gridLayout_5.addWidget(self.doButtonSelect, 1, 0, 1, 1)
        self.clearButtonSelect = QtWidgets.QPushButton(self.layoutWidget1)
        self.clearButtonSelect.setObjectName("clearButtonSelect")
        self.gridLayout_5.addWidget(self.clearButtonSelect, 1, 1, 1, 1)
        self.functionTabWidget.addTab(self.selectTab, "")
        self.insertTab = QtWidgets.QWidget()
        self.insertTab.setObjectName("insertTab")
        self.layoutWidget2 = QtWidgets.QWidget(self.insertTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 1, 211, 271))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.enameLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.enameLabelInsert.setObjectName("enameLabelInsert")
        self.gridLayout_8.addWidget(self.enameLabelInsert, 0, 0, 1, 1)
        self.enameLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.enameLineEditInsert.setObjectName("enameLineEditInsert")
        self.gridLayout_8.addWidget(self.enameLineEditInsert, 0, 1, 1, 1)
        self.essnLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.essnLabelInsert.setObjectName("essnLabelInsert")
        self.gridLayout_8.addWidget(self.essnLabelInsert, 1, 0, 1, 1)
        self.essnLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.essnLineEditInsert.setObjectName("essnLineEditInsert")
        self.gridLayout_8.addWidget(self.essnLineEditInsert, 1, 1, 1, 1)
        self.addressLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.addressLabelInsert.setObjectName("addressLabelInsert")
        self.gridLayout_8.addWidget(self.addressLabelInsert, 2, 0, 1, 1)
        self.addressLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.addressLineEditInsert.setObjectName("addressLineEditInsert")
        self.gridLayout_8.addWidget(self.addressLineEditInsert, 2, 1, 1, 1)
        self.salaryLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.salaryLabelInsert.setObjectName("salaryLabelInsert")
        self.gridLayout_8.addWidget(self.salaryLabelInsert, 3, 0, 1, 1)
        self.salaryLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.salaryLineEditInsert.setObjectName("salaryLineEditInsert")
        self.gridLayout_8.addWidget(self.salaryLineEditInsert, 3, 1, 1, 1)
        self.superssnLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.superssnLabelInsert.setObjectName("superssnLabelInsert")
        self.gridLayout_8.addWidget(self.superssnLabelInsert, 4, 0, 1, 1)
        self.superssnLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.superssnLineEditInsert.setObjectName("superssnLineEditInsert")
        self.gridLayout_8.addWidget(self.superssnLineEditInsert, 4, 1, 1, 1)
        self.dnoLabelInsert = QtWidgets.QLabel(self.layoutWidget2)
        self.dnoLabelInsert.setObjectName("dnoLabelInsert")
        self.gridLayout_8.addWidget(self.dnoLabelInsert, 5, 0, 1, 1)
        self.dnoLineEditInsert = QtWidgets.QLineEdit(self.layoutWidget2)
        self.dnoLineEditInsert.setObjectName("dnoLineEditInsert")
        self.gridLayout_8.addWidget(self.dnoLineEditInsert, 5, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 2)
        self.clearButtonInsert = QtWidgets.QPushButton(self.layoutWidget2)
        self.clearButtonInsert.setObjectName("clearButtonInsert")
        self.gridLayout_9.addWidget(self.clearButtonInsert, 1, 1, 1, 1)
        self.doButtonInsert = QtWidgets.QPushButton(self.layoutWidget2)
        self.doButtonInsert.setObjectName("doButtonInsert")
        self.gridLayout_9.addWidget(self.doButtonInsert, 1, 0, 1, 1)
        self.functionTabWidget.addTab(self.insertTab, "")
        self.updateTab = QtWidgets.QWidget()
        self.updateTab.setObjectName("updateTab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.updateTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 211, 271))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.doButtonUpdate = QtWidgets.QPushButton(self.layoutWidget_2)
        self.doButtonUpdate.setObjectName("doButtonUpdate")
        self.gridLayout_10.addWidget(self.doButtonUpdate, 1, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.enameLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.enameLineEditUpdate.setObjectName("enameLineEditUpdate")
        self.gridLayout_11.addWidget(self.enameLineEditUpdate, 0, 1, 1, 1)
        self.essnLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.essnLineEditUpdate.setObjectName("essnLineEditUpdate")
        self.gridLayout_11.addWidget(self.essnLineEditUpdate, 1, 1, 1, 1)
        self.salaryLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.salaryLineEditUpdate.setObjectName("salaryLineEditUpdate")
        self.gridLayout_11.addWidget(self.salaryLineEditUpdate, 3, 1, 1, 1)
        self.addressLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.addressLineEditUpdate.setObjectName("addressLineEditUpdate")
        self.gridLayout_11.addWidget(self.addressLineEditUpdate, 2, 1, 1, 1)
        self.dnoLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.dnoLineEditUpdate.setObjectName("dnoLineEditUpdate")
        self.gridLayout_11.addWidget(self.dnoLineEditUpdate, 5, 1, 1, 1)
        self.superssnLineEditUpdate = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.superssnLineEditUpdate.setObjectName("superssnLineEditUpdate")
        self.gridLayout_11.addWidget(self.superssnLineEditUpdate, 4, 1, 1, 1)
        self.enameCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.enameCheckBoxUpdate.setObjectName("enameCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.enameCheckBoxUpdate, 0, 0, 1, 1)
        self.essnCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.essnCheckBoxUpdate.setObjectName("essnCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.essnCheckBoxUpdate, 1, 0, 1, 1)
        self.addressCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.addressCheckBoxUpdate.setObjectName("addressCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.addressCheckBoxUpdate, 2, 0, 1, 1)
        self.salaryCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.salaryCheckBoxUpdate.setObjectName("salaryCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.salaryCheckBoxUpdate, 3, 0, 1, 1)
        self.superssnCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.superssnCheckBoxUpdate.setObjectName("superssnCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.superssnCheckBoxUpdate, 4, 0, 1, 1)
        self.dnoCheckBoxUpdate = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.dnoCheckBoxUpdate.setObjectName("dnoCheckBoxUpdate")
        self.gridLayout_11.addWidget(self.dnoCheckBoxUpdate, 5, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_11, 0, 0, 1, 2)
        self.clearButtonUpdate = QtWidgets.QPushButton(self.layoutWidget_2)
        self.clearButtonUpdate.setObjectName("clearButtonUpdate")
        self.gridLayout_10.addWidget(self.clearButtonUpdate, 1, 1, 1, 1)
        self.functionTabWidget.addTab(self.updateTab, "")
        self.deleteTab = QtWidgets.QWidget()
        self.deleteTab.setObjectName("deleteTab")
        self.layoutWidget3 = QtWidgets.QWidget(self.deleteTab)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 1, 211, 271))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.enameLineEditDelete = QtWidgets.QLineEdit(self.layoutWidget3)
        self.enameLineEditDelete.setObjectName("enameLineEditDelete")
        self.gridLayout_7.addWidget(self.enameLineEditDelete, 0, 1, 1, 1)
        self.essnCheckBoxDelete = QtWidgets.QCheckBox(self.layoutWidget3)
        self.essnCheckBoxDelete.setObjectName("essnCheckBoxDelete")
        self.gridLayout_7.addWidget(self.essnCheckBoxDelete, 1, 0, 1, 1)
        self.addressLineEditDelete = QtWidgets.QLineEdit(self.layoutWidget3)
        self.addressLineEditDelete.setObjectName("addressLineEditDelete")
        self.gridLayout_7.addWidget(self.addressLineEditDelete, 2, 1, 1, 1)
        self.enameCheckBoxDelete = QtWidgets.QCheckBox(self.layoutWidget3)
        self.enameCheckBoxDelete.setObjectName("enameCheckBoxDelete")
        self.gridLayout_7.addWidget(self.enameCheckBoxDelete, 0, 0, 1, 1)
        self.essnLineEditDelete = QtWidgets.QLineEdit(self.layoutWidget3)
        self.essnLineEditDelete.setObjectName("essnLineEditDelete")
        self.gridLayout_7.addWidget(self.essnLineEditDelete, 1, 1, 1, 1)
        self.addressCheckBoxDelete = QtWidgets.QCheckBox(self.layoutWidget3)
        self.addressCheckBoxDelete.setObjectName("addressCheckBoxDelete")
        self.gridLayout_7.addWidget(self.addressCheckBoxDelete, 2, 0, 1, 1)
        self.superssnCheckBoxDelete = QtWidgets.QCheckBox(self.layoutWidget3)
        self.superssnCheckBoxDelete.setObjectName("superssnCheckBoxDelete")
        self.gridLayout_7.addWidget(self.superssnCheckBoxDelete, 3, 0, 1, 1)
        self.superssnLineEditDelete = QtWidgets.QLineEdit(self.layoutWidget3)
        self.superssnLineEditDelete.setObjectName("superssnLineEditDelete")
        self.gridLayout_7.addWidget(self.superssnLineEditDelete, 3, 1, 1, 1)
        self.dnoLineEditDelete = QtWidgets.QLineEdit(self.layoutWidget3)
        self.dnoLineEditDelete.setObjectName("dnoLineEditDelete")
        self.gridLayout_7.addWidget(self.dnoLineEditDelete, 4, 1, 1, 1)
        self.dnoCheckBoxDelete = QtWidgets.QCheckBox(self.layoutWidget3)
        self.dnoCheckBoxDelete.setObjectName("dnoCheckBoxDelete")
        self.gridLayout_7.addWidget(self.dnoCheckBoxDelete, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 2)
        self.doButtonDelete = QtWidgets.QPushButton(self.layoutWidget3)
        self.doButtonDelete.setObjectName("doButtonDelete")
        self.gridLayout.addWidget(self.doButtonDelete, 1, 0, 1, 1)
        self.clearButtonDelete = QtWidgets.QPushButton(self.layoutWidget3)
        self.clearButtonDelete.setObjectName("clearButtonDelete")
        self.gridLayout.addWidget(self.clearButtonDelete, 1, 1, 1, 1)
        self.functionTabWidget.addTab(self.deleteTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.functionTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectBox.setTitle(_translate("MainWindow", "连接数据库"))
        self.hostLable.setText(_translate("MainWindow", "主机"))
        self.userNameLable.setText(_translate("MainWindow", "用户名"))
        self.keyLable.setText(_translate("MainWindow", "密码"))
        self.databaseLable.setText(_translate("MainWindow", "数据库名"))
        self.connectButton.setText(_translate("MainWindow", "连接"))
        self.disconnectButton.setText(_translate("MainWindow", "断开"))
        self.sqlBox.setTitle(_translate("MainWindow", "SQL语句"))
        self.resultBox.setTitle(_translate("MainWindow", "结果"))
        self.superssnCheckBoxSelect.setText(_translate("MainWindow", "领导编号"))
        self.addressCheckBoxSelect.setText(_translate("MainWindow", "地址"))
        self.dnoCheckBoxSelect.setText(_translate("MainWindow", "部门编号"))
        self.enameCheckBoxSelect.setText(_translate("MainWindow", "姓名"))
        self.essnCheckBoxSelect.setText(_translate("MainWindow", "编号"))
        self.doButtonSelect.setText(_translate("MainWindow", "执行"))
        self.clearButtonSelect.setText(_translate("MainWindow", "清空"))
        self.functionTabWidget.setTabText(self.functionTabWidget.indexOf(self.selectTab), _translate("MainWindow", "查询"))
        self.enameLabelInsert.setText(_translate("MainWindow", "姓名"))
        self.essnLabelInsert.setText(_translate("MainWindow", "编号"))
        self.addressLabelInsert.setText(_translate("MainWindow", "地址"))
        self.salaryLabelInsert.setText(_translate("MainWindow", "工资"))
        self.superssnLabelInsert.setText(_translate("MainWindow", "领导编号"))
        self.dnoLabelInsert.setText(_translate("MainWindow", "部门编号"))
        self.clearButtonInsert.setText(_translate("MainWindow", "清空"))
        self.doButtonInsert.setText(_translate("MainWindow", "执行"))
        self.functionTabWidget.setTabText(self.functionTabWidget.indexOf(self.insertTab), _translate("MainWindow", "插入"))
        self.doButtonUpdate.setText(_translate("MainWindow", "执行"))
        self.enameCheckBoxUpdate.setText(_translate("MainWindow", "姓名"))
        self.essnCheckBoxUpdate.setText(_translate("MainWindow", "编号"))
        self.addressCheckBoxUpdate.setText(_translate("MainWindow", "地址"))
        self.salaryCheckBoxUpdate.setText(_translate("MainWindow", "工资"))
        self.superssnCheckBoxUpdate.setText(_translate("MainWindow", "领导编号"))
        self.dnoCheckBoxUpdate.setText(_translate("MainWindow", "部门编号"))
        self.clearButtonUpdate.setText(_translate("MainWindow", "清空"))
        self.functionTabWidget.setTabText(self.functionTabWidget.indexOf(self.updateTab), _translate("MainWindow", "更新"))
        self.essnCheckBoxDelete.setText(_translate("MainWindow", "编号"))
        self.enameCheckBoxDelete.setText(_translate("MainWindow", "姓名"))
        self.addressCheckBoxDelete.setText(_translate("MainWindow", "地址"))
        self.superssnCheckBoxDelete.setText(_translate("MainWindow", "领导编号"))
        self.dnoCheckBoxDelete.setText(_translate("MainWindow", "部门编号"))
        self.doButtonDelete.setText(_translate("MainWindow", "执行"))
        self.clearButtonDelete.setText(_translate("MainWindow", "清空"))
        self.functionTabWidget.setTabText(self.functionTabWidget.indexOf(self.deleteTab), _translate("MainWindow", "删除"))

