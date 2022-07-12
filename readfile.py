############## Calculator operations ##############

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

operations = {'x': multiply, '+': add, '-': subtract, '/': divide}

############## Commands ##############

def calc(op, a, b):
    return operations[op](a, b)

commands = {'calc': calc}

############## Other methods ##############

def calculateLine(line):
    li = line.split(' ')
    return commands[li[0]](li[1], int(li[2]), int(li[3]))

############## Main program ##############

with open("step_2.txt", 'r') as f:
    lines = f.read().splitlines()
    calculations = [calculateLine(line) for line in lines]
    print(sum(calculations))

with open('outputs.txt', 'w') as f:
    for calc in calculations:
        f.write(f"{calc}\n")
        