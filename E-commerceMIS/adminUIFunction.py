from adminUI import Ui_Form
from PyQt5 import QtWidgets
import pymysql
import sys

class AdminUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self, db, dbcursor):
        super(AdminUI, self).__init__()
        self.setupUi(self)

        self.db = db
        self.dbcursor = dbcursor
        self.buyerPage = 1
        self.storePage = 1

        self.getAllBuyer()
        self.initBuyerTable()
        self.buyerPageLabel.setText(str(self.buyerPage))
        self.showBuyer()

        self.buyerSearchPushButton.clicked.connect(self.searchBuyer)
        self.buyerDeletePushButton.clicked.connect(self.deleteBuyer)
        self.buyerLastPushButton.clicked.connect(self.buyerLastPage)
        self.buyerNextPushButton.clicked.connect(self.buyerNextPage)

        self.getAllStore()
        self.initStoreTable()
        self.storePageLabel.setText(str(self.storePage))
        self.showStore()

        self.storeSearchPushButton.clicked.connect(self.searchStore)
        self.storeDeletePushButton.clicked.connect(self.deleteStore)
        self.storeLastPushButton.clicked.connect(self.storeLastPage)
        self.storeNextPushButton.clicked.connect(self.storeNextPage)

    def searchBuyer(self):
        self.sql = 'select Bid, Bname, Scredit from buyer ' \
                   'where Bname like \"%' + self.buyerSearchLineEdit.text() + '%\";'
        self.dbcursor.execute(self.sql)
        self.buyerData = self.dbcursor.fetchall()
        self.buyerPage = 1
        self.showBuyer()

    def deleteBuyer(self):
        if self.buyerPage * 3 - 3 + 0 < len(self.buyerData) and self.haveBuyerCheckBox1 and self.buyerCheckBox1.isChecked():
            self.sql = 'select Oid from orderform where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 0][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.buyerOid = self.dbcursor.fetchall()

            if len(self.buyerOid) > 0:
                self.buyerOid = self.buyerOid[0]

                self.sql = 'delete from logistics where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from commodity_order where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from orderform where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

            else:
                self.buyerOid = self.buyerOid[0]

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 0][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from cart where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 0][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from addressbook where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 0][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 0][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

        elif self.buyerPage * 3 - 3 + 1 < len(self.buyerData) and self.haveBuyerCheckBox1 and self.buyerCheckBox1.isChecked():
            self.sql = 'select Oid from orderform where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 1][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.buyerOid = self.dbcursor.fetchall()

            if len(self.buyerOid) > 0:
                self.buyerOid = self.buyerOid[0]

                self.sql = 'delete from logistics where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from commodity_order where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from orderform where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

            else:
                self.buyerOid = self.buyerOid[0]

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 1][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from cart where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 1][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from addressbook where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 1][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 1][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

        elif self.buyerPage * 3 - 3 + 2 < len(self.buyerData) and self.haveBuyerCheckBox1 and self.buyerCheckBox1.isChecked():
            self.sql = 'select Oid from orderform where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 2][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.buyerOid = self.dbcursor.fetchall()

            if len(self.buyerOid) > 0:
                self.buyerOid = self.buyerOid[0]

                self.sql = 'delete from logistics where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from commodity_order where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from orderform where Oid = \"' + self.buyerOid[0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

            else:
                self.buyerOid = self.buyerOid[0]

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 2][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from cart where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 2][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from addressbook where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 2][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from buyer where Bid = \"' + self.buyerData[self.buyerPage * 3 - 3 + 2][0] + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

    def buyerLastPage(self):
        self.buyerPage = self.buyerPage - 1
        self.showBuyer()
        self.buyerPageLabel.setText(str(self.buyerPage))

    def buyerNextPage(self):
        self.buyerPage = self.buyerPage + 1
        self.showBuyer()
        self.buyerPageLabel.setText(str(self.buyerPage))

    def getAllBuyer(self):
        self.sql = 'select Bid, Bname, Scredit from buyer;'
        self.dbcursor.execute(self.sql)
        self.buyerData = self.dbcursor.fetchall()

    def initBuyerTable(self):
        self.haveBuyerCheckBox1 = False
        self.haveBuyerCheckBox2 = False
        self.haveBuyerCheckBox3 = False

        if self.buyerPage * 3 - 3 + 0 < len(self.buyerData):
            self.buyerWidget1 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.buyerWidget1)
            spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem1)
            self.buyerCheckBox1 = QtWidgets.QCheckBox(self.buyerWidget1)
            self.horizontalLayout.addWidget(self.buyerCheckBox1)
            spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem2)
            self.buyerTableWidget.setCellWidget(0, 0, self.buyerWidget1)

            self.buyerCheckBox1.stateChanged.connect(self.enableBuyerFuncPushButton)
            self.haveBuyerCheckBox1 = True

        if self.buyerPage * 3 - 3 + 1 < len(self.buyerData):
            self.buyerWidget2 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.buyerWidget2)
            spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem3)
            self.buyerCheckBox2 = QtWidgets.QCheckBox(self.buyerWidget2)
            self.horizontalLayout.addWidget(self.buyerCheckBox2)
            spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem4)
            self.buyerTableWidget.setCellWidget(1, 0, self.buyerWidget2)

            self.buyerCheckBox2.stateChanged.connect(self.enableBuyerFuncPushButton)
            self.haveBuyerCheckBox2 = True

        if self.buyerPage * 3 - 3 + 2 < len(self.buyerData):
            self.buyerWidget3 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.buyerWidget3)
            spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem5)
            self.buyerCheckBox3 = QtWidgets.QCheckBox(self.buyerWidget3)
            self.horizontalLayout.addWidget(self.buyerCheckBox3)
            spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem6)
            self.buyerTableWidget.setCellWidget(2, 0, self.buyerWidget3)

            self.buyerCheckBox3.stateChanged.connect(self.enableBuyerFuncPushButton)
            self.haveBuyerCheckBox3 = True

    def enableBuyerPagePushButton(self):
        if self.buyerPage == 1:
            self.buyerLastPushButton.setEnabled(False)
        else:
            self.buyerLastPushButton.setEnabled(True)

        if self.buyerPage * 3 >= len(self.buyerData):
            self.buyerNextPushButton.setEnabled(False)
        else:
            self.buyerNextPushButton.setEnabled(True)

    def enableBuyerFuncPushButton(self):
        if self.buyerPage * 3 - 3 + 1 == len(self.buyerData):
            if self.buyerCheckBox1.isChecked():
                self.buyerDeletePushButton.setEnabled(True)
            else:
                self.buyerDeletePushButton.setEnabled(False)
        elif self.buyerPage * 3 - 3 + 2 == len(self.buyerData):
            if self.buyerCheckBox1.isChecked() or self.buyerCheckBox2.isChecked():
                self.buyerDeletePushButton.setEnabled(True)
            else:
                self.buyerDeletePushButton.setEnabled(False)
        else:
            if self.buyerCheckBox1.isChecked() or self.buyerCheckBox2.isChecked() or self.buyerCheckBox3.isChecked():
                self.buyerDeletePushButton.setEnabled(True)
            else:
                self.buyerDeletePushButton.setEnabled(False)

    def showBuyer(self):
        self.clearBuyerTable()
        self.enableBuyerPagePushButton()
        self.enableBuyerFuncPushButton()
        if len(self.buyerData) > 0:
            for i in range(0, 3):
                if self.buyerPage * 3 - 3 + i < len(self.buyerData):
                    for j in range(1, 4):
                        self.buyerTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(
                            str(self.buyerData[self.buyerPage * 3 - 3 + i][j - 1])))
                else:
                    break

    def clearBuyerTable(self):
        self.buyerTableWidget.clearContents()
        self.initBuyerTable()

    def searchStore(self):
        self.sql = 'select Sid, Sname, Scredit from store ' \
                   'where Sname like \"%' + self.storeSearchLineEdit.text() + '%\";'
        self.dbcursor.execute(self.sql)
        self.storeData = self.dbcursor.fetchall()

        self.storePage = 1
        self.showStore()

    def deleteStore(self):
        for i in range(0, 3):
            if self.storePage * 3 - 3 + i < len(self.storeData) and self.haveStoreCheckBox1 and self.storeCheckBox1.isChecked():
                self.sql = 'update orderform set Sid = \"000\" ' \
                           'where Sid = \"' + self.storeData[self.storePage * 3 - 3 + i][0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'update commodity set Sid = \"000\" ' \
                           'where Sid = \"' + self.storeData[self.storePage * 3 - 3 + i][0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

                self.sql = 'delete from store where Sid = \"' + self.storeData[self.storePage * 3 - 3 + i][0] + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()

    def storeLastPage(self):
        self.storePage = self.storePage - 1
        self.showStore()
        self.storePageLabel.setText(str(self.storePage))

    def storeNextPage(self):
        self.storePage = self.storePage + 1
        self.showStore()
        self.storePageLabel.setText(str(self.storePage))

    def getAllStore(self):
        self.sql = 'select Sid, Sname, Scredit from store;'
        self.dbcursor.execute(self.sql)
        self.storeData = self.dbcursor.fetchall()

    def initStoreTable(self):
        self.haveStoreCheckBox1 = False
        self.haveStoreCheckBox2 = False
        self.haveStoreCheckBox3 = False

        if self.storePage * 3 - 3 + 0 < len(self.storeData):
            self.storeWidget1 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.storeWidget1)
            spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem1)
            self.storeCheckBox1 = QtWidgets.QCheckBox(self.storeWidget1)
            self.horizontalLayout.addWidget(self.storeCheckBox1)
            spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem2)
            self.storeTableWidget.setCellWidget(0, 0, self.storeWidget1)

            self.storeCheckBox1.stateChanged.connect(self.enableStoreFuncPushButton)
            self.haveStoreCheckBox1 = True

        if self.storePage * 3 - 3 + 1 < len(self.storeData):
            self.storeWidget2 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.storeWidget2)
            spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem3)
            self.storeCheckBox2 = QtWidgets.QCheckBox(self.storeWidget2)
            self.horizontalLayout.addWidget(self.storeCheckBox2)
            spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem4)
            self.storeTableWidget.setCellWidget(1, 0, self.storeWidget2)

            self.storeCheckBox2.stateChanged.connect(self.enableStoreFuncPushButton)
            self.haveStoreCheckBox2 = True

        if self.storePage * 3 - 3 + 2 < len(self.storeData):
            self.storeWidget3 = QtWidgets.QWidget()
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.storeWidget3)
            spacerItem5 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem5)
            self.storeCheckBox3 = QtWidgets.QCheckBox(self.storeWidget3)
            self.horizontalLayout.addWidget(self.storeCheckBox3)
            spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout.addItem(spacerItem6)
            self.storeTableWidget.setCellWidget(2, 0, self.storeWidget3)

            self.storeCheckBox3.stateChanged.connect(self.enableStoreFuncPushButton)
            self.haveStoreCheckBox3 = True

    def enableStorePagePushButton(self):
        if self.storePage == 1:
            self.storeLastPushButton.setEnabled(False)
        else:
            self.storeLastPushButton.setEnabled(True)

        if self.storePage * 3 >= len(self.storeData):
            self.storeNextPushButton.setEnabled(False)
        else:
            self.storeNextPushButton.setEnabled(True)

    def enableStoreFuncPushButton(self):
        if self.storePage * 3 - 3 + 1 == len(self.storeData):
            if self.storeCheckBox1.isChecked():
                self.storeDeletePushButton.setEnabled(True)
            else:
                self.storeDeletePushButton.setEnabled(False)
        elif self.storePage * 3 - 3 + 2 == len(self.storeData):
            if self.storeCheckBox1.isChecked() or self.storeCheckBox2.isChecked():
                self.storeDeletePushButton.setEnabled(True)
            else:
                self.storeDeletePushButton.setEnabled(False)
        else:
            if self.storeCheckBox1.isChecked() or self.storeCheckBox2.isChecked() or self.storeCheckBox3.isChecked():
                self.storeDeletePushButton.setEnabled(True)
            else:
                self.storeDeletePushButton.setEnabled(False)

    def showStore(self):
        self.clearStoreTable()
        self.enableStorePagePushButton()
        self.enableStoreFuncPushButton()
        if len(self.storeData) > 0:
            for i in range(0, 3):
                if self.storePage * 3 - 3 + i < len(self.storeData):
                    for j in range(1, 4):
                        self.storeTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(
                            str(self.storeData[self.storePage * 3 - 3 + i][j - 1])))
                else:
                    break

    def clearStoreTable(self):
        self.storeTableWidget.clearContents()
        self.initStoreTable()

if __name__ == "__main__":
    db = pymysql.connect("localhost", "root", "130e340", "e-commerce")
    cursor = db.cursor()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    adminUI = AdminUI(db, cursor)
    adminUI.show()
    sys.exit(app.exec_())