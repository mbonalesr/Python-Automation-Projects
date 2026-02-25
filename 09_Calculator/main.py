import os
os.system('cls')
from art import logo

def add(n1, n2):
    """Gets 2 numbers and returns the sum"""
    return n1 + n2


def subtract(n1, n2):
    """Gets 2 numbers and returns the subtraction"""
    return n1 - n2


def multiply(n1, n2):
    """Gets 2 numbers and returns the multiplication"""
    return n1 * n2


def divide(n1, n2):
    """Gets 2 numbers and returns the division"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num_1 = float(input("What's the first number: "))
    
    should_continue = True

    while should_continue:
        for operation in operations.keys():
            print(operation)

        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol] # obtaining operation from dictionary

        num_2 = float(input("What's the next number: "))

        answer = calculation_function(n1=num_1, n2=num_2) # linking the numbers with the correct function through symbol

        print(f"{num_1} {operation_symbol} {num_2} = {answer}") # showing results

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num_1 = answer
        elif choice == 'n':
            os.system('cls') # clearing screen
            calculator()
        else:
            print("Please write ONLY 'y' or 'n'")
            break

calculator()
