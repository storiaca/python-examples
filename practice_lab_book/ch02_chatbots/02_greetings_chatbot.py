# Greetings Chatbot
# Author: Aleksandar Ristic
# Date: 16.02.2025.

import random
import time

# Say hi, what’s your name?
print("Hi, what's your name?")
# Get the user’s name
user = input()
# Respond nice to meet you, <name>
print("Nice to meet you, " + user)
# Ask what your favourite book is
print("What is your favorite book?")
# Let the user respond
book = input()
time.sleep(1.5)
# Make a comment about it
print(f"Hey, {user}, that's a great book, {book}, to reade.")

# Make a not−too−repetitive response in 3 steps:
# Create a list of possible response
responses = ["Oh, nice!", "That's a good one.", "Hmm, strange taste.", "blah blah blah", "Whoa there." "Hahahhaa!"]
# Choose one randomly from the list
random_response = random.choice(responses)
# Say that random response
print(random_response)