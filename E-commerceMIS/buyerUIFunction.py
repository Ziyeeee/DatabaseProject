from PyQt5.QtWidgets import QMessageBox, QWidget
from buyerUI import Ui_Form
import pymysql


class BuyerUI(QWidget, Ui_Form):
    def __init__(self):
        super(BuyerUI, self).__init__()
        self.setupUi(self)