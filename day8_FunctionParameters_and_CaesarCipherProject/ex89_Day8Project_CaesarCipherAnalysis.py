alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Our objective is to connect two objects to one another by means of a method. Think of our task as being similar to
# that of building a stairway or ladder from one place to another: to traverse the distance between our origin and our
# destination, we must pass through a series of steps. In the context of the Python language, we call a series of steps
# a "program". Programs can contain many 'sub-programs' or 'subroutines', which are referred to as "functions".

# To summarise: Our (original) object in this case is any string input by a user, and our objective is a string related
# to its object by a program of our own design. The characters of both the object and the objective can be members of
# the Latin alphabet, numbers between 0 and 9, as well as symbols. Each member of the objective that is a member of the
# alphabet should be offset from the corresponding member of its object by n indices, while each member of both the
# objective and its object that is a number or symbol should be identical to one another.

# Let us call the object by a variable "start_text", and the objective by a variable "end_text".

# Recall that our intention is to invoke the values called by "start_text" and to transform them to the values called by
# "end_text". We begin by defining a function "caesar". Our intention is for the parameters "start_text", "shift-amount"
# and "cipher_direction" to pass through - and be transformed by - the function called by "caesar".

def caesar(start_text, shift_amount, cipher_direction):

# Let us now define a variable called by "end_text" and equate it to an empty string (i.e., an object with no values
# stored within it).

    end_text = ""

    # We wish to be able to both ENCODE an object and to DECODE an objective: that is, we want our function to be
    # reversible. Encoding implies offsetting in the forward direction i.e., from left-to-right, whereas decoding
    # implies offsetting in the reverse direction i.e., from right-to-left. We therefore set a condition: if the user
    # wishes to decode an objective, we reverse the offset direction.

    if cipher_direction == "decode":
        shift_amount *= -1


        # In the next step, we instruct Python to call the index value of a character belonging to the list called by
        # "alphabet" by a new variable, "position", if and only if that same character can also be called by the
        # variable "start_text". In pseudo-code, we can state 'for character in "start_text": if character in
        # "alphabet", store its value in memory and call it by the variable "position".' We can instruct Python to
        # compute the index value of a member of a list by the built-in function .index().

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)

            # In the next step, we instruct Python to transform the character to the character n indices to its right or
            # left (the direction being dependent upon the value called by "cipher_direction").

            new_position = position + shift_amount

            # In the next step, we instruct Python to append each character called by "position" to the string called by
            # "end_text".

            end_text += alphabet[new_position]

        # In the next step, by an 'else-statement' we instruct Python to append the object character to the string
        # called by "end_text" if it canNOT also be called by "alphabet". An else-statement is essentially an
        # anti-if-statement.

        else:
            end_text += char

    # The final step of the function called by caesar() instructs Python to print an f-string, by which the values
    # called by "ciper_direction" and "end_text" are also called.

    print(f"Here's the {cipher_direction}d result: {end_text}")

# The steps below instruct Python to import the string called by "logo" from the module called by "art", and to print
# it to the user interface.

from art import logo
print(logo)

# The next block of code includes a conditional statement and a while-function (also known as a 'while-loop'. By a
# while-loop, we can instruct Python to iterate a series of steps WHILE some condition (as defined in a 'conditional
# statement' persists. In the block below, Python is instructed to iterate a series of steps while the value called by
# the variable "should_end" is False. If the value called by "should_end" changes to True, then Python is instructed to
# stop iterating the steps.

should_end = False
while not should_end:

    # The first step of this while-function instructs Python to instruct the user to input one of two strings: 'encode'
    # or 'decode'. It also instructs Python to store the string input by the user in memory and to call it by (a
    # variable) "direction".

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # The next step instructs Python to instruct the user to input any string. It also instructs Python to store the
    # string input by the user in memory and to call it by "text".

    text = input("Type your message:\n").lower()

    # The next step instructs Python to instruct the user to input the value of the offset they desire. It also
    # instructs Python to store the value input by the user in memory and to call it by "shift".

    shift = int(input("Type the shift number:\n"))

    # Now, consider a condition wherein the user inputs a value of 367 for "shift" i.e., shift = 367: Python will return
    # the message "IndexError: list out of range". Ideally, we want Python to cycle back through the list (think of the
    # list as a circle divided by degrees called by its members i.e., the characters that belong to it.). How might we
    # instruct Python to do this in its own language? One way we can do this is by instructing Python to compute the
    # remaining value of shift after it has been divided by 26. For example, if the user inputs a value of shift = 367,
    # Python will ask the kernel to compute modulo of 367 / 26, then the kernel will return a value of 3 (in machine
    # language i.e, binary) and Python will translate this into a decimal value of 3.
    # if the input value is less than 26, there will be no remainder and the value called by shift will be the same as
    # that input by the user.

    shift = shift % 26

    # The next step calls the function i.e., "caesar", and passes the arguments (delimited by the parentheses) through
    # it. Note that the variables on the left-hand-side of the equality symbol are referred to as the PARAMETERS of the
    # function, and those on the right-hand-side are referred to as "arguments".

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # The next step instructs Python to instruct the user to input one of two strings, "yes" or "no".
    # It also instructs Python to store the string input by the user in memory and to call it by a variable, "restart".
    # The next step is represented by a block of code referred to as an if-statement. It instructs Python to change the
    # the value called by "should_end" to True and to print the string "Goodbye" IF the user inputs the string "no".

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")



