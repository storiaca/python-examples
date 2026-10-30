# Mind Reader Game (3 rounds with random words)
# Author: Aleksandar Ristic
# Date: 28.10.2026.
# This is a 2−player game.
# The 1st player reads a word and secretly
# enters 3 words they associate with it.
# The 2nd player must then try to guess at
# least one of the words.
# If it’s a match, they win!

import random
# Introduce the game
print("Welcome to Mind Reader")

# Makea list of words
word_list = ["cat", "dog", "apple", "hot", "coffee", "sport", "show"]

# do 3 rounds
for i in range(3):
    # Ask the first palyer to neter 3 words
    # associated with a randomly selected word
    word = random.choice(word_list)
    print("Player 1, enter 3 words you think of when I \24 say " + word)

    # Get the 3 words from the user
    first_word = input("First word: ").lower()
    second_word = input("Second word: ").lower()
    third_word = input("Third word: ").lower()

    # Clear the sceen
    print(100*"\n")

    # Ask the 2nd player to guess
    print("Player 2, what is one word you think Player 1 \ associates with " + word + "?")
    guess = input().lower()

    # Check if they match and tell them if they win!
    if guess in [first_word, second_word, third_word]:
      print("You got it!")
    
    # Otherwise, if they got it wrong
    else: 
       print("No match! They said " + first_word + \
             ", "+ second_word + " and " + third_word)