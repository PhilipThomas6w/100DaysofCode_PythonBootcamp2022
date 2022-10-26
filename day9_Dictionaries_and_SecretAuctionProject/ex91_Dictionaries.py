# Dictionaries allow us to group together and tag related pieces of information. Every dictionary consists of two parts:
# 1) a key, and 2) a value. {Key : Value}

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])
print("\n")

# Adding new items to a dictionary...

programming_dictionary["Dictionary"] = "An unordered key:value pair"

print(programming_dictionary)

empty_dictionary = {} # creates an empty dictionary called by "empty_dictionary"

programming_dictionary = {} # effectively wipes the contents of programming dictionary - in reality it creates an empty dictionary called by programming_dictionary such that the original dictionary can no longer be called by that variable.

# Let's redefine programming_dictionary so we can continue with our examples...

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

print("\n")

for object in programming_dictionary:
  print(object)  # prints the keys but not the values...

print("\n")

for key in programming_dictionary:
  print(key) # prints the keys
  print(programming_dictionary[key])  # prints the values
