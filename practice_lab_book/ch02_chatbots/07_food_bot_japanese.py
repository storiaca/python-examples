# Food Bot (Japanese food expert)
# Author: Aleksandar Ristic
# Date: 08.03.2026.

# Asks your favourite dish?
print("What's your favorite dish?")

# Gets your reply, e.g., tempura
favorite = input().lower().strip(".?!")

# Create a list of Japanese foods, including
# tempura, sushi, sashimi
japanese_foods = ["tempura", "sushi", "sashimi"]

# If your favourite food is in the Japanese
# food list, then give a recommendation
if favorite in japanese_foods:
  print("Oh! You should try Sushi Garden in Metrotown.")
else:
  print("Sorry, not sure. You could always try Cactus Club!")