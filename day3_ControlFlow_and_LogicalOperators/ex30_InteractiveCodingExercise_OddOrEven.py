# This program will tell you if any integer is an odd or an even number.

# First, we ask the user for an input. Even though we input numbers, Python will recognise the input as a string,
# so we have to convert it to an integer by passing it through the int() function.

number = int(input("Which number do you want to check? "))

# Now we have an integer, we need to check if it is even. To do so, we divide it by 2 and return the remainder. Python
# includes the % (modulo) operator for this purpose. If the remainder of our integer/2 is greater than or equal to 1,
# then we know it must be an odd number.

if number % 2 >= 1:
    print("This is an odd number")
else:
    print("This is an even number")