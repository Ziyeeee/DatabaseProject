import sys
from PyQt5 import QtWidgets
from signIn import Ui_Form
from forgotDialogFunction import forgotDialog


class SignIn(QtWidgets.QWidget, Ui_Form):

    def __init__(self, db, cursor):
        super(SignIn, self).__init__()
        self.setupUi(self)

        self.sql = ''
        self.db = db
        self.dbcursor = cursor

        self.chooseComboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.forgotPushButton.clicked.connect(self.forgotKey)

    def comboBoxChanged(self):
        if self.chooseComboBox.currentIndex() == 2:
            self.forgotPushButton.setEnabled(False)
            self.signUpPushButton.setEnabled(False)
        else:
            self.forgotPushButton.setEnabled(True)
            self.signUpPushButton.setEnabled(True)

    def forgotKey(self):
        if self.nameLineEdit.text() == '':
            QtWidgets.QMessageBox.warning(self, 'Warning', '昵称不能为空')
        else:
            if self.chooseComboBox.currentIndex() == 0:
                self.sql = 'select BkeyProtect1, BkeyAns1, BkeyProtect2, BkeyAns2 from buyer where Bname = \"' \
                           + self.nameLineEdit.text() + '\"'
            elif self.chooseComboBox.currentIndex() == 1:
                self.sql = 'select BkeyProtect1, BkeyAns1, BkeyProtect2, BkeyAns2 from store where Sname = \"' \
                           + self.nameLineEdit.text() + '\"'
            self.dbcursor.execute(self.sql)
            self.data = self.dbcursor.fetchone()
            if self.data == None:
                QtWidgets.QMessageBox.warning(self, 'Warning', '账户不存在')
                self.nameLineEdit.clear()
            else:
                self.forgotDialog = forgotDialog(self.db, self.dbcursor, self.chooseComboBox.currentIndex(),
                                                 self.nameLineEdit.text(), self.data)
                self.forgotDialog.show()

    def buyersignUp(self):
        pass




def showSignInUI(db, cursor):
        app = QtWidgets.QApplication(sys.argv)
        signInUI = SignIn(db, cursor)
        signInUI.show()
        sys.exit(app.exec_())