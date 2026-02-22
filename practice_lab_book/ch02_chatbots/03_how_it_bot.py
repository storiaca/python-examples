# How’s it going bot
# Author: Aleksandar Ristic
# Date: 22.02.2026
# Description: This bot will aks you how it's
# oing and make a comment depending on
# how you answer

# Ask the user how it’s going
print("How it's going?")
# Get the user’s reply
reply = input()
# If they said Good, reply Good!
if reply == 'Good' or reply == "good" or reply == "great":
  print("Good!")
# Otherwise if they said Bad, reply Oh no!
elif reply == 'Bad' or reply == 'bad' or reply == "poor":
  print("Oh no!")
# Otherwise if they’re "So so", reply "Hope you feel better!"
elif reply == "So so":
  print("Hope you feel better!")
# Otherwise reply "I see..."
else:
  print("I see..")