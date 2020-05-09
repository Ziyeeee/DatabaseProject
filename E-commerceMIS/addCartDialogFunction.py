from addCartDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QMessageBox


class AddCartDialog(QWidget, Ui_Dialog):
    def __init__(self, db, dbcursor, Bid, Cid, name, stockSize, stock):
        super(AddCartDialog, self).__init__()
        self.setupUi(self)

        self.db = db
        self.dbcursor = dbcursor
        self.Bid = Bid
        self.Cid = Cid
        self.name = name
        self.stockSize = stockSize
        self.stock = stock

        self.nameLabel.setText(self.name)
        self.stockLabel.setText('库存' + str(self.stock) + '件')
        self.numHorizontalSlider.setMaximum(int(self.stock))

        self.numLineEdit.editingFinished.connect(self.showHorizontalSlider)
        self.numHorizontalSlider.valueChanged.connect(self.showLineEdit)
        self.pushButton.clicked.connect(self.addCart)

    def showLineEdit(self):
        self.numLineEdit.setText(str(self.numHorizontalSlider.value()))

    def showHorizontalSlider(self):
        self.numHorizontalSlider.setValue(int(self.numLineEdit.text()))

    def addCart(self):
        self.sql = 'insert into cart(Cid, Bid, size, num) ' \
                   'value (\"' + self.Cid + '\", \"' + self.Bid + '\", \"' + self.stockSize + '\", \"' \
                   + self.numLineEdit.text() + '\");'
        self.dbcursor.execute(self.sql)
        self.db.commit()

        QMessageBox.information(self, 'Information', '添加成功')
        self.close()