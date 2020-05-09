from buyDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QMessageBox

class BuyDialog(QWidget, Ui_Dialog):
    def __init__(self, db, dbcursor, Bid, Cid, Sid, stockSize, num, price, Dname, Daddresss, DTel):
        super(BuyDialog, self).__init__()
        self.setupUi(self)
        self.db = db
        self.dbcursor = dbcursor
        self.Bid = Bid
        self.Cid = Cid
        self.Sid = Sid
        self.stockSize = stockSize
        self.num = num
        self.price = price
        self.Dname = Dname
        self.Daddress = Daddresss
        self.DTel = DTel

        self.sql = 'select Rname, address, Tel from addressbook where Bid = \"' + self.Bid + '\";'
        self.dbcursor.execute(self.sql)
        self.RData = self.dbcursor.fetchall()

        for i in range(0, len(self.RData)):
            self.nameComboBox.addItem(self.RData[i][0])
        self.showAddress()

        self.nameComboBox.currentIndexChanged.connect(self.showAddress)
        self.pushButton.clicked.connect(self.confirm)

    def showAddress(self):
        self.addressTextBrowser.setText(self.RData[self.nameComboBox.currentIndex()][1])

    def confirm(self):
        self.sql = 'select stock from warehouse where stockCid = \"' + self.Cid + '\" and stockSize = \"' + self.stockSize + '\";'
        self.dbcursor.execute(self.sql)
        self.stock = self.dbcursor.fetchone()

        # warehouse
        if int(self.stock[0]) < self.num:
            QMessageBox.warning(self, 'Warning', '库存不足')
            self.close()
        elif int(self.stock[0]) == self.num:
            self.sql = 'delete from commodity where Cid = \"' + self.Cid + '\" and stockSize = \"' + self.stockSize + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'delete from warehouse where stockCid = \"' + self.Cid + '\" and stockSize = \"' + self.stockSize + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()
        else:
            self.sql = 'update warehouse set stock = \"' + str(int(self.stock[0]) - self.num) + '\" where stockCid = \"' \
                       + self.Cid + '\" and stockSize = \"' + self.stockSize + '\";'
            self.dbcursor.execute(self.sql)
            self.db.commit()

        # order
        self.sql = 'select Oid from orderform;'
        self.dbcursor.execute(self.sql)
        self.data = self.dbcursor.fetchall()

        if len(self.data) == 0:
            self.Oid = '001'
        else:
            if int(self.data[-1][0]) > 98:
                self.Oid = str(int(self.data[-1][0]) + 1)
            elif 99 > int(self.data[-1][0]) > 8:
                self.Oid = '0' + str(int(self.data[-1][0]) + 1)
            elif int(self.data[-1][0]) < 9:
                self.Oid = '00' + str(int(self.data[-1][0]) + 1)

        self.sql = 'insert into orderform(Oid, Bid, Sid, size, num, price, Lstatus) ' \
                   'value(\"' + self.Oid + '\",  \"' + self.Bid + '\",  \"' + self.Sid + '\",  \"' + self.stockSize \
                   + '\",  \"' + str(self.num) + '\",  \"' + str(self.price) + '\",  \"0\");'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        # commodity_order
        self.sql = 'insert into commodity_order(Oid, Cid, Csize) ' \
                   'value(\"' + self.Oid + '\", \"' + self.Cid + '\", \"' + self.stockSize + '\");'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        # logistics
        self.sql = 'select Lid from logistics;'
        self.dbcursor.execute(self.sql)
        self.data = self.dbcursor.fetchall()

        if len(self.data) == 0:
            self.Lid = '001'
        else:
            if int(self.data[-1][0]) > 98:
                self.Lid = str(int(self.data[-1][0]) + 1)
            elif 99 > int(self.data[-1][0]) > 8:
                self.Lid = '0' + str(int(self.data[-1][0]) + 1)
            elif int(self.data[-1][0]) < 9:
                self.Lid = '00' + str(int(self.data[-1][0]) + 1)
        self.sql = 'insert into logistics(Lid, Oid, Daddress, Dname, DTel, Raddress, Rname, RTel, Lstatus) ' \
                   'value(\"' + self.Lid + '\", \"' + self.Oid + '\", \"' + self.Daddress + '\", \"' + self.Dname \
                   + '\", \"' + self.DTel + '\", \"' + self.RData[self.nameComboBox.currentIndex()][1] + '\", \"' \
                   + self.RData[self.nameComboBox.currentIndex()][0] + '\", \"' \
                   + self.RData[self.nameComboBox.currentIndex()][2] + '\", \"0\");'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QMessageBox.information(self, 'Information', '购买成功')
        self.close()
