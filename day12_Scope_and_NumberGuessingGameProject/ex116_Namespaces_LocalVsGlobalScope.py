################### Scope ####################

# You can't call a local variable from outside of the function it is called by. You must call the function, and then the
# variable will then be called by the function it is nested within.

enemies = 1                                     # has global scope.

def increase_enemies():
  enemies = 2                                   # has local scope within the function <increase_enemies()>.
  print(f"enemies inside function: {enemies}")  # calls the local variable <enemies> (by which is called a value of 2).

increase_enemies()
print(f"enemies outside function: {enemies}")   # calls the global variable <enemies> (by which is called a value of 1)
                                                # rather than the local variable <enemies> (by which is called a value
                                                # of 2).

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# print(potion_strength)                        # Note that intellisense won't offer the option of tabbing in
                                                # <potion_strength> as you begin to type it. This gives you a hint that
                                                # <potion_strength> is beyond the scope of Python. If we instruct
                                                # Python to print <potion_strength>, then Python will inform us that
                                                # <potion_strength> is undefined i.e., Python can't recognise it and
                                                # hence can't call it.

                                                # We have to instruct Python to call <drink_potion()>: <drink_potion()>
                                                # contains the instructions to memorise the value 2 and to call it by
                                                # <potion_strength>, and the instruction to pass the value called by
                                                # <potion_strength> through the <print()> function.

                                                # We can think of the function as a tabernacle with opaque walls. To
                                                # call an object contained within the tabernacle, we have to instruct
                                                # Python to go into the tabernacle: Python can only call objects
                                                # contained within the tabernacle while it is inside the tabernacle,
                                                # otherwise it doesn't know they are there. If we don't instruct Python
                                                # to enter the tabernacle, it remains outside i.e., in the global
                                                # environment.

                                                # If we want an object contained within the tabernacle to be available
                                                # outside of the tabernacle, then we have either have to move it to the
                                                # outside of the tabernacle.