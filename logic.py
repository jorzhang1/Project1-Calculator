from PyQt6.QtWidgets import *
from calculator import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.push_submit.clicked.connect(self.submit)
        self.push_clear.clicked.connect(self.clear_input)
        self.ans_label.setText("")

    def submit(self):
        pass

    def clear_input(self):
        pass
