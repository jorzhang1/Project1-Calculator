from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that connects the calculator UI to code
    """

    def __init__(self):
        """
        A method that sets up the calculator UI
        and connects the buttons to code
        """
        super().__init__()
        self.setupUi(self)

        # numbers
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
        self.total_input = []

    def num_clicked(self):
        """
        A method that reads input when the user clicks a number
        """
        button = self.sender()
        number = button.text()

        if number.isdigit() or number == '.':
            self.push_clear.setText("C")

        if number == '.':
            if '.' not in self.current_input:
                self.total_input.append(number)
                self.current_input.append(number)
        else:
            self.total_input.append(int(number))
            self.current_input.append(int(number))
            print('current', self.current_input)
            print('total', self.total_input)

        ans = "".join(map(str, self.total_input))
        self.ans_label.setText(ans)

    def calculate(self):
        """
        A method that reads input when the user clicks an operation
        """
        button = self.sender()
        operation = button.text()
        self.current_input = [operation]

        if len(self.total_input) > 0:
            if type(self.total_input[-1]) is int:
                self.total_input.append(operation)
                ans = "".join(map(str, self.total_input))
                self.ans_label.setText(ans)

    def submit(self):
        """
        A method that calculators an answer when the user clicks the equal button
        """
        pass

    def clear_input(self):
        """
        A method that clears the current input on the calculator screen
        """
        operators = ['×', '−', '+', '÷']
        has_operator = any(op in self.total_input for op in operators)

        if not has_operator:
            self.total_input = []
            self.ans_label.setText("")
        elif type(self.total_input[-1]) is str:
            self.total_input.pop()
            ans = "".join(map(str, self.total_input))
            self.ans_label.setText(ans)
        else:
            for i in reversed(self.total_input):
                if type(i) is not str:
                    self.total_input.pop()
                else:
                    break
            ans = "".join(map(str, self.total_input))
            self.ans_label.setText(ans)
