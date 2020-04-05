import sys
from GUI import *
from PyQt5.QtGui import QIcon
import pymysql


class GUI(Ui_MainWindow):
    __sql = ''

    def setupFunction(self):
        self.connectButton.clicked.connect(self.connectDatabase)
        self.disconnectButton.clicked.connect(self.disconnectDatabase)

        self.clearButtonSelect.clicked.connect(self.clearSelect)
        self.doButtonSelect.clicked.connect(self.doSelect)

    def connectDatabase(self):
        try:
            self.__db = pymysql.connect(self.hostLineEdit.text(), self.userNameLineEdit.text(), self.keyLineEdit.text(),
                                        self.databaseLineEdit.text())
            self.__cursor = self.__db.cursor()
            self.statusbar.showMessage("Connected")
        except:
            self.statusbar.showMessage("Error in connecting MySQL")

    def disconnectDatabase(self):
        try:
            self.__db.close()
            self.statusbar.showMessage("Disconnected")
        except:
            self.statusbar.showMessage("Error in connecting MySQL")

    def clearSelect(self):
        self.enameCheckBoxSelect.setCheckState(False)
        self.essnCheckBoxSelect.setCheckState(False)
        self.addressCheckBoxSelect.setCheckState(False)
        self.superssnCheckBoxSelect.setCheckState(False)
        self.dnoCheckBoxSelect.setCheckState(False)
        self.enameLineEditSelect.clear()
        self.essnLineEditSelect.clear()
        self.addressLineEditSelect.clear()
        self.superssnLineEditSelect.clear()
        self.dnoLineEditSelect.clear()

    def doSelect(self):
        conditionNum = 0
        self.__sql = 'SELECT *\nFROM employee\nWHERE '

        if self.enameCheckBoxSelect.isChecked():
            conditionNum += 1
            self.__sql += "ename = \"" + self.enameLineEditSelect.text() + "\""
        elif self.essnCheckBoxSelect.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += " and "
            self.__sql += "essn = \"" + self.essnLineEditSelect.text() + "\""
        elif self.addressCheckBoxSelect.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += " and "
            self.__sql += "address like \"%" + self.addressLineEditSelect.text() + "%\""
        elif self.superssnCheckBoxSelect.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += " and "
            self.__sql += "superssn = \"" + self.superssnLineEditSelect.text() + "\""
        elif self.dnoCheckBoxSelect.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += " and "
            self.__sql += "dno = \"" + self.dnoLineEditSelect.text() + "\""
        self.__sql += ";"

        self.sqlTextBrowser.setText(self.__sql)

        try:
            self.__cursor.execute(self.__sql)
            data = self.__cursor.fetchall()

            self.resulTableWidget.setRowCount(len(data))
            self.resulTableWidget.setColumnCount(6)
            self.resulTableWidget.setHorizontalHeaderLabels(["姓名", "编号", "地址", "工资", "领导编号", "部门编号"])

            self.resulTableWidget.resizeRowsToContents()
            self.resulTableWidget.setColumnWidth(0, 50)
            self.resulTableWidget.setColumnWidth(1, 50)
            self.resulTableWidget.setColumnWidth(2, 200)
            self.resulTableWidget.setColumnWidth(3, 75)
            self.resulTableWidget.setColumnWidth(4, 75)
            self.resulTableWidget.setColumnWidth(5, 75)

            for i in range(0, len(data)):
                for j in range(0, 6):
                    self.resulTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

                self.statusbar.showMessage("Select successfully. Total " + str(len(data)) + " items")

        except:
            self.statusbar.showMessage("Error in SELECT SQL")



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
