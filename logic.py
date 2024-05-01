from PyQt6.QtWidgets import *
from gui import *


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
        self.push_decimal.clicked.connect(self.num_clicked)

        #operators
        self.push_divide.clicked.connect(self.calculate)
        self.push_multiply.clicked.connect(self.calculate)
        self.push_minus.clicked.connect(self.calculate)
        self.push_add.clicked.connect(self.calculate)

        self.push_submit.clicked.connect(self.submit)
        self.push_clear.clicked.connect(self.clear_input)

        self.current_input = []

    def num_clicked(self):
        button = self.sender()
        number = button.text()

        if number.isdigit() or number == '.':
            self.push_clear.setText("C")

        if number == '.':
            if '.' not in self.current_input:
                self.current_input.append(number)
        else:
            self.current_input.append(int(number))

        ans = "".join(map(str, self.current_input))
        self.ans_label.setText(ans)
        print(self.current_input)

    def calculate(self):
        button = self.sender()
        operation = button.text()
        if len(self.current_input) > 0:
            if type(self.current_input[-1]) is int:
                self.current_input.append(operation)
                print(self.current_input)

    def submit(self):
        pass

    def clear_input(self):
        operators = ['×','−','+','÷']
        has_operator = any(op in self.current_input for op in operators)

        if not has_operator:
            self.current_input = []
            self.ans_label.setText("")
        elif type(self.current_input[-1]) is str:
            self.current_input.pop()
            ans = "".join(map(str, self.current_input))
            self.ans_label.setText(ans)
            print(self.current_input)
        else:
            for i in reversed(self.current_input):
                if type(i) is not str:
                    self.current_input.pop()
                else:
                    break
            ans = "".join(map(str, self.current_input))
            self.ans_label.setText(ans)
            print(self.current_input)

