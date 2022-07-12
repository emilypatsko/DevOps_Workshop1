def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

methods = {'x': multiply, '+': add, '-': subtract, '/': divide}

while True:
    operation = input('What operation would you like to perform? ')
    if operation not in ['x', '+', '-', '/']:
        continue

    try:
        a = int(input('Enter a number: '))
    except:
        print('Please enter an integer.')
        continue

    try:
        b = int(input('Enter another number: '))
    except:
        print('Please enter an integer.')
        continue

    print(f'The answer to {str(a) + operation + str(b)} is {methods[operation](a, b)}')
    break
