#!/usr/bin/python3
import random

# Assign a random signed integer to the variable number
number = random.randint(-100, 100)

# Check if the number is positive, negative, or zero and print the appropriate message
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
