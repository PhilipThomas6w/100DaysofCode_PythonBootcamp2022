

# There are 52 cards in a standard deck.
# There are 4 suits (Clubs, Hearts, Diamonds, and Spades) and there are 13 cards in each suit (1, 2 ,3, 4, 5, 6, 7, 8,
# 9, 10, Jack, Queen, King, Ace)
# The Jack, King and Queen each call a value of 10. An Ace calls a value of 11.
# Since there are four suits, there are four cards in each suit that call a value of 10.
# While there is equal probability of calling any card in the deck i.e., 1/52, the probability of calling a particular
# value is significantly less. The probability of calling a value of 1-9 is 4/52 i.e., 1/13, and the probability of
# calling a value of 10 is 16/52 i.e., 4/13.
# To simplify our task, we won't work with probabilities. We'll simply assume that each value has a probability
# of 1/13 of being called. We'll include 4 <10>s in our 'deck', so that the probability of calling a 10 is increased to
# 4/13.

# Let us create a list of 13 'cards':

Deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Now, we want to draw a card at random...