# Coffee Bot
# Author: Aleksandar Ristic
# Date: 26.02.2025.

'''
Write a CoffeeBot that asks if you would like cream. It should accept Yes/yes or No/no as inputs, and reply appropriately depending on the answer. If the user inputs anything else, it should repeat back their answer and say that it does not understand.
'''
print("I'm CoffeeBot. Would you like craem with yoyr coffee? (Yes/No)")

answer = input()

if (answer == "Yes" or answer == "yes"):
  print("Here's your coffee with cream.")
elif(answer == "No" or answer == "no"):
  print("Here's your coffee, no cream.")
else:
  print("Sorry, I don't know what" + answer + " means.")
