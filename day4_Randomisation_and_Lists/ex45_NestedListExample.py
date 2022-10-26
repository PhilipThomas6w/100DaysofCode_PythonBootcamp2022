# Below, we are going to create a nested list i.e., a list that contains lists. Nested lists are commonly used by Python programmers, and it's useful to get comfortable with creating them.

# dirtyDozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]

vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

# Notice that if we concatenate the two lists, we simply get a consolidated list.

dirtyDozen = fruits + vegetables
print(dirtyDozen)

# but if we create a new list and include each list as a parameter, then we get a nest list i.e., a list that contains two lists.

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(len(dirty_dozen))

print(dirty_dozen[0][2])

