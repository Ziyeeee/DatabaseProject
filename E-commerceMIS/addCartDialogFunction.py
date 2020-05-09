from addCartDialog import Ui_Dialog
from PyQt5.QtWidgets import QWidget


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

        self.numLineEdit.editingFinished.connect(self.showLineEdit())
        self.numHorizontalSlider.valueChanged.connect(self.showHorizontalSlider)

    def showLineEdit(self):
        self.numLineEdit.setText(str(self.numHorizontalSlider.value()))

    def showHorizontalSlider(self):
        self.numHorizontalSlider.setValue(self.numLineEdit.text())

