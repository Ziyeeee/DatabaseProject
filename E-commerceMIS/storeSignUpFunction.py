from storeSignUpDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QMessageBox
import pymysql


class storeDialog(QWidget, Ui_Dialog):

    def __init__(self, db, dbcursor):
        super(storeDialog, self).__init__()
        self.setupUi(self)
        self.db = db
        self.dbcursor = dbcursor

        self.pushButton.clicked.connect(self.signUp)

    def signUp(self):
        if self.nameLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '昵称不能为空')

        elif self.keyLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '密码不能为空')

        elif self.keyLineEdit.text() != self.confirmLineEdit.text():
            QMessageBox.warning(self, 'Warning', '两次密码不一致')

        elif self.principalLineEdit.text() == '':
            QMessageBox.warning(self, 'Warning', '负责人不能为空')

        elif len(self.IDLineEdit.text()) != 18:
            QMessageBox.warning(self, 'Warning', '请输入18位身份证号')

        elif len(self.TelLineEdit.text()) != 11:
            QMessageBox.warning(self, 'Warning', '请输入正确的手机号码')

        else:
            self.sql = 'select Sid from store;'
            self.dbcursor.execute(self.sql)
            self.data = self.dbcursor.fetchall()

            if len(self.data) == 0:
                self.id = '001'
            else:
                if int(self.data[-1][0]) > 98:
                    self.id = str(int(self.data[-1][0]) + 1)
                elif 99 > int(self.data[-1][0]) > 8:
                    self.id = '0' + str(int(self.data[-1][0]) + 1)
                elif int(self.data[-1][0]) < 9:
                    self.id = '00' + str(int(self.data[-1][0]) + 1)

            self.sql = 'insert into store(Sid, Sname, Tel, Scredit, principal, ID_card, Bkey, BkeyProtect1, BkeyAns1, BkeyProtect2, BkeyAns2) ' \
                       'value (\"' + self.id + '\", \"' + self.nameLineEdit.text() + '\", \"' + self.TelLineEdit.text() \
                       + '\", \"1", \"' + self.principalLineEdit.text() + '\", \"' + self.IDLineEdit.text() + '\", \"' \
                       + self.keyLineEdit.text() + '\", \"' + self.que1LineEdit.text() + '\", \"' + self.ans1LineEdit.text() \
                       + '\", \"' + self.que2LineEdit.text() + '\", \"' + self.ans2LineEdit.text() + '\");'
            self.dbcursor.execute(self.sql)
            self.db.commit()
            QMessageBox.information(self, 'Information', '注册成功')
            self.close()
