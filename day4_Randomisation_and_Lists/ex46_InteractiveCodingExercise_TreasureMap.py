# Let's create a game called "Treasure Map". The game will allow a user to put an "X in the box of their choosing.

# First, we are going to create three lists and store them in three variables, row1, row2, and row3.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Next, we are going to create a nested list of those lists and store it inside a variable we'll call "grid".

grid = [row1, row2, row3]

# The following instruction tells the Python interpreter to pass an f-string through the print() function.
# Python concatenates the three lists (row1, row2, and row3) but prints each on a new line.
# This prints what in effect looks like a 2-D array.

print(f"{row1}\n{row2}\n{row3}")

# It's critical to note that Python will still interpret grid as a nested list of three lists, however.

# Now we ask the user for an input based on grid reference i.e.,

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2.2)

grid_ref = input("Where do you want to put the treasure? ")

# Python will interpret the input as a two digit string by default, so we need to tell Python to convert the two digits
# of the string into integers and to store each in new variables e.g., "row" and "column".

row = int(grid_ref[0])
column = int(grid_ref[1])

# Now, we want Python to replace a ⬜️with an "X" at the relevant grid reference. WHAT YOU NEED TO REMEMBER IS THAT
# PYTHON DOES NOT INTERPRET THIS DATA STRUCTURE AS A 2-D ARRAY: IT INTERPRETS IT AS A NESTED LIST OF THREE LISTS!!!
# Therefore, we need to command Python to replace a ⬜️with an X in an index (i.e., [0], [1], or [2] of one of those
# lists i.e., row1, row2, or row3, which are themselves positioned at indices [0], [1] and [2] of the nested array.
# We need to turn our input into an index reference e.g., grid[0][1], and change the value of that index reference to
# "X". # Before we do so, remember that "23", for example, will in fact refer to grid[1][2]. If we pass "3" into our
# grid, we will get an IndexError, because the list index will be out of range. What we need to do, therefore,
# is subtract 1 from each of the input digits.

grid[row -1][column -1] = "X"

# Now, if we print our grid again, we should see an "X" at the reference we provided.

print(f"{row1}\n{row2}\n{row3}")

# This was a tricky exercise. Let's summarise what we did for future reference. First, we constructed three lists with
# three indices each, and we stored those lists in the variables "row1", "row2" and "row3". We stored the value ⬜️in
# each of the indices of the three lists.
# Next, we created a nested list of the first three lists and stored it in a variable "grid". We then commanded Python
# to print the nested list, but with each list on a new line, so that the user would see a grid-like structure.
# We then prompted the user for a two-digit grid-reference.
# We then converted that two digit string into integers and stored each integer in the variables "row" and "column".
# We then passed those variables as an index reference to an index stored in the nested list i.e., in grid, and we
# commanded python to replace the value in that index with "X".
# We then printed the 'grid' again.