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
tim_hartson_tally = 0
artiggiano_taly = 0

for i in range(5):
  # Ask the user what their favourite cafe is
  favourite_cafe = input("What's your favourite of Starbucks, Tim Hortons, Artiggiano? ").lower()
  