import sys
from GUI import *
from PyQt5.QtGui import QIcon
import pymysql


class GUI(Ui_MainWindow):
    __sql = ''

    def setupFunction(self):
        self.setResultTable()
        self.connectButton.clicked.connect(self.connectDatabase)
        self.disconnectButton.clicked.connect(self.disconnectDatabase)

        self.clearButtonSelect.clicked.connect(self.clearSelect)
        self.doButtonSelect.clicked.connect(self.doSelect)

        self.clearButtonInsert.clicked.connect(self.clearInsert())
        self.doButtonInsert.clicked.connect(self.doInsert())

        self.clearButtonUpdate.clicked.connect()
        self.doButtonUpdate.clicked.connect()

    def setResultTable(self):
        self.resulTableWidget.setColumnCount(6)
        self.resulTableWidget.setHorizontalHeaderLabels(["姓名", "编号", "地址", "工资", "领导编号", "部门编号"])

        self.resulTableWidget.resizeRowsToContents()
        self.resulTableWidget.setColumnWidth(0, 50)
        self.resulTableWidget.setColumnWidth(1, 50)
        self.resulTableWidget.setColumnWidth(2, 200)
        self.resulTableWidget.setColumnWidth(3, 75)
        self.resulTableWidget.setColumnWidth(4, 75)
        self.resulTableWidget.setColumnWidth(5, 75)

    def dataToTableWidget(self, data):
        self.resulTableWidget.setRowCount(len(data))

        for i in range(0, len(data)):
            for j in range(0, 6):
                self.resulTableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

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
        self.__sql = "SELECT *\nFROM employee\nWHERE "

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

            self.dataToTableWidget(data)

            self.statusbar.showMessage("Select successfully. Total " + str(len(data)) + " items")

        except:
            self.statusbar.showMessage("Error in SELECT SQL")

    def clearInsert(self):
        self.enameLineEditInsert.clear()
        self.essnLineEditInsert.clear()
        self.addressLineEditInsert.clear()
        self.salaryLineEditInsert.clear()
        self.superssnLineEditInsert.clear()
        self.dnoLineEditInsert.clear()

    def doInsert(self):
        self.__sql = "insert into employee(essn, ename, address, salary, superssn, dno)\n"
        self.__sql += "value(\'" + self.essnLineEditInsert + "\', \'" + self.enameLineEditInsert + "\', \'" +\
                      self.addressLineEditInsert + "\', " + self.salaryLineEditInsert + ", \'" +\
                      self.superssnLineEditInsert + "\', \'" + self.dnoLineEditInsert + "\');"

        self.sqlTextBrowser.setText(self.__sql)

        try:
            self.__cursor.execute(self.__sql)
            self.__db.commit()

            self.__sql = "SELECT * FROM employee"
            self.__sql += "\'" + self.essnLineEditInsert + "\';"

            self.__cursor.execute(self.__sql)
            data = self.__cursor.fetchall()

            self.dataToTableWidget(data)

            self.statusbar.showMessage("Insert successfully.")

        except:
            self.statusbar.showMessage("Error in INSERT SQL")

    def clearUpdate(self):
        self.enameCheckBoxUpdate.setCheckState(False)
        self.addressCheckBoxUpdate.setCheckState(False)
        self.salaryCheckBoxUpdate.setCheckState(False)
        self.superssnCheckBoxUpdate.setCheckState(False)
        self.dnoCheckBoxUpdate.setCheckState(False)
        self.enameLineEditUpdate.clear()
        self.essnLineEditUpdate.clear()
        self.addressLineEditUpdate.clear()
        self.salaryLineEditUpdate.clear()
        self.superssnLineEditUpdate.clear()
        self.dnoLineEditUpdate.clear()

    def doUpdate(self):
        conditionNum = 0
        self.__sql = "UPDATE employee\n"

        if self.enameCheckBoxUpdate.isChecked():
            conditionNum += 1
            self.__sql += "SET ename = \"" + self.enameLineEditUpdate.text() + "\""
        elif self.addressCheckBoxUpdate.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += ", "
            self.__sql += "SET address like \"%" + self.addressLineEditUpdate.text() + "%\""
        elif self.superssnCheckBoxUpdate.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += ", "
            self.__sql += "SET superssn = \"" + self.superssnLineEditUpdate.text() + "\""
        elif self.dnoCheckBoxUpdate.isChecked():
            conditionNum += 1
            if conditionNum > 1:
                self.__sql += ", "
            self.__sql += "SET dno = \"" + self.dnoLineEditUpdate.text() + "\""
        self.__sql += ";"

        self.sqlTextBrowser.setText(self.__sql)

        try:
            self.__cursor.execute(self.__sql)
            self.__db.commit()

            self.__sql = "SELECT * FROM employee WHERE essn = "
            self.__sql += "\'" + self.essnLineEditUpdate + "\';"

            self.__cursor.execute(self.__sql)
            data = self.__cursor.fetchall()

            self.dataToTableWidget(data)

            self.statusbar.showMessage("Update successfully.")

        except:
            self.statusbar.showMessage("Error in UPDATE SQL")



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
