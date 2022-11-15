import math

print('''
Virtual calculator with which you can perform the following math operations:
+ - adding;
- - subtraction;
* - multiplication;
/ - sharing with the rest;
^ - square root with remainder.
''')

def add(x, y):
    return x + y

# This function subtracts two numbers
def sub(x, y):
    return x - y

# This function multiplies two numbers
def mul(x, y):
    return x * y

# This function divides two numbers
def floordiv(x, y):
    if y == 0:
        print("You can not divide by zero.")
    else:
        div = x // y
        rest = x % y
        return div, rest

# Square root with rest
def r_sqrt(x):
    sq_all = math.floor(x ** (1/2))
    power = sq_all * sq_all
    rest = x - power
    return sq_all, rest


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
    "^": r_sqrt
}

a = int(input("Enter first number: "))

if a > 0:
    op = None
    while op not in ("+", "-", "*", "/", "^"):
        op = input("Enter operator (+, -, *, /, ^):  ")
        if op == "^": 
            print(f"Square root {a} = {r_sqrt(a)}")
        else:

            operation = operations[op]

            b = int(input("Enter second number: "))

            result = operation(a, b)

            print(f"{a} {op} {b} = {result}")
else:
    print('Only natural numbers')
