from forgotDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QMessageBox
import pymysql


class forgotDialog(QWidget, Ui_Dialog):

    def __init__(self, db, dbcursor, index, name, data):
        super(forgotDialog, self).__init__()
        self.setupUi(self)
        self.db = db
        self.dbcursor = dbcursor
        self.index = index
        self.name = name
        self.data = data

        self.que1Label.setText(self.data[0])
        self.que2Label.setText(self.data[2])

        if self.data[0] == '':
            self.ans1LineEdit.setEnabled(False)
        if self.data[2] == '':
            self.ans2LineEdit.setEnabled(False)

        self.pushButton.clicked.connect(self.conform)

    def conform(self):
        if self.ans1LineEdit.text() == self.data[1] and self.ans2LineEdit.text() == self.data[3] \
                and self.keyLineEdit.text() == self.confirmLineEdit.text():
            if self.keyLineEdit.text() == '':
                QMessageBox.warning(self, 'Warning', '密码不能为空')
            else:
                if self.index == 0:
                    self.sql = 'update buyer set Bkey = \"' + self.keyLineEdit.text() + '\" where Bname = \"' \
                               + self.name + '\";'
                elif self.index == 1:
                    self.sql = 'update store set Bkey = \"' + self.keyLineEdit.text() + '\" where Sname = \"' \
                               + self.name + '\";'
                self.dbcursor.execute(self.sql)
                self.db.commit()
                QMessageBox.information(self, 'Information', '修改成功')
                self.close()

        elif self.ans1LineEdit.text() != self.data[1] or self.ans2LineEdit.text() != self.data[3]:
            QMessageBox.warning(self, 'Warning', '回答错误')
            self.ans1LineEdit.clear()
            self.ans2LineEdit.clear()

        elif self.keyLineEdit.text() != self.confirmLineEdit.text():
            QMessageBox.warning(self, 'Warning', '两次密码不一致')
            self.keyLineEdit.clear()
            self.confirmLineEdit.clear()
