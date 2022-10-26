# This program will print the sum of the two elements of a two-digit number.
# First, we ask the user for an input, and we store that input in a variable called "two_digit_number".

two_digit_string = input("Type a two digit number: ")

# Even though the input will look like a number, Python will recognise it as a string...

print(two_digit_string)
print(type(two_digit_string))

# We need to convert the str to an int. We can do so by passing the string through the int() function.

two_digit_number = int(two_digit_string)
print(two_digit_number)
print(type(two_digit_number))

# Numbers are not subscriptable, meaning we can't ask Python to operate on them in the same way as we would a string.
# To explain, we can print the 4th element of a string by passing it through the print() function.

print("This function will print the fourth element of this string" [3])

# Now, let us try the same for a number...

print(12345, [3])

# The above print() function didn't actually print the fourth element. It printed a list containing the number 3. The
# fourth element in the number "12345" is actually "4".

# To add the two digits together, we need to subscribe the string first, THEN convert the digits to numbers, and THEN
# add them.

print(int(two_digit_string[0]) + int(two_digit_string[1]))

