def check_isdigit(n):
    f = 1
    try:
        float(n)
    except ValueError:
        f = 0
    while f == 0:
        n = input("Not a number. Enter a number: ")
        try:
            float(n)
            f = 1
        except ValueError:
            f = 0
    return float(n)
while True:
    number_1 = check_isdigit(input('Enter your first number: '))
    operation = input('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        q for exit
        ''')
    if operation == 'q':
        print('Exit')
        break
    if operation in ('+', '-', '*', '/'):
        number_2 = check_isdigit(input('Enter your second number: '))
        if operation == '+':
            print(number_1 + number_2)
        elif operation == '-':
            print(number_1 - number_2)
        elif operation == '*':
            print(number_1 * number_2)
        elif operation == '/':
            if number_2 != 0:
                print(number_1 / number_2)
            else:
                print("Division by zero is not allowed!")
    else:
        print('You have not typed a valid operator, please try again.')
