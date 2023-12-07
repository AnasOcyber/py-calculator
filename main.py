from math import pow, sqrt


def addition(first, second):
    return first + second


def subtraction(first, second):
    if first > second:
        return first - second
    return second - first


def multiplication(first, second):
    return first * second


def division(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return f"\nHow can you divide something by zero?\nIn this case you are trying {first} / {second}.\nDid you mean {second} / {first}?\n"


def show_menu():
    print("\nOperations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print("6. Square Root")
    print("7. Quit\n")


while True:
    try:
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
    except ValueError:
        print("ERROR: This program expects a number.")
    else:
        show_menu()
        operation = int(input(
            "What operation do you want to perform? (1 - 5): "))

        if operation == 1:
            result = addition(first, second)
            print(result)
        elif operation == 2:
            result = subtraction(first, second)
            print(result)
        elif operation == 3:
            result = multiplication(first, second)
            print(result)
        elif operation == 4:
            result = division(first, second)
            print(result)
        elif operation == 5:
            print(int(pow(first, second)))

        elif operation == 6:
            print(f"Square root of {first}: {sqrt(first)}")
            print(f"Square root of {second}: {sqrt(second)}")
        elif operation == 7:
            break
        else:
            print("Bad choice!")


print("Have a nice day 😎")
