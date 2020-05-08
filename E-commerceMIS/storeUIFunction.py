from PyQt5 import QtWidgets
from storeUI import Ui_Form
import pymysql
import sys
from addCommodityDialogFunction import AddCommodityDialog


class StoreUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self, db, dbcursor, Sid):
        super(StoreUI, self).__init__()
        self.setupUi(self)
        self.db = db
        self.dbcursor = dbcursor
        self.Sid = Sid
        self.page = 1

        self.commodityTableWidget.setColumnWidth(0, 40)
        self.commodityTableWidget.setColumnWidth(1, 80)

        self.widget1 = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.checkBox1 = QtWidgets.QCheckBox(self.widget1)
        self.horizontalLayout.addWidget(self.checkBox1)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.commodityTableWidget.setCellWidget(0, 0, self.widget1)
        self.textBrowser1 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(0, 2, self.textBrowser1)
        self.textBrowser4 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(0, 7, self.textBrowser4)

        self.widget2 = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkBox2 = QtWidgets.QCheckBox(self.widget2)
        self.horizontalLayout.addWidget(self.checkBox2)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.commodityTableWidget.setCellWidget(1, 0, self.widget2)
        self.textBrowser2 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(1, 2, self.textBrowser2)
        self.textBrowser5 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(1, 7, self.textBrowser5)

        self.widget3 = QtWidgets.QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.checkBox3 = QtWidgets.QCheckBox(self.widget3)
        self.horizontalLayout.addWidget(self.checkBox3)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.commodityTableWidget.setCellWidget(2, 0, self.widget3)
        self.textBrowser3 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(2, 2, self.textBrowser3)
        self.textBrowser6 = QtWidgets.QTextBrowser()
        self.commodityTableWidget.setCellWidget(2, 7, self.textBrowser6)

        self.sql = 'select Cname, Cdescribe, price, discount, commodity.stockSize, stock, address ' \
                   'from commodity, warehouse where commodity.Sid = \"' + self.Sid \
                   + '\" and commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize;'
        self.dbcursor.execute(self.sql)
        self.data = self.dbcursor.fetchall()

        self.commodityPageLabel.setText(str(self.page))
        self.enablePagePushButton()
        self.enableFuncPushButton()
        self.showData()

        self.commodityAddPushButton.clicked.connect(self.addCommodity)
        self.checkBox1.stateChanged.connect(self.enableFuncPushButton)
        self.checkBox2.stateChanged.connect(self.enableFuncPushButton)
        self.checkBox3.stateChanged.connect(self.enableFuncPushButton)

    def addCommodity(self):
        self.addCommodityDialog = AddCommodityDialog(self.db, self.dbcursor, self.Sid)
        self.addCommodityDialog.show()

    def enablePagePushButton(self):
        if self.page == 1:
            self.commodityLastPushButton.setEnabled(False)
        else:
            self.commodityLastPushButton.setEnabled(True)

        if self.page * 3 >= len(self.data):
            self.commodityNextPushButton.setEnabled(False)
        else:
            self.commodityNextPushButton.setEnabled(True)

    def enableFuncPushButton(self):
        if self.checkBox1.isChecked() or self.checkBox2.isChecked() or self.checkBox3.isChecked():
            self.commodityAddPushButton.setEnabled(True)
            self.commodityUpdatePushButton.setEnabled(True)
            self.commodityDeletePushButton.setEnabled(True)
        else:
            self.commodityAddPushButton.setEnabled(False)
            self.commodityUpdatePushButton.setEnabled(False)
            self.commodityDeletePushButton.setEnabled(False)

    def showData(self):
        print(self.data)
        for i in range(0, 3):
            for j in [0, 2, 3, 4, 5, 6]:
                self.commodityTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.data[self.page * 3 - 3 + i][j])))
            if i == 0:
                self.textBrowser1.setText(self.data[self.page * 3 - 3 + i][1])
                self.textBrowser4.setText(self.data[self.page * 3 - 3 + i][7])
            elif i == 1:
                self.textBrowser2.setText(self.data[self.page * 3 - 3 + i][1])
                self.textBrowser5.setText(self.data[self.page * 3 - 3 + i][7])
            elif i == 2:
                self.textBrowser3.setText(self.data[self.page * 3 - 3 + i][2])
                self.textBrowser6.setText(self.data[self.page * 3 - 3 + i][7])



if __name__ == "__main__":
    db = pymysql.connect("localhost", "root", "130e340", "e-commerce")
    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    storeUI = StoreUI(db, cursor, "001")
    storeUI.show()
    sys.exit(app.exec_())
