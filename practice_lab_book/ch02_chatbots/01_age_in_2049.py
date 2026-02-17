# Your age in 2049 bot
# Author: Aleksandar
# Date: 15.02.2025.
# Description: This bot will ask you
# what year it is in and how old you
# currently are, then it’ll tell you
# your age in 2049

# Ask user what year it is in
print("What year are we in?")

# Get the user's reply
currentYear = input()

# Ask user what age they currently are
print("How old are you currently?")

# Get the user’s reply
userAge = input()

# Calculate how old the user will be in 2049
yearsAhead = 2049 - int(currentYear)
userFutureAge = int(userAge) + yearsAhead

# Tell the user how old they will be in 2049
print("You will be", userFutureAge, "years old in 2049!")