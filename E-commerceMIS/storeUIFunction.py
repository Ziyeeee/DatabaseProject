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
        self.commodityTableWidget.setColumnWidth(2, 150)
        self.commodityTableWidget.setColumnWidth(3, 60)
        self.commodityTableWidget.setColumnWidth(4, 60)
        self.commodityTableWidget.setColumnWidth(5, 60)
        self.commodityTableWidget.setColumnWidth(6, 60)
        self.commodityTableWidget.setColumnWidth(7, 200)

        self.getAllData()

        self.initTable()

        self.commodityPageLabel.setText(str(self.page))
        self.reShow()

        self.sql = 'select Sname, Scredit, principal, Tel, ID_card ' \
                   'from store where Sid = \"' + self.Sid + '\";'
        self.dbcursor.execute(self.sql)
        self.info = self.dbcursor.fetchone()

        self.SnameLineEdit.setText(self.info[0])
        self.creditLabel.setText(str(self.info[1]))
        self.principalLineEdit.setText(self.info[2])
        self.TelLineEdit.setText(self.info[3])
        self.IDLineEdit.setText(self.info[4])

        self.commodityAddPushButton.clicked.connect(self.addCommodity)
        self.commodityUpdatePushButton.clicked.connect(self.updataCommodity)
        self.commodityDeletePushButton.clicked.connect(self.deleteCommodity)
        self.commoditySearchPushButton.clicked.connect(self.searchCommodity)

        self.commodityLastPushButton.clicked.connect(self.lastPage)
        self.commodityNextPushButton.clicked.connect(self.nextPage)

        self.infoUpdatePushButton.clicked.connect(self.updateInfo)

    def searchCommodity(self):
        self.sql = 'select Cname, Cdescribe, price, discount, commodity.stockSize, stock, address, Cid, warehouse.Wid ' \
                   'from commodity, warehouse where commodity.Sid = \"' + self.Sid \
                   + '\" and commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize ' \
                     'and Cname like \"%' + self.commoditySearchLineEdit.text() + '%\";'
        self.dbcursor.execute(self.sql)
        self.data = self.dbcursor.fetchall()
        self.page = 1
        self.reShow()

    def addCommodity(self):
        self.addCommodityDialog = AddCommodityDialog(self.db, self.dbcursor, self.Sid)
        self.addCommodityDialog.show()

    def updataCommodity(self):
        if self.page * 3 - 3 + 0 < len(self.data) and self.haveCheckBox1 and self.checkBox1.isChecked():
            self.sql = 'update warehouse set stockSize = \"' + self.commodityTableWidget.item(0, 5).text() \
                       + '\", stock = \"' + self.commodityTableWidget.item(0, 6).text() \
                       + '\" where stockCid = \"' + self.data[self.page * 3 - 3 + 0][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 0][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'update commodity set stockSize = \"' + self.commodityTableWidget.item(0, 5).text() \
                       + '\", Cname = \"' + self.commodityTableWidget.item(0, 1).text() \
                       + '\", price = \"' + self.commodityTableWidget.item(0, 3).text() \
                       + '\", discount = \"' + self.commodityTableWidget.item(0, 4).text() \
                       + '\", Cdescribe = \"' + self.textBrowser1.toPlainText() \
                       + '\" where Cid = \"' + self.data[self.page * 3 - 3 + 0][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 0][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        if self.page * 3 - 3 + 1 < len(self.data) and self.haveCheckBox2 and self.checkBox2.isChecked():
            self.sql = 'update warehouse set stockSize = \"' + self.commodityTableWidget.item(1, 5).text() \
                       + '\", stock = \"' + self.commodityTableWidget.item(1, 6).text() \
                       + '\" where stockCid = \"' + self.data[self.page * 3 - 3 + 1][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 1][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'update commodity set stockSize = \"' + self.commodityTableWidget.item(1, 5).text() \
                       + '\", Cname = \"' + self.commodityTableWidget.item(1, 1).text() \
                       + '\", price = \"' + self.commodityTableWidget.item(1, 3).text() \
                       + '\", discount = \"' + self.commodityTableWidget.item(1, 4).text() \
                       + '\", Cdescribe = \"' + self.textBrowser2.toPlainText() \
                       + '\" where Cid = \"' + self.data[self.page * 3 - 3 + 1][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 1][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        if self.page * 3 - 3 + 2 < len(self.data) and self.haveCheckBox3 and self.checkBox3.isChecked():
            self.sql = 'update warehouse set stockSize = \"' + self.commodityTableWidget.item(2, 5).text() \
                       + '\", stock = \"' + self.commodityTableWidget.item(2, 6).text() \
                       + '\" where stockCid = \"' + self.data[self.page * 3 - 3 + 2][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 2][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'update commodity set stockSize = \"' + self.commodityTableWidget.item(2, 5).text() \
                       + '\", Cname = \"' + self.commodityTableWidget.item(2, 1).text() \
                       + '\", price = \"' + self.commodityTableWidget.item(2, 3).text() \
                       + '\", discount = \"' + self.commodityTableWidget.item(2, 4).text() \
                       + '\", Cdescribe = \"' + self.textBrowser3.toPlainText() \
                       + '\" where Cid = \"' + self.data[self.page * 3 - 3 + 2][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 2][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '修改成功')

    def deleteCommodity(self):
        if self.page * 3 - 3 + 0 < len(self.data) and self.haveCheckBox1 and self.checkBox1.isChecked():
            self.sql = 'delete from commodity where Cid = \"' + self.data[self.page * 3 - 3 + 0][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 0][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from warehouse where Wid = \"' + self.data[self.page * 3 - 3 + 0][8] \
                       + '\" and stockCid = \"' + self.data[self.page * 3 - 3 + 0][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 0][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        if self.page * 3 - 3 + 1 < len(self.data) and self.haveCheckBox2 and self.checkBox2.isChecked():
            self.sql = 'delete from commodity where Cid = \"' + self.data[self.page * 3 - 3 + 1][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 1][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from warehouse where Wid = \"' + self.data[self.page * 3 - 3 + 1][8] \
                       + '\" and stockCid = \"' + self.data[self.page * 3 - 3 + 1][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 1][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        if self.page * 3 - 3 + 2 < len(self.data) and self.haveCheckBox3 and self.checkBox3.isChecked():
            self.sql = 'delete from commodity where Cid = \"' + self.data[self.page * 3 - 3 + 2][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 2][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from warehouse where Wid = \"' + self.data[self.page * 3 - 3 + 2][8] \
                       + '\" and stockCid = \"' + self.data[self.page * 3 - 3 + 2][7] \
                       + '\" and stockSize = \"' + self.data[self.page * 3 - 3 + 2][4] + '\";'

            self.dbcursor.execute(self.sql)
            self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '删除成功')

    def lastPage(self):
        self.page = self.page - 1
        self.showData()
        self.showPage()
        self.enablePagePushButton()
        self.enableFuncPushButton()

    def nextPage(self):
        self.page = self.page + 1
        self.showData()
        self.showPage()
        self.enablePagePushButton()
        self.enableFuncPushButton()

    def updateInfo(self):
        self.sql = 'update store set Sname = \"' + self.SnameLineEdit.text() + '\", principal = \"' \
                   + self.principalLineEdit.text() + '\", Tel = \"' + self.TelLineEdit.text() \
                   + '\", ID_card = \"' + self.IDLineEdit.text() + '\" where Sid = \"' + self.Sid + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '修改成功')

    def initTable(self):
        self.haveCheckBox1 = False
        self.haveCheckBox2 = False
        self.haveCheckBox3 = False

        if self.page * 3 - 3 + 0 < len(self.data):
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
            self.textBrowser1.setReadOnly(False)

            self.checkBox1.stateChanged.connect(self.enableFuncPushButton)
            self.haveCheckBox1 = True

        if self.page * 3 - 3 + 1 < len(self.data):
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
            self.textBrowser2.setReadOnly(False)

            self.checkBox2.stateChanged.connect(self.enableFuncPushButton)
            self.haveCheckBox2 = True

        if self.page * 3 - 3 + 2 < len(self.data):
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
            self.textBrowser3.setReadOnly(False)

            self.checkBox3.stateChanged.connect(self.enableFuncPushButton)
            self.haveCheckBox2 = True

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
        self.commodityAddPushButton.setEnabled(True)
        if self.page * 3 - 3 + 1 == len(self.data):
            if self.checkBox1.isChecked():
                self.commodityUpdatePushButton.setEnabled(True)
                self.commodityDeletePushButton.setEnabled(True)
            else:
                self.commodityUpdatePushButton.setEnabled(False)
                self.commodityDeletePushButton.setEnabled(False)
        elif self.page * 3 - 3 + 2 == len(self.data):
            if self.checkBox1.isChecked() or self.checkBox2.isChecked():
                self.commodityUpdatePushButton.setEnabled(True)
                self.commodityDeletePushButton.setEnabled(True)
            else:
                self.commodityUpdatePushButton.setEnabled(False)
                self.commodityDeletePushButton.setEnabled(False)
        else:
            if self.checkBox1.isChecked() or self.checkBox2.isChecked() or self.checkBox3.isChecked():
                self.commodityUpdatePushButton.setEnabled(True)
                self.commodityDeletePushButton.setEnabled(True)
            else:
                self.commodityUpdatePushButton.setEnabled(False)
                self.commodityDeletePushButton.setEnabled(False)

    def getAllData(self):
        self.sql = 'select Cname, Cdescribe, price, discount, commodity.stockSize, stock, address, Cid, warehouse.Wid ' \
                   'from commodity, warehouse where commodity.Sid = \"' + self.Sid \
                   + '\" and commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize;'
        self.dbcursor.execute(self.sql)
        self.data = self.dbcursor.fetchall()

    def showData(self):
        self.clearTable()
        for i in range(0, 3):
            if self.page * 3 - 3 + i < len(self.data):
                for j in [1, 3, 4, 5, 6]:
                    self.commodityTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.data[self.page * 3 - 3 + i][j - 1])))
                if i == 0:
                    self.textBrowser1.setText(self.data[self.page * 3 - 3 + i][1])
                    self.textBrowser4.setText(self.data[self.page * 3 - 3 + i][6])
                elif i == 1:
                    self.textBrowser2.setText(self.data[self.page * 3 - 3 + i][1])
                    self.textBrowser5.setText(self.data[self.page * 3 - 3 + i][6])
                elif i == 2:
                    self.textBrowser3.setText(self.data[self.page * 3 - 3 + i][1])
                    self.textBrowser6.setText(self.data[self.page * 3 - 3 + i][6])
            else:
                break

    def showPage(self):
        self.commodityPageLabel.setText('第' + str(self.page) + '页')

    def reShow(self):
        self.showData()
        self.enablePagePushButton()
        self.enableFuncPushButton()
        self.showPage()

    def clearTable(self):
        self.commodityTableWidget.clearContents()
        self.initTable()


if __name__ == "__main__":
    db = pymysql.connect("localhost", "root", "130e340", "e-commerce")
    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    storeUI = StoreUI(db, cursor, "001")
    storeUI.show()
    sys.exit(app.exec_())
