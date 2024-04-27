from formulas import *
from logic import *
def main():
    terminal = sys.argv

    if len(terminal) <= 1:
        sys.exit('Need to provide operator')
    elif len(terminal) <= 3:
        sys.exit('Need to provide at least two values')

    operator = terminal[1]
    numbers = terminal[2:]
    numbers = [float(num) for num in numbers]

    if operator == 'add':
        print(f'Answer = {formulas.add(numbers):.2f}')
    elif operator == 'subtract':
        print(f'Answer = {formulas.subtract(numbers):.2f}')
    elif operator == 'multiply':
        print(f'Answer = {formulas.multiply(numbers):.2f}')
    elif operator == 'divide':
        print(f'Answer = {formulas.divide(numbers):.2f}')
    else:
        sys.exit('Valid operator names (add, subtract, multiply, divide)')

    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
