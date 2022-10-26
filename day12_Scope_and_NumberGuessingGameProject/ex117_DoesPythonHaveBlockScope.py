# Unlike functions, conditional statements don't have opaque 'walls' or 'fences' that prevent Python from calling
# objects contained within them. We might think of their 'walls' as being transparent, so that Python can see right
# through them. In reality, conditional statements have no walls. Their contents are not local: they are exposed to the
# global environment and hence Python can always see them, even if they appear to be 'nested' within other conditional
# statements.

# For example, if we instruct Python to pass the values called by <a_variable> and <new_enemy>, below, each of which
# appear to be nested within a conditional statement, then Python will recognise the variables and call them.

if 3 > 2:
    a_variable = 10
print(a_variable)

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# However, if we move a conditional statement inside a function, Python can no longer see it i.e., it moves beyond
# Python's scope.

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

# We can instruct Python to 'call the function', and this will in turn enable it to call the instructions contained
# within the function (i.e., the instructions called by the function), but it can't call the contents of the function
# directly.

enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Now consider the code below. We want to instruct Python to increase the value of <enemies> by 1.

# enemies = 1
#
# def increase_enemies():
#     enemies += 1                                    # Note that <enemies> inside the function is highlighted, indicating
#                                                     # an error. The error text states "Unresolved reference 'enemies'.
#                                                     # In other words, the function doesn't know what 'enemies' is
#                                                     # supposed to call.
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# We can resolve this using the <global> function...

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# However, using the <global> function is not recommended, because it generally leads to confusion and bugs. It's better
# to use the return function to achieve the same outcome.

enemies = 1

def increase_enemies():
    # print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")