import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn.resize(btn.sizeHint())

        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('database.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
