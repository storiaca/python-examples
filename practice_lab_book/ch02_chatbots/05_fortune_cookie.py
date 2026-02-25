# Horoscope Bot
# Author: Aleksandar Ristic
# Date: 25.02.2026.
# Description: Write a fortune cookie generator that prints out a random fortune to the screen when the
# program is run. It must select from the following fortunes:

# You will have great success.
# You will become rich.
# You will find love.
import random

print("Welcome to Fortune Cookie Generator")

fortunes = ["You will have great success.", "You will become rich.", "You will find love."]

random_fortune = random.choice(fortunes)

print(random_fortune)