import math

print('''
Virtual calculator with which you can perform the following math operations:
+ - adding;
- - subtraction;
* - multiplication;
/ - division with the rest;
^ - square root with rest;
end - end of the program.
''')

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def floordiv(x, y):
    if y == 0:
        print('You can not divide by zero.')
    else:
        div = x // y
        rest = x % y
        return div, rest

def r_sqrt(x):
    sq_all = math.floor(x ** (1/2))
    power = sq_all * sq_all
    rest = x - power
    return sq_all, rest


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv,
    '^': r_sqrt,
}


def calculator():
    try:   
        a = input('Enter first number or end of program: ')
        a = int(a)
    except ValueError:
        if a == 'end':
            pass
        else:
            print('Put a natural number!')
            return calculator()

    if a == 'end':
            print('End of program.')
            exit()

    if a >= 0:
        op = None
        while op not in ('+', '-', '*', '/', '^', 'end'):
            op = input('Enter operator (+, -, *, /, ^, end): ')
            try:
                if op == '^':
                    print(f'Square root {a} = {r_sqrt(a)}')
                elif op == 'end':
                    print('End of program.')
                    exit()
                else:

                    operation = operations[op]

                    try:   
                        b = int(input('Enter second number: '))
                    except ValueError:
                        print('Put a natural number!')

                    result = operation(a, b)

                    print(f'{a} {op} {b} = {result}')
            except KeyError:
                print('Enter only this operator (+, -, *, /, ^, end)')
    else:
        print('Only natural numbers')

    return calculator()

if __name__ == "__main__":
    print("Hello, World!")
    calc = calculator()