from addAddressDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QMessageBox

class AddAddressDialog(QWidget, Ui_Dialog):
    def __init__(self, db, dbcursor, Bid):
        super(AddAddressDialog, self).__init__()
        self.setupUi(self)

        self.db = db
        self.dbcursor = dbcursor
        self.Bid = Bid

        self.pushButton.clicked.connect(self.confirm)

    def confirm(self):
        if self.RnameLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '收件人不能为空')
        elif self.TelLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '电话号码不能为空')
        elif self.infoAddressTextBrowser.toPlainText() == '':
            QMessageBox.warning(self, 'Warning', '收件地址不能为空')
        elif self.postcode.text() == '':
            QMessageBox.warning(self, 'Warning', '邮政编码不能为空')
        elif len(self.TelLineEdit.text()) != 11:
            QMessageBox.warning(self, 'Warning', '请输入正确的电话号码')
        elif len(self.postcodeLineEdit.text()) != 6:
            QMessageBox.warning(self, 'Warning', '请输入正确的邮政编码')
        else:

            self.sql = 'select Aid from addressbook;'
            self.dbcursor.execute(self.sql)
            self.data = self.dbcursor.fetchall()

            if len(self.data) == 0:
                self.Aid = '001'
            else:
                if int(self.data[-1][0]) > 98:
                    self.Aid = str(int(self.data[-1][0]) + 1)
                elif 99 > int(self.data[-1][0]) > 8:
                    self.Aid = '0' + str(int(self.data[-1][0]) + 1)
                elif int(self.data[-1][0]) < 9:
                    self.Aid = '00' + str(int(self.data[-1][0]) + 1)

            self.sql = 'insert into addressbook(Aid, Bid, address, Rname, Tel, postcode) ' \
                       'value (\"' + self.Aid + '\", \"' + self.Bid + '\", \"' + self.infoAddressTextBrowser.toPlainText() \
                       + '\", \"' + self.RnameLineEdit.text() + '\", \"' + self.TelLineEdit.text() + '\", \"' \
                       + self.postcodeLineEdit.text() + '\");'
            self.dbcursor.execute(self.sql)
            self.db.commit()

            QMessageBox.information(self, 'Information', '添加成功')
            self.close()