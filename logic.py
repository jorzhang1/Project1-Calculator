from PyQt6.QtWidgets import *
from decimal import Decimal
import csv
import formulas
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
        self.operators = ['×', '-', '+', '÷']

        self.historyButton.clicked.connect(self.history)
        self.expanded = False

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

        self.push_negative.clicked.connect(self.negative)
        self.push_percentage.clicked.connect(self.percentage)
        self.push_submit.clicked.connect(self.submit)
        self.push_clear.clicked.connect(self.clear_input)

        self.result = 0
        self.current_input = []

    def num_clicked(self):
        """
        A method that reads input when the user clicks a number
        """
        self.ans_label.setStyleSheet("color: grey;")
        button = self.sender()
        number = button.text()

        if number.isdigit() or number == '.':
            self.push_clear.setText("C")

            if self.current_input:
                if '.' in self.current_input[-1]:
                    if number == '.':
                        return
                    else:
                        self.current_input[-1] += number
                elif self.current_input[-1] in self.operators:
                    if number == '.':
                        return
                    else:
                        self.current_input.append(number)
                else:
                    self.current_input[-1] += number

            else:
                if number == '.':
                    self.current_input.append("0.")
                else:
                    self.current_input.append(number)

        ans = self.current_input[-1] if self.current_input else number
        self.ans_label.setText(ans)
        print(self.current_input)

        """
        if number.isdigit() or number == '.':
            self.push_clear.setText("C")
            
            if self.current_input
                if len(self.current_input) < 2 and '.' in self.current_input[-1]:
                    if number == '.':
                        return
                elif self.current_input[-1] in self.operators:
                    return
                else:
                    self.current_input.append(number)
            else:
                self.current_input[-1] += number
            
                
                
            
        
        """

    def negative(self):
        """
        A method that adds a negative sign to the input
        """
        if self.current_input:
            if self.current_input[-1] in self.operators:
                return
            if '-' in self.current_input[-1]:
                self.current_input[-1] = self.current_input[-1][1:]
            else:
                self.current_input[-1] = '-' + self.current_input[-1]

        ans = self.current_input[-1] if self.current_input else ""
        self.ans_label.setText(ans)

    def percentage(self):
        """
        Method to change input into percentage
        """
        if self.current_input:
            last_input = self.current_input[-1]
            if last_input.lstrip('-').replace('.', '', 1).isdigit():
                num = Decimal(last_input)
                num /= Decimal('100')
                self.current_input[-1] = str(num)
                self.ans_label.setText(self.current_input[-1])

    def calculate(self):
        """
        A method that reads input when the user clicks an operation
        """
        button = self.sender()
        operation = button.text()
        if self.current_input:
            if len(self.current_input) < 2:
                self.current_input.append(operation)
            elif len(self.current_input) > 1 and self.current_input[-1] in self.operators:
                self.current_input.pop()
                self.current_input.append(operation)
            else:
                self.submit()
        print(self.current_input)

    def submit(self):
        """
        A method that calculates an answer when the user clicks the equal button
        """
        try:
            if len(self.current_input) == 3:
                num1 = Decimal(self.current_input[0])
                num2 = Decimal(self.current_input[2])
                operator = self.current_input[1]

                if operator == '×':
                    self.result = formulas.multiply([num1, num2])
                elif operator == '÷':
                    self.result = formulas.divide([num1, num2])
                elif operator == '+':
                    self.result = formulas.add([num1, num2])
                elif operator == '-':
                    self.result = formulas.subtract([num1, num2])

                self.write_history()
                self.current_input = [str(self.result)]
                self.ans_label.setText(str(self.result))

        except ValueError as e:
            self.ans_label.setText(str(e))
            self.ans_label.setStyleSheet("color: red;")
            self.current_input = []
            print(self.current_input)

    def clear_input(self):
        """
        A method that clears the current input on the calculator screen
        """
        if self.current_input:
            if len(self.current_input) == 3:
                self.current_input.pop()
            else:
                self.current_input = []
            self.ans_label.setText("")
            self.push_clear.setText("A/C")

    def history(self):
        if self.expanded:
            self.setFixedWidth(580)
            self.expanded = False
            self.historyLabel.setEnabled(False)
        else:
            self.setFixedWidth(900)
            self.expanded = True
            self.historyLabel.setEnabled(True)

        label = ''
        try:
            with open('history.csv', 'r') as history_file:
                reader = csv.reader(history_file)
                history_data = list(reader)
                for row in history_data:
                    label += str(f"<p style='margin-bottom: 10px;'>{row[0]} {row[1]} {row[2]} = {row[3]}\n</p>")
                self.historyLabel.setText(label)
                self.historyLabel.setStyleSheet("font-size: 12pt;")

        except FileNotFoundError:
            print('hi')
            self.historyLabel.setText("There's not history yet")

    def write_history(self):
        try:
            with open('history.csv', 'a', newline='') as history_file:
                contents = csv.writer(history_file)
                contents.writerow([self.current_input[0], self.current_input[1], self.current_input[2], self.result])
                print('Write successful:',
                      [self.current_input[0], self.current_input[1], self.current_input[2], self.result])
        except Exception as e:
            print('Error writing to history:', e)
