
my_dictionary = {
    "A": 1,
    "B": 4,
    "C": 3,
    "D": 2,
}

print(my_dictionary)

print(my_dictionary["C"])

highest_value = 0
winner = ""

for key in my_dictionary:
    my_variable = my_dictionary[key]


    if my_variable > highest_value:
        highest_value = my_variable

        winner = key
        print(winner)
