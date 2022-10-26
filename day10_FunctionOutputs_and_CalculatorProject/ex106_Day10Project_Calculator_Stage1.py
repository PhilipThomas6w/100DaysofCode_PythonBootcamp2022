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
  "/": division
}

# Instruct Python to request two user inputs: <num1> and <num2>. Instruct Python to convert the string inputs to
# integers.

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

# Instruct Python to print the keys called by <operations_dictionary> (so that the user can see their options).

for operator in operations_dictionary:
    print(operator)

# Instruct Python to request a user input (from one of the options printed above) and call it by <operation>. The user
# input will correspond to a key in <operations_dictionary>.

operation = input("Choose an operation from the options given above: ")

# Instruct Python to pass the value called by <operation> e.g., "+" through <operations_dictionary> (this will call
# the value paired with that key), and call the value called by <operations_dictionary[operation]> by
# <calculation_function>. So, for example, if the user inputs "+", "+" will be passed through <operations_dictionary>
# and will call the function <addition>. The function called by <addition> will now be called by <calculation_function>.

calculation_function = operations_dictionary[operation]

# Instruct Python to pass the values called by <num1> and <num2> through <calculation_function> and call the result by
# <answer>. So, for example, if the user inputs "10", "5", and "+", Python will pass 10 and 5 through the function
# called by <addition> (i.e., <n1 + n2>).

first_answer = calculation_function(num1, num2)

# Instruct Python to pass an f-string through the <print> function.

print(f"{num1} {operation} {num2} = {first_answer}")

operation = input("Pick another operation: ")
num3 = int(input("What's the third number?: "))
calculation_function = operations_dictionary[operation]
second_answer = calculation_function(first_answer, num3)

print(f"{answer} {operation} {num3} = {second_answer}")