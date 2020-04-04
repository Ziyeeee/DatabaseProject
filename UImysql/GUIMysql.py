import sys
from GUI import *
from PyQt5.QtGui import QIcon



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.setupFunction()             #还没有添加操作函数
    MainWindow.setWindowTitle("Database Manager")
    MainWindow.setWindowIcon(QIcon("database.png"))
    MainWindow.show()
    sys.exit(app.exec_())
