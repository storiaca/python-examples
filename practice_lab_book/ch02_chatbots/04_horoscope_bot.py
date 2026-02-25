# Horoscope Bot
# Author: Aleksandar Ristic
# Date: 23.02.2026.
# Description: The bot asks what year you are
# born and tells you your Chinese Zodiac sign.

# Greet the user
print("Hello! I’m the Horoscope Bot. \
Tell me, what year were you born?")

# Get users year of birth
birth_year = input()

# Rat - 1996, 1984, 1972, 1960, 1948
if(birth_year == "1996" or birth_year == "1984" \
   or birth_year == "1972" or birth_year == "1960" or birth_year == "1948"):
  print("You were born in the Year of the Rat!") 
# Ox - 1997, 1985, 1973, 1961, 1949
elif(birth_year == "1997" or birth_year == "1985" \
      or birth_year == "1973" or birth_year == "1961" or birth_year == "1949"):
  print("You were born in the Year of the Ox!") 
# Tiger - 1998, 1986, 1974, 1962, 1950
elif(birth_year == "1998" or birth_year == "1986" \
      or birth_year == "1974" or birth_year == "1962" or birth_year == "1950"):
  print("You were born in the Year of the Tiger!") 
# Rabbit - 1999, 1987, 1975, 1963, 1951
elif(birth_year == "1999" or birth_year == "1987" \
      or birth_year == "1975" or birth_year == "1963" or birth_year == "1951"):
  print("You were born in the Year of the Rabbit!") 
# Dragon - 2000, 1988, 1976, 1964, 1952
elif(birth_year == "2000" or birth_year == "1988" \
      or birth_year == "1976" or birth_year == "1964" or birth_year == "1952"):
  print("You were born in the Year of the Dragon!")
# Snake - 2001, 1989, 1977, 1965, 1953
elif(birth_year == "2001" or birth_year == "1989" \
      or birth_year == "1977" or birth_year == "1965" or birth_year == "1953"):
  print("You were born in the Year of the Snake!")
# Horse - 2002, 1990, 1978, 1966, 1954
elif(birth_year == "2002" or birth_year == "1990" \
      or birth_year == "1978" or birth_year == "1966" or birth_year == "1954"):
  print("You were born in the Year of the Horse!")
# Goat - 2003, 1991, 1979, 1967, 1955
elif(birth_year == "2003" or birth_year == "1991" \
      or birth_year == "1979" or birth_year == "1967" or birth_year == "1955"):
  print("You were born in the Year of the Goat!")
# Monkey - 2004, 1992, 1980, 1968, 1956
elif(birth_year == "2004" or birth_year == "1992" \
      or birth_year == "1980" or birth_year == "1968" or birth_year == "1956"):
  print("You were born in the Year of the Monkey!")
# Rooster - 2005, 1993, 1981, 1969, 1957
elif(birth_year == "2005" or birth_year == "1993" \
      or birth_year == "1981" or birth_year == "1969" or birth_year == "1957"):
  print("You were born in the Year of the Rooster!")
# Dog - 2006, 1994, 1982, 1970, 1958
elif(birth_year == "2006" or birth_year == "1994" \
      or birth_year == "1982" or birth_year == "1970" or birth_year == "1958"):
  print("You were born in the Year of the Dog")
# Pig - 2007, 1995, 1983, 1971, 1959
elif(birth_year == "2007" or birth_year == "1995" \
      or birth_year == "1983" or birth_year == "1971" or birth_year == "1959"):
  print("You were born in the Year of the Pig!")

# Error handling
else: 
  print ("Please enter a year between 1948 and 2007.")


# Horoscope Bot Optimized
# Description: Uses modulo arithmetic to determine the Chinese Zodiac sign.
'''
zodiacs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]

print("Hello! I’m the Horoscope Bot. Tell me, what year were you born?")

try:
    birth_year = int(input())
    # The remainder of year % 12 maps directly to the zodiac list index
    # 1944 % 12 is 0 (Monkey), 1945 % 12 is 1 (Rooster), etc.
    sign = zodiacs[birth_year % 12]
    print(f"You were born in the Year of the {sign}!")
except ValueError:
    print("Please enter a valid four-digit year (e.g., 1996).")
'''


