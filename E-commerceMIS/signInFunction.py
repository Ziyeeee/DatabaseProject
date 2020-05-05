import sys
from PyQt5 import QtWidgets
from signIn import Ui_Form


class SignIn(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(SignIn, self).__init__()
        self.setupUi(self)

        __sql = ''

        self.chooseComboBox.currentIndexChanged.connect(self.comboBoxChanged)
        self.forgotPushButton.clicked.connect()

    def comboBoxChanged(self):
        if self.chooseComboBox.currentIndex() == 2:
            self.forgotPushButton.setEnabled(False)
            self.signUpPushButton.setEnabled(False)
        else:
            self.forgotPushButton.setEnabled(True)
            self.signUpPushButton.setEnabled(True)

    def forgotKey(self):
        



def showSignInUI():
        app = QtWidgets.QApplication(sys.argv)
        signInUI = SignIn()
        signInUI.show()
        sys.exit(app.exec_())