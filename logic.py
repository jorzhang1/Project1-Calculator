from PyQt6.QtWidgets import *
from calculator import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        #numbers
        self.push_one.clicked.connect(self.num_clicked)
        self.push_two.clicked.connect(self.num_clicked)
        self.push_three.clicked.connect(self.num_clicked)
        self.push_four.clicked.connect(self.num_clicked)
        self.push_five.clicked.connect(self.num_clicked)
        self.push_six.clicked.connect(self.num_clicked)
        self.push_seven.clicked.connect(self.num_clicked)
        self.push_eight.clicked.connect(self.num_clicked)
        self.push_nine.clicked.connect(self.num_clicked)

        #operators
        self.push_divide.clicked.connect(self.calculate)
        self.push_multiply.clicked.connect(self.calculate)
        self.push_minus.clicked.connect(self.calculate)
        self.push_add.clicked.connect(self.calculate)

        self.push_submit.clicked.connect(self.submit)
        self.push_clear.clicked.connect(self.clear_input)

        self.current_input = []

    def num_clicked(self):
        if len(self.current_input) < 1:

        if self.push_one:
            self.current_input.append(1)
        elif self.push_two:
            self.current_input.append(2)
        elif self.push_three:
            self.current_input.append(3)
        elif self.push_four:
            self.current_input.append(4)
        elif self.push_five:
            self.current_input.append(5)
        elif self.push_six:
            self.current_input.append(6)
        elif self.push_seven:
            self.current_input.append(7)
        elif self.push_eight:
            self.current_input.append(8)
        elif self.push_nine:
            self.current_input.append(9)

        self.ans_label.setText("".join(self.current_input))

    def calculate(self):
        pass

    def submit(self):
        pass




    def clear_input(self):
        pass
