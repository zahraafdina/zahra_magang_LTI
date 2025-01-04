import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QIcon, QAction

from main_1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__== '_main_':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())