from PyQt5.QtWidgets import QWidget, QMessageBox
from addCommodityDialog import Ui_Dialog
import pymysql

class AddCommodityDialog(QWidget, Ui_Dialog):

    def __init__(self, db, dbcursor, Sid):
        super(AddCommodityDialog, self).__init__()
        self.setupUi(self)

        self.db = db
        self.dbcursor = dbcursor
        self.Sid = Sid

        self.WidLineEdit.editingFinished.connect(self.autoAddress)
        self.pushButton.clicked.connect(self.confirm)

    def autoAddress(self):
        try:
            self.sql = 'select address from warehouse where Wid = \"' + self.WidLineEdit.text() + '\";'
            self.dbcursor.execute(self.sql)
            self.data = self.dbcursor.fetchone()
            self.addressTextEdit.setText(str(self.data[0]))
        except:
            QMessageBox.warning(self, 'Warning', '这是一个新的仓库')

    def confirm(self):
        if self.nameLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '商品名不能为空')
        elif self.addressTextEdit.toPlainText() == '':
            QMessageBox.warning(self, 'Warning', '仓库地址不能为空')
        else:
            if self.sizeLineEdit == '':
                self.sizeLineEdit.setText('-')

            self.sql = 'select Cid from commodity;'
            self.dbcursor.execute(self.sql)
            self.data = self.dbcursor.fetchall()

            if len(self.data) == 0:
                self.Cid = '001'
            else:
                if int(self.data[-1][0]) > 98:
                    self.Cid = str(int(self.data[-1][0]) + 1)
                elif 99 > int(self.data[-1][0]) > 8:
                    self.Cid = '0' + str(int(self.data[-1][0]) + 1)
                elif int(self.data[-1][0]) < 9:
                    self.Cid = '00' + str(int(self.data[-1][0]) + 1)

            self.sql = 'insert into warehouse(Wid, stockCid, stockSize, stock, address) ' \
                       'value (\"' + self.WidLineEdit.text() + '\", \"' + self.Cid + '\", \"' + self.sizeLineEdit.text() \
                       + '\", \"' + self.stockSpinBox.text() + '\", \"' + self.addressTextEdit.toPlainText() + '\");'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            self.sql = 'insert into commodity(Cid, Sid, Wid, stockSize, Cname, price, discount, Cdescribe) ' \
                       'value (\"' + self.Cid + '\", \"' + self.Sid + '\", \"' + self.WidLineEdit.text() + '\", \"' \
                       + self.sizeLineEdit.text() + '\", \"' + self.nameLineEdit.text() + '\", \"' \
                       + self.priceSpinBox.text() + '\", \"' + self.discountDoubleSpinBox.text() + '\", \"' \
                       + self.describeTextEdit.toPlainText() + '\");'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            QMessageBox.information(self, 'Information', '添加成功')
            self.close()