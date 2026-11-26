# Most Popular Cafe Finder
# Author: Aleksandar Ristic
# Date:
# A survey to deduce the most popular cafe
# Starbucks − an international cafe
# Tim Hortons − a Canadian cafe
# Artiggiano − a local cafe
# The cafe which gets the most votes is the most popular
# Initialize tallies to 0
import string

starbucks_tally = 0
tim_hortson_tally = 0
artiggiano_tally = 0

for i in range(5):
  # Ask the user, then normalise: lowercase, trim spaces, drop punctuation
  favourite_cafe = input("What's your favourite of Starbucks, Tim Hortons, Artiggiano? ")
  favourite_cafe = favourite_cafe.lower().strip().strip(string.punctuation)

  # add to the matching tally
  if favourite_cafe == "starbucks":
    starbucks_tally += 1
  
  elif favourite_cafe == "tim hortons":
    tim_hortson_tally += 1

  elif favourite_cafe == "artiggiano":
    artiggiano_tally += 1

# Prints out the percentage of peple who like
# each one, up to 2 decimal places
print("Starbucks: {:.2f}%".format(starbucks_tally/5*100))
print("Tim Hortons: {:.2f}%".format(tim_hortson_tally/5*100))
print("Artiggiano: {:.2f}%".format(artiggiano_tally/5*100))
  