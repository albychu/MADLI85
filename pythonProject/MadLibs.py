#!/usr/bin/env python3

"""
This script is intended to show my project and what I learned in class.

Author | Albert Chu

"""
import re


# Welcoming Code
print("Intoduction:\n"
    "Welcome to the world of MADLI85.\n"
    "Fill in the blanks to many different proverbs!\n"
    "Use your silly, funny, and outrageous imagination!\n")
print(input("PRESS ENTER TO BEGIN."))



file = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\Storiez.txt")
sentence = file.read()
file.close()
regex = re.compile(r"ADJECTIVE|NOUN|VERB|ADVERB")

while True:
    match = regex.search(sentence)
    if match == None:
        break
    elif match.group() == "ADJECTIVE":
        print ("Enter Adjective: ")
    elif match.group() == "NOUN":
        print ("Enter Noun: ")
    elif match.group() == "VERB":
        print ("Enter Verb: ")
    elif match.group() == "ADVERB":
        print ("Enter Adverb: ")



    word = input()
    sentence = sentence.replace(match.group(), word, 1)

newFile = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\NewStoriez.txt", "w")
newFile.write(sentence)
newFile.close()




