# Calculator

# Instruct Python to define each operation as a function (note that operators are in fact built-in functions in Python).

# Addition
def addition(n1, n2):
    return n1 + n2

# Subtract
def subtraction(n1, n2):
    return n1 - n2

# Multiply
def multiplication(n1, n2):
    return n1 * n2

# Divide
def division(n1, n2):
    return n1 / n2

# Instruct Python to memorise a collection of {key: value} pairs and call them by <operations_dictionary>. The keys are
# given as strings ("+", "-", "*", "/"), and their corresponding values call the functions we defined above (add,
# subtract, multiply, and divide). By this way, we call a function by calling its name from the dictionary.

operations_dictionary = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

from ex106_ASCIIArt import logo
print(logo)

def calculator():
    num1 = float(input("Choose a number?: "))
    for operator in operations_dictionary:
        print(operator)
    continue_calculation = True


    while continue_calculation:
        operation = input("Choose an operation from the options given above: ")
        num2 = float(input("Choose another number?: "))
        calculation_function = operations_dictionary[operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        calculate_more = input(
            f'Do you wish to continue calculating using {answer} as your first number? Type "Y" or "N": ').lower()

        if calculate_more == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()

calculator()