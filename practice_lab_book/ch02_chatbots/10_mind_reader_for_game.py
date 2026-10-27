# Mind Reader Game (3 rounds)
# Author: Aleksandar Ristic
# Date: 25.10.2026.
# This is a 2−player game.
# The 1st player reads a word and secretly
# enters 3 words they associate with it.
# The 2nd player must then try to guess at
# least one of the words.
# If it’s a match, they win!

# Introduce the game
print("Welcome to Mind Reader")

# Make a list of words
word_list = ["cat", "dog", "apple"]

# Loop through all the items in words
for word in word_list:
	# Ask the firts player to enter 3 words
  # accoiated with a given word
  print("Player 1, enter 3 words you think \ of when I say " + word)

# Get the 3 words from the user
first_word = input("First word: ").lower()
second_word = input("Second word: ").lower()
third_word = input("Third word: ").lower()

# Clear the screen
print(100*"\n")

# Ask the 2nd player to guess
print("Player2, what is one word yu think \ Player 1 associates with " + word + "?")
guess = input().lower()

# Check if they match and tell them if they win
if guess in [first_word, second_word, third_word]:
  print("You got it!")

# Otherwise, if they got it wrong
else:
  print("No match! They said " + first_word + \
        ", "+ second_word + " and " + third_word)