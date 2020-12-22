# !/usr/bin/env python3

"""
This script is intended to show my project and what I learned in class.
Author | Albert Chu
"""

# Program to read a random MadLib from a file and print the Mad Lib with the user's response
import random

# Open the Mad Libs text file
f = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\Storiezz.txt")

# Read the whole file and store each line in a list
def random_line():
    line_num = 0
    selected_line = " "
    with f:
        while 1:
            madlibText = f.readline()
            if not madlibText: break
            line_num += 1
            if random.choice(0, line_num) < 1:
                selected_line = madlibText
    return selected_line.strip()

# Choose a random line from the list
madlib = random.choice(madlibText)

# Ask the user to input a verb
verb = input("Enter a VERB: ")

# Replace the blank with the user's input
madlib = madlib.replace("blank", verb)

# Print out the Mad Lib including the user's response
print(madlib)


