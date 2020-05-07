from PyQt5.QtWidgets import QMessageBox, QWidget
from storeUI import Ui_Form
import pymysql


class StoreUI(QWidget, Ui_Form):
    def __init__(self):
        super(StoreUI, self).__init__()
        self.setupUi(self)