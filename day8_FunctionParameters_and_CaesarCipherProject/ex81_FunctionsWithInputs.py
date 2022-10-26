# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print("Hi Philip.")
  print("How are you today, Philip?")
  print("Isn't the weather just fantastic today, Philip?.")

greet()

def greeting(name):
  print(f"Hi, {name}.")
  print(f"How are you today, {name}?")
  print(f"Isn't the weather just fantastic today, {name}?")

greeting("Luke")
greeting("Thomas")

# In the above function, greeting(name), "name" is referred to as the "parameter", and the value it is given when the
# function is called is known as the "argument". The argument is 'passed through' the function.

# Functions with more than one parameter.

def greet_with(title, name, location):
    print(f"Good day to you {title} {name}. It's a pleasure to meet your acquaintance.")
    print(f"Would you happen to be on your way to {location}?")

greet_with("Grand Sorcerer", "Lukios", "Skyrim")