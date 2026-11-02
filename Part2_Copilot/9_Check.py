# 9 — Put conditions in the right order
# Read: https://www.w3schools.com/python/python_if_elif.asp
# Relevant: Python uses the first matching branch of an if/elif/else chain.
# Use these exact ranges to interpret the original task below:
# - age < 0: "That must be a mistake"
# - age from 0 through 4: "I suspect you can't write quite yet..."
# - age >= 5: "Ok, you're <age> years old" (replace <age> with the input)
# Do not add an upper-age limit for this exercise.
# Boundary checks: -1, 0, 4 and 5.
#
# Please write a program which asks for the user's age.
# If the age is not plausible, that is, it is under 5 or something that can't be an actual human age,
# the program should print out a comment.

# Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.

# Sample output
# What is your age? 13
# Ok, you're 13 years old

# Sample output
# What is your age? 2
# I suspect you can't write quite yet...

# Sample output
# What is your age? -4
# That must be a mistake

# Write your code here:

