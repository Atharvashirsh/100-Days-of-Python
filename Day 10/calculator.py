# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))

    calculateMore = True
    while calculateMore:
        for operators in operations:
            print(operators, end=" ")
        operation_symbol = input("\nPick an operation from the line above: ")

        num2 = float(input("What is the next number? "))

        operation_function = operations[operation_symbol]
        first_answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")

        check = input(
            f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation, or type 'q' to quit: "
        ).lower()

        if check == "n":
            calculateMore = False
            calculator()
        elif check == "q":
            calculateMore = False
            print("Goodbye!!")
        else:
            num1 = first_answer


calculator()
