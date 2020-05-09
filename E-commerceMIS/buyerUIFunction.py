from PyQt5 import QtWidgets
from buyerUI import Ui_Form
from addCartDialogFunction import AddCartDialog
from addAddressDialogFuntion import AddAddressDialog
from buyDialogFunction import BuyDialog
import pymysql
import sys


class BuyerUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self, db, dbcursor, Bid):
        super(BuyerUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.dbcursor = dbcursor
        self.Bid = Bid
        self.commodityPage = 1
        self.cartPage = 1
        self.orderPage = 1
        self.addressPage = 1

        self.commodityTableWidget.setColumnWidth(0, 40)
        self.commodityTableWidget.setColumnWidth(1, 80)
        self.commodityTableWidget.setColumnWidth(2, 150)
        self.commodityTableWidget.setColumnWidth(3, 60)
        self.commodityTableWidget.setColumnWidth(4, 60)

        # commodityTab
        self.getAllCommodityData()
        self.initTable()
        self.commodityPageLabel.setText(str(self.commodityPage))
        self.reShowCommodity()

        # cartTab
        self.getAllCart()
        self.showCart()

        # orderTab
        self.getAllOrder()
        self.showOrder()

        # infoTab
        self.getBuyerInfo()
        self.showBuyerInfo()
        self.getAllAddress()
        self.showAddress()

        # commodityTab
        self.commoditySearchPushButton.clicked.connect(self.searchCommodity)
        self.addCartPushButton.clicked.connect(self.addCart)
        self.commodityLastPushButton.clicked.connect(self.commodityLastPage)
        self.commodityNextPushButton.clicked.connect(self.commodityNextPage)

        # cartTab
        self.cartRefreshPushButton.clicked.connect(self.reShowCart)
        self.cartBuyPushButton.clicked.connect(self.buy)
        self.cartDeletePushButton.clicked.connect(self.deletCart)
        self.cartLastPagePushButton.clicked.connect(self.cartLastPage)
        self.cartNextPagePushButton.clicked.connect(self.cartNextPage)

        # orderTab
        self.orderRefreshPushButton.clicked.connect(self.reShowOrder)
        self.orderDeletePushButton.clicked.connect(self.deletOrder)
        self.orderLastPagePushButton.clicked.connect(self.orderLastPage)
        self.orderNextPagePushButton.clicked.connect(self.orderNextPage)

        # infoTab
        self.infoRefreshPushButton.clicked.connect(self.reShowAddress)
        self.infoAddPushButton.clicked.connect(self.addAddress)
        self.infoUpdatePushButton.clicked.connect(self.updateAddress)
        self.infoLastPagePushButton.clicked.connect(self.addressLastPage)
        self.infoNextPagePushButton.clicked.connect(self.addressNextPage)

    # commodityTab
    def searchCommodity(self):
        self.sql = 'select Cname, Cdescribe, commodity.stockSize, price, discount, commodity.Cid, stock, address ' \
                   'from commodity, warehouse ' \
                   'where commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize ' \
                   'and Cname like \"%' + self.commoditySearchLineEdit.text() + '%\";'
        self.dbcursor.execute(self.sql)
        self.commodityData = self.dbcursor.fetchall()
        self.commodityPage = 1
        self.reShowCommodity()

    def addCart(self):
        if self.haveCheckBox1 and self.checkBox1.isChecked():
            self.addCartDialog1 = AddCartDialog(self.db, self.dbcursor, self.Bid,
                                                self.commodityData[self.commodityPage * 3 - 3 + 0][5],
                                                self.commodityData[self.commodityPage * 3 - 3 + 0][0],
                                                self.commodityData[self.commodityPage * 3 - 3 + 0][2],
                                                self.commodityData[self.commodityPage * 3 - 3 + 0][6])
            self.addCartDialog1.show()
        if self.haveCheckBox2 and self.checkBox2.isChecked():
            self.addCartDialog2 = AddCartDialog(self.db, self.dbcursor, self.Bid,
                                                self.commodityData[self.commodityPage * 3 - 3 + 1][5],
                                                self.commodityData[self.commodityPage * 3 - 3 + 1][0],
                                                self.commodityData[self.commodityPage * 3 - 3 + 1][2],
                                                self.commodityData[self.commodityPage * 3 - 3 + 1][6])
            self.addCartDialog2.show()
        if self.haveCheckBox3 and self.checkBox3.isChecked():
            self.addCartDialog3 = AddCartDialog(self.db, self.dbcursor, self.Bid,
                                                self.commodityData[self.commodityPage * 3 - 3 + 2][5],
                                                self.commodityData[self.commodityPage * 3 - 3 + 2][0],
                                                self.commodityData[self.commodityPage * 3 - 3 + 2][2],
                                                self.commodityData[self.commodityPage * 3 - 3 + 2][6])
            self.addCartDialog3.show()

    def commodityLastPage(self):
        self.commodityPage = self.commodityPage - 1
        self.showCommodityData()
        self.showCommodityPage()
        self.enableCommodityPagePushButton()
        self.enableCommodityFuncPushButton()

    def commodityNextPage(self):
        self.commodityPage = self.commodityPage + 1
        self.showCommodityData()
        self.showCommodityPage()
        self.enableCommodityPagePushButton()
        self.enableCommodityFuncPushButton()

    def initTable(self):
        self.haveCheckBox1 = False
        self.haveCheckBox2 = False
        self.haveCheckBox3 = False

        if self.commodityPage * 3 - 3 + 0 < len(self.commodityData):
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

            self.checkBox1.stateChanged.connect(self.enableCommodityFuncPushButton)
            self.haveCheckBox1 = True

        if self.commodityPage * 3 - 3 + 1 < len(self.commodityData):
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

            self.checkBox2.stateChanged.connect(self.enableCommodityFuncPushButton)
            self.haveCheckBox2 = True

        if self.commodityPage * 3 - 3 + 2 < len(self.commodityData):
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

            self.checkBox3.stateChanged.connect(self.enableCommodityFuncPushButton)
            self.haveCheckBox3 = True

    def enableCommodityPagePushButton(self):
        if self.commodityPage == 1:
            self.commodityLastPushButton.setEnabled(False)
        else:
            self.commodityLastPushButton.setEnabled(True)

        if self.commodityPage * 3 >= len(self.commodityData):
            self.commodityNextPushButton.setEnabled(False)
        else:
            self.commodityNextPushButton.setEnabled(True)

    def enableCommodityFuncPushButton(self):
        if self.commodityPage * 3 - 3 + 1 == len(self.commodityData):
            if self.checkBox1.isChecked():
                self.addCartPushButton.setEnabled(True)
            else:
                self.addCartPushButton.setEnabled(False)
        elif self.commodityPage * 3 - 3 + 2 == len(self.commodityData):
            if self.checkBox1.isChecked() or self.checkBox2.isChecked():
                self.addCartPushButton.setEnabled(True)
            else:
                self.addCartPushButton.setEnabled(False)
        else:
            if self.checkBox1.isChecked() or self.checkBox2.isChecked() or self.checkBox3.isChecked():
                self.addCartPushButton.setEnabled(True)
            else:
                self.addCartPushButton.setEnabled(False)

    def getAllCommodityData(self):
        self.sql = 'select Cname, Cdescribe, commodity.stockSize, price, discount, commodity.Cid, stock, address ' \
                   'from commodity, warehouse ' \
                   'where commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize;'
        self.dbcursor.execute(self.sql)
        self.commodityData = self.dbcursor.fetchall()

    def showCommodityData(self):
        self.clearTable()
        for i in range(0, 3):
            if self.commodityPage * 3 - 3 + i < len(self.commodityData):
                for j in [1, 3]:
                    self.commodityTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(
                        str(self.commodityData[self.commodityPage * 3 - 3 + i][j - 1])))
                if i == 0:
                    self.textBrowser1.setText(self.commodityData[self.commodityPage * 3 - 3 + i][1])
                    self.commodityTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(
                        str(self.commodityData[self.commodityPage * 3 - 3 + i][3] * self.commodityData[self.commodityPage * 3 - 3 + i][4])))
                elif i == 1:
                    self.textBrowser2.setText(self.commodityData[self.commodityPage * 3 - 3 + i][1])
                    self.commodityTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(
                        str(self.commodityData[self.commodityPage * 3 - 3 + i][3] * self.commodityData[self.commodityPage * 3 - 3 + i][4])))
                elif i == 2:
                    self.textBrowser3.setText(self.commodityData[self.commodityPage * 3 - 3 + i][1])
                    self.commodityTableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(
                        str(self.commodityData[self.commodityPage * 3 - 3 + i][3] * self.commodityData[self.commodityPage * 3 - 3 + i][4])))
            else:
                break

    def showCommodityPage(self):
        self.commodityPageLabel.setText('第' + str(self.commodityPage) + '页')

    def reShowCommodity(self):
        self.showCommodityData()
        self.enableCommodityPagePushButton()
        self.enableCommodityFuncPushButton()
        self.showCommodityPage()

    def clearTable(self):
        self.commodityTableWidget.clearContents()
        self.initTable()

    # cartTab
    def getAllCart(self):
        self.sql = 'select store.Sname, commodity.Cname, commodity.Cdescribe, cart.size, cart.num, commodity.price, ' \
                   'commodity.discount, commodity.Cid, store.Sid, store.principal, warehouse.address, store.Tel ' \
                   'from store, commodity, warehouse, cart ' \
                   'where cart.Bid = \"' + self.Bid \
                   + '\" and cart.Cid = commodity.Cid and cart.size = commodity.stockSize ' \
                     'and commodity.Cid = warehouse.stockCid and commodity.stockSize = warehouse.stockSize ' \
                     'and store.Sid = commodity.Sid;'
        self.dbcursor.execute(self.sql)
        self.cartData = self.dbcursor.fetchall()

    def showCart(self):
        if len(self.cartData) > 0:
            self.cartSnameLabel.setText(self.cartData[self.cartPage - 1][0])
            self.cartCnameLabel.setText(self.cartData[self.cartPage - 1][1])
            self.cartDescribeTextBrowser.setText(self.cartData[self.cartPage - 1][2])
            self.cartSizeLabel.setText(self.cartData[self.cartPage - 1][3])
            self.cartNumLabel.setText(str(self.cartData[self.cartPage - 1][4]))
            self.cartPriseLabel.setText(str(self.cartData[self.cartPage - 1][5] * self.cartData[self.cartPage - 1][6]))

            self.cartPageLabel.setText('第' + str(self.cartPage) + '页')

            if self.cartPage == 1:
                self.cartLastPagePushButton.setEnabled(False)
            else:
                self.cartLastPagePushButton.setEnabled(True)
            if self.cartPage == len(self.cartData):
                self.cartNextPagePushButton.setEnabled(False)
            else:
                self.cartNextPagePushButton.setEnabled(True)
        else:
            self.cartBuyPushButton.setEnabled(False)
            self.cartDeletePushButton.setEnabled(False)
            self.cartLastPagePushButton.setEnabled(False)
            self.cartNextPagePushButton.setEnabled(False)

    def buy(self):
        self.buyDialog = BuyDialog(self.db, self.dbcursor, self.Bid, self.cartData[self.cartPage - 1][7], self.cartData[self.cartPage - 1][8],
                                   self.cartData[self.cartPage - 1][3], self.cartData[self.cartPage - 1][4],
                                   (self.cartData[self.cartPage - 1][5] * self.cartData[self.cartPage - 1][6]),
                                   self.cartData[self.cartPage - 1][9], self.cartData[self.cartPage - 1][10],
                                   self.cartData[self.cartPage - 1][11])
        self.buyDialog.show()

    def deletCart(self):
        self.sql = 'delete from cart ' \
                   'where Cid = \"' + self.cartData[self.cartPage - 1][7] + '\" and Bid = \"' + self.Bid \
                   + '\" and size = \"' + self.cartData[self.cartPage - 1][3] + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '已删除')

    def cartLastPage(self):
        self.cartPage = self.cartPage - 1
        self.showCart()

    def cartNextPage(self):
        self.cartPage = self.cartPage + 1
        self.showCart()

    def reShowCart(self):
        self.cartPage = 1
        self.getAllCart()
        self.showCart()

    # orderTab
    def getAllOrder(self):
        self.sql = 'select store.Sname, orderform.Oid, commodity.Cname, commodity.Cdescribe, orderform.size, ' \
                   'orderform.num, orderform.price, orderform.Lstatus ' \
                   'from store, commodity, orderform, commodity_order ' \
                   'where orderform.Sid = store.Sid and orderform.Oid = commodity_order.Oid ' \
                   'and commodity_order.Cid = commodity.Cid and commodity_order.Csize = commodity.stockSize ' \
                   'and orderform.Bid = \"' + self.Bid + '\";'
        self.dbcursor.execute(self.sql)
        self.orderData = self.dbcursor.fetchall()

    def showOrder(self):
        if len(self.orderData) > 0:
            self.orderSnameLabel.setText(self.orderData[self.orderPage - 1][0])
            self.orderIdLabel.setText(self.orderData[self.orderPage - 1][1])
            self.orderCnameLabel.setText(self.orderData[self.orderPage - 1][2])
            self.orderDescribeTextBrowser.setText(self.orderData[self.orderPage - 1][3])
            self.orderSizeLabel.setText(self.orderData[self.orderPage - 1][4])
            self.orderNumLabel.setText(str(self.orderData[self.orderPage - 1][5]))
            self.orderPriceLabel.setText(str(self.orderData[self.orderPage - 1][6]))
            if self.orderData[self.orderPage - 1][7] == '0':
                self.orderStatusLabel.setText('未发货')
            elif self.orderData[self.orderPage - 1][7] == '1':
                self.orderStatusLabel.setText('正在运输')
            elif self.orderData[self.orderPage - 1][7] == '2':
                self.orderStatusLabel.setText('已签收')

            self.orderPageLabel.setText('第' + str(self.orderPage) + '页')

            if self.orderPage == 1:
                self.orderLastPagePushButton.setEnabled(False)
            else:
                self.orderLastPagePushButton.setEnabled(True)
            if self.orderPage == len(self.orderData):
                self.orderNextPagePushButton.setEnabled(False)
            else:
                self.orderNextPagePushButton.setEnabled(True)
        else:
            self.orderDeletePushButton.setEnabled(False)
            self.orderLastPagePushButton.setEnabled(False)
            self.orderNextPagePushButton.setEnabled(False)

    def deletOrder(self):
        self.sql = 'delete from logistics ' \
                   'where Oid = \"' + self.orderData[self.orderPage - 1][1] + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        self.sql = 'delete from commodity_order ' \
                   'where Oid = \"' + self.orderData[self.orderPage - 1][1] + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        self.sql = 'delete from orderform ' \
                   'where Oid = \"' + self.orderData[self.orderPage - 1][1] + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '已删除')

    def orderLastPage(self):
        self.orderPage = self.orderPage - 1
        self.showOrder()

    def orderNextPage(self):
        self.orderPage = self.orderPage + 1
        self.showOrder()

    def reShowOrder(self):
        self.orderPage = 1
        self.getAllOrder()
        self.showOrder()

    # infoTab
    def getBuyerInfo(self):
        self.sql = 'select Bname, Scredit from buyer where Bid = \"' + self.Bid + '\";'
        self.dbcursor.execute(self.sql)
        self. buyerInfo = self.dbcursor.fetchone()

        self.infoBnameLabel.setText(self.buyerInfo[0])
        self.infoCreditLabel.setText(str(self.buyerInfo[1]))

    def showBuyerInfo(self):
        self.infoBnameLabel.setText(self.buyerInfo[0])
        self.infoCreditLabel.setText(str(self.buyerInfo[1]))

    def getAllAddress(self):
        self.sql = 'select Rname, Tel, address, postcode, Aid from addressbook where Bid = \"' + self.Bid + '\";'
        self.dbcursor.execute(self.sql)
        self.addressData = self.dbcursor.fetchall()

    def showAddress(self):
        if len(self.addressData) > 0:
            self.infoRnameLineEdit.setText(self.addressData[self.addressPage - 1][0])
            self.infoTelLineEdit.setText(self.addressData[self.addressPage - 1][1])
            self.infoAddressTextBrowser.setText(self.addressData[self.addressPage - 1][2])
            self.infoPostcodeLineEdit.setText(self.addressData[self.addressPage - 1][3])

            self.infoPageLabel.setText('第' + str(self.addressPage) + '页')
            if self.addressPage == 1:
                self.infoLastPagePushButton.setEnabled(False)
            else:
                self.infoLastPagePushButton.setEnabled(True)
            if self.addressPage == len(self.addressData):
                self.infoNextPagePushButton.setEnabled(False)
            else:
                self.infoNextPagePushButton.setEnabled(True)
        else:
            self.infoUpdatePushButton.setEnabled(False)
            self.infoLastPagePushButton.setEnabled(False)
            self.infoNextPagePushButton.setEnabled(False)

    def addAddress(self):
        self.addAddressDialog = AddAddressDialog(self.db, self.dbcursor, self.Bid)
        self.addAddressDialog.show()

    def updateAddress(self):
        self.sql = 'update addressbook set Rname = \"' + self.infoRnameLineEdit.text() + '\", Tel = \"' \
                   + self.infoTelLineEdit.text() + '\", address = \"' + self.infoAddressTextBrowser.toPlainText() \
                   + '\", postcode = \"' + self.infoPostcodeLineEdit.text() \
                   + '\" where Aid = \"' + self.addressData[self.addressPage - 1][4] + '\";'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QtWidgets.QMessageBox.information(self, 'Information', '修改成功')

    def addressLastPage(self):
        self.addressPage = self.addressPage - 1
        self.showAddress()

    def addressNextPage(self):
        self.addressPage = self.addressPage + 1
        self.showAddress()

    def reShowAddress(self):
        self.addressPage = 1
        self.getAllAddress()
        self.showAddress()


if __name__ == "__main__":
    db = pymysql.connect("localhost", "root", "130e340", "e-commerce")
    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    buyerUI = BuyerUI(db, cursor, "001")
    buyerUI.show()
    sys.exit(app.exec_())