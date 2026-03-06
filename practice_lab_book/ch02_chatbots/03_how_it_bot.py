# How’s it going bot
# Author: Aleksandar Ristic
# Date: 22.02.2026
# Description: This bot will aks you how it's
# oing and make a comment depending on
# how you answer

# Ask the user how it’s going
print("How it's going?")
# Get the user’s reply
reply = input().lower()
# If they said Good, reply Good!
if "Good" in reply or "good" in reply or "great" in reply:
  if "not" in reply:
    print("Oh no!")
  else:
    print("Good!")
# Otherwise if they said Bad, reply Oh no!
elif "bad" in reply or "not good" in reply:
  print("Oh no!")
# Otherwise if they’re "So so", reply "Hope you feel better!"
elif reply == "So so":
  print("Hope you feel better!")
# Otherwise reply "I see..."
else:
  print("I see..")