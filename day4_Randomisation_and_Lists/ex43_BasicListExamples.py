states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Missisippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# The variable above contains a list of US states in the order they joined the union. If I wanted to know the name of the 15th state to join the union, I would instruct Python to print the result of the following statement:

print(states_of_america[14])

# You might think I made a typo, but this isn't the case. The first item in a list has an offset of 0:

print(states_of_america[0])

# The second item has an offset of 1, the third of 2, and so on. The fifteenth item therefore has an offset of 14. 

# We can also work backwards. If I want to know the name of the last state to join the union, I can input the following:

print(states_of_america[-1])

# Now let's say I want to correct the spelling of an item in a list. 

print(states_of_america[19])
states_of_america[19] = "Mississippi"
print(states_of_america[19])

# Now let's say that, rather than asking the name of e.g., the 21st state to join the union, I instead want to know what number Texas was when it joined. To do this, I use the index() function.

print(states_of_america.index("Florida"))

# Python tells me that Florida was the 27th (26 + 1) state to join the union.

# Let's look at another list. 

shoppingList = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# We can use the append() function to append a single item to a list.

shoppingList.append("Carrots")
print(shoppingList)

# or the extend([]) function to append several items to a list...

shoppingList.extend(["Lettuce", "Tomatoes", "Cucumber"])
print(shoppingList)

# We can use the remove() function to remove an item from the list.__doc__

shoppingList.remove("Cherries")
print(shoppingList)

# Now, let's say I want to sort my list in alphabetical order...

shoppingList.sort()
print(shoppingList)

# or in reverse alphabetical order...

shoppingList.reverse()
print(shoppingList)