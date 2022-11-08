print('''
Wellcome to the magic calculator, where everything is simple.
You can use different calculation. If You press:
1 - add
2 - subtraction
3 - multiplication
4 - division
5 - dvision with the rest
6 - rest of the division
7 - square root
8 - new number
''')

while True:
    try:
        x = int(input("Enter a first number: "))
        y = int(input("Enter a second number: "))
        break
    except ValueError:
        print("Put a number!")

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        print("You can not divide by zero.")
    else:
        return x / y

def divide_rest(x, y):
    if y == 0:
        print("You can not divide by zero.")
    else:
        return x // y

def divide_modulo(x, y):
    if y == 0:
        print("You can not divide by zero.")
    else:
        return x % y

def square(x, y):
    return x ** y

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))

        elif choice == '5':
            print(x, "//", y, "=", divide_rest(x, y))

        elif choice == '6':
            print(x, "%", y, "=", divide_modulo(x, y))

        elif choice == '7':
            print(x, "**", y, "=", square(x, y))

        elif choice == '8':
            while True:
                try:
                    x = int(input("Enter a first number: "))
                    y = int(input("Enter a second number: "))
                    break
                except ValueError:
                    print("Put a number!")
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
