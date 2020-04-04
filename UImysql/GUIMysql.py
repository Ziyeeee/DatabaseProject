import sys
from GUI import *
from PyQt5.QtGui import QIcon
import pymysql


class GUI(Ui_MainWindow):
    def setupFunction(self):
        self.connectButton.clicked.connect(self.connectDatabase)

    def connectDatabase(self):
        try:
            self.__db = pymysql.connect(self.hostLineEdit.text(), self.userNameLineEdit.text(), self.keyLineEdit.text(),
                                        self.databaseLineEdit.text())
            self.__cursor = self.__db.cursor()
            self.statusbar.showMessage("Connected")
        except:
            self.statusbar.showMessage("Error in connecting MySQL")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(MainWindow)
    ui.setupFunction()
    MainWindow.setWindowTitle("Database Manager")
    MainWindow.setWindowIcon(QIcon("database.png"))
    MainWindow.show()
    sys.exit(app.exec_())
