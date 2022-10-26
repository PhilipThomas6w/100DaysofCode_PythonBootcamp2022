# Banker Roulette - Who will pay the bill?

# Split string method

# First we ask for a string as an input i.e., the names of all party members.

names_string = input("Give me everybody's names, separated by a comma.\n")

# Bob, Mark, Paul, Peter, David, Susan, Louise, Shirley (I've typed these names here so that I can copy-paste each time I test the code)

# Next, we use the split() function. The split() function is a built-in Python function that splits a string into a list. 

names = names_string.split(", ")

# Now I'll print the list...

print(names)

# There are two methods by which we can solve this problem. The first (and less efficient) way is as follows...

# First, we pass the list we stored in the variable "names" through the len() function and store the return value inside another variable, num_items. Recall that the len() function is one of Python’s built-in functions. It returns the length of an object. For example, it can return the number of items in a list.

num_items = len(names)
print(num_items)

# The standard out tells us that there are 8 items in the list. The number 8 is therefore stored in the num_items variable.

# Now we need to import the random module so that we can call functions from it...

import random

# Done! Now we can use the randint() function to select one of the items contained in the list at random. Remember, the first item is at 0, the second at 1, and so on; so we start from 0. We know that the last item will be stored at the num_of_items -1 i.e., in a list of four items, the first would be at 0 and the fourth would be at 3.   

random_choice = random.randint(0, num_items - 1)
print(random_choice)

# Now, rather than returning a number, we really want to return a name, 

person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay the bill today. Ouch!")

# A much easier way to do this is to simply pass the list stored in "names" through the choice() function, which we can also call from the random module.

for i in range(1): 
  print(random.choice(names), "is going to pay the bill today. Tough luck!")

# the argument in the range() function sets the number of random values that will be returned. 'i' can be anything. We could have said "for t in range(3)" and we would have got three names back.