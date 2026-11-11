# Most Popular Cafe Finder
# Author: Aleksandar Ristic
# Date:
# A survey to deduce the most popular cafe
# Starbucks − an international cafe
# Tim Hortons − a Canadian cafe
# Artiggiano − a local cafe
# The cafe which gets the most votes is the most popular
# Initialize tallies to 0

starbucks_tally = 0
tim_hortson_tally = 0
artiggiano_tally = 0

for i in range(5):
  # Ask the user what their favourite cafe is
  favourite_cafe = input("What's your favourite of Starbucks, Tim Hortons, Artiggiano? ").lower()

  # add to the matching tally
  if favourite_cafe == "starbucks":
    starbucks_tally = starbucks_tally + 1
  
  elif favourite_cafe == "tim hortons":
    tim_hortson_tally = tim_hortson_tally + 1

  elif favourite_cafe == "artiggiano":
    artiggiano_tally = artiggiano_tally + 1

# print out how many people who like each one
print("Starbucks:", starbucks_tally)
print("Tim Hortons:", tim_hortson_tally)
print("Artiggiano:", artiggiano_tally)
  