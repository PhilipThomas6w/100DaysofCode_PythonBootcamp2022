import random

randomInteger = random.randint(1, 1000)
print(randomInteger)

# Now let's generate a random floating point number and round it off to three decimal places. By default, the random()
# function in the random module will generate a random number between 0 and 1 (but never 0 and never 1).

randomFloat = round(random.random(), 3)
print(randomFloat)

# Now, what if we want to return a random floating point number between 0 and 5 (but never 0 and never 5)? We can't
# pass an argument in the random() function like we did in the randint() function, so we have to come up with a
# creative way of achieving this. We can do so by multiplying the result of random.random() by 5.

randomFloat = round(random.random() * 5, 3)
print(randomFloat)

# We can use the randint() function to simulate a coin toss. A coin toss will result in either heads or tails. We can
# let heads = 1 and tails = 0.

coinToss = random.randint(0, 1)
print(coinToss)

# We can also the randrange() function to simulate a dice throw. randrange() returns a randomly selected integer from
# range(start, stop, step).

diceThrow = random.randrange(1, 6, 1)
print(diceThrow)

# The randrange() function will return a ValueError if istart > istop.

# diceThrow = random.randrange(6, 1, 1)
# print(diceThrow)