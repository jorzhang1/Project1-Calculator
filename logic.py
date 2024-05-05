from PyQt6.QtWidgets import *

import formulas
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that connects the calculator UI to code
    """
    result = None

    def __init__(self):
        """
        A method that sets up the calculator UI
        and connects the buttons to code
        """
        super().__init__()
        self.setupUi(self)
        self.operators = ['×', '−', '+', '÷']

        # numbers
        self.push_zero.clicked.connect(self.num_clicked)
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

        # operators
        self.push_divide.clicked.connect(self.calculate)
        self.push_multiply.clicked.connect(self.calculate)
        self.push_minus.clicked.connect(self.calculate)
        self.push_add.clicked.connect(self.calculate)

        self.push_submit.clicked.connect(self.submit)
        self.push_clear.clicked.connect(self.clear_input)

        self.current_input = []

    def num_clicked(self):
        """
        A method that reads input when the user clicks a number
        """
        button = self.sender()
        number = button.text()

        if number.isdigit() or number == '.':
            self.push_clear.setText("C")

            if ((not self.current_input or self.current_input[-1] in self.operators) or
                    self.current_input == self.result):
                self.current_input.append(number)
            else:
                self.current_input[-1] += number

        ans = self.current_input[-1] if self.current_input else "0"
        self.ans_label.setText(ans)
        print(self.current_input)

    def calculate(self):
        """
        A method that reads input when the user clicks an operation
        """
        button = self.sender()
        operation = button.text()
        if len(self.current_input) > 0 and self.current_input[-1] != '.':
            self.current_input.append(operation)

    def submit(self):
        """
        A method that calculates an answer when the user clicks the equal button
        """

        try:
            if len(self.current_input) > 2:
                self.result = 0
                if self.current_input[1] == '×':
                    self.result = formulas.multiply([float(self.current_input[0]), float(self.current_input[2])])
                elif self.current_input[1] == '÷':
                    self.result = formulas.divide([float(self.current_input[0]), float(self.current_input[2])])
                elif self.current_input[1] == '+':
                    self.result = formulas.add([float(self.current_input[0]), float(self.current_input[2])])
                elif self.current_input[1] == '-':
                    self.result = formulas.subtract([float(self.current_input[0]), float(self.current_input[2])])

                self.current_input = [str(self.result)]
                self.ans_label.setText(str(self.result))
                print(self.current_input)
        except ValueError:
            print('Must enter a number')

    def clear_input(self):
        """
        A method that clears the current input on the calculator screen
        """
        has_operator = any(op in self.current_input for op in self.operators)

        if not has_operator:
            self.current_input = []
            self.ans_label.setText("")
            self.push_clear.setText("A/C")
        elif type(self.current_input[-1]) is str:
            self.current_input.pop()
            ans = "".join(map(str, self.current_input))
            self.ans_label.setText(ans)
        else:
            for i in reversed(self.current_input):
                if type(i) is not str:
                    self.current_input.pop()
                else:
                    break
            ans = "".join(map(str, self.current_input))
            self.ans_label.setText(ans)
