# Chip Rater
# Author:
# Date:
# To rate chips from 1−5 on various factors
# such as crispiness, taste, etc.
# and get an overall average score out of 5.
# Greet the participant
print("Welcome to our Chip Rater experiment.")
print("Please answer three questions on a scale of 1−5.")
# Make a list of questions about chip goodness
questions = ["How crispy are the chips? ",
"How would you rate the taste? ",
"How would you rate the packaging? "]
# Initialize overall score
score = 0
# For each question, get their response out of 5
# and convert it to an int
for question in questions:
  rating = input(question)
  score = score + int(rating)
# Calculate final overall score
# by taking the sum of all ratings
# and dividing by number of questions.
print("Overall score: " + str(score/len(questions)))