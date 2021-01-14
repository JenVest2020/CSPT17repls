"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
import math

for i in dir(math):
  if i.startswith("is"):
    print(i)