import random

# Import the hangmanASCII module (I created this module in the same folder).

import hangmanASCII

# Import the hangmanWordlist module (I created this module in the same folder).

import hangmanWordlist

print(hangmanASCII.logo)
print("\n")

# Use the random.choice() function to choose a word at random from hangmanWordlist.word_list and store it in a variable
# called display.

chosen_word = random.choice(hangmanWordlist.word_list)

# Create an empty list and store it in a variable called display.

display = []

# Next, append a "_" to the list stored in "display" for each character in chosen_word (we could say "for x in" or "for
# y in" - it makes no difference). Then print the list so that the player can see how many letters are in the word.

for letter in chosen_word:
    display.append("_")
print(display)
print("\n")

# Now, we store a boolean value of "False" in a variable called "end_of_game". For so long as end_of_game = False, the
# game should iterate. If end_of_game = True, the game should stop.

end_of_game = False

# Players of hangman have a finite number of attempts to guess the word: 6 attempts to be precise. We can represent
# these attempts as "lives". We therefore store a value of 6 inside a variable called "lives".

lives = 6

# Now we need to represent our loop as a set of imperative and conditional statements.

while not end_of_game:

    guess = (input("Guess a letter.\n")).lower()

    for i, letter in enumerate(chosen_word):    # Convert the string stored in chosen_word to an enumerated object
        if letter == guess:
            display[i] = letter
    print(display)
    print("\n")

    if guess not in chosen_word:
        lives -= 1  # Lose 1 life
        print(hangmanASCII.stages[lives])
        print(f'You guessed "{guess}": that\'s not in the word. You lose a life!')
        print("\n")
        print(display)
        print("\n")
        if lives == 0:
            end_of_game = True  # This will break the loop.
            print(f'You lose! The word was "{chosen_word}".')

    if "_" not in display:
        end_of_game = True      # This will break the loop.
        print("You win!")


