# Movie Rater with Dictionaries
# Author: Aleksandar Ristic
# Date: 26/11/2026
# Asks 5 people for their movie ratings
# and tracks them using dictionaries

# Initialize a dictionary of movies
movies = { "frozen": 0, "x-men": 0, "harry potter": 0}

# Ask 5 people for their movie preference
for i in range(5):
  preference = input("Which movie is your favorite out of Frozen, X-Men or Harry Potter? ").lower().strip(" .!")

  # Add 1 to the appropriate movie
  if preference in movies:
    movies[preference] += 1
  else: 
    # print("Please type Frozen, X-Men, or Harry Potter")
    # if the key is not there, add a new pair
    movies[preference] = 1

# Print out the results using a loop
for movie in movies:
  print(f"{movie.capitalize()}: {movies[movie]}") # Name and tally