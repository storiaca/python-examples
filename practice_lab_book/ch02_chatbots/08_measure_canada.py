# How to Measure Things in Canada
# Authors: Aleksandar Ristic
# Date: 09.03.2026.

print("I can tell you how to do measurments in Canada!")
measure = input("What are you measuring (mass/volume)? ").lower().strip(".!")

# Left branch - mass
# If weight, lbs, Othervise kg 
if measure == "mass":
  is_weight = input("Is it your weight?").lower()
  if is_weight == "yes":
    print("Use lbs.")
  else:
    print("Use kg.")

# Right branch - volume
# If cooking , cups & spoons. Otherwise metric.
elif measure == "volume":
  is_cooking = input("Is it for cooking?").lower()
  if is_cooking == "yes":
    print("Cups & Sponns")
  else:
    print("Metric")
  pass