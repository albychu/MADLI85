#!/usr/bin/env python3

"""
This script is intended to show my project and what I learned in class.

Author | Albert Chu

"""
import re


# Welcoming Code
print("Intoduction:\n"
    "Welcome to the world of MADLI85.\n"
    "Fill in the blanks!\n")
print(input("PRESS ENTER TO BEGIN."))


# this is the file that has the story
file = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\Storiezz.txt")
sentence = file.read()
file.close()
regex = re.compile(r"ADJECTIVE1|ADJECTIVE2|ADJECTIVE3|NOUN|VERB1|VERB2|ADVERB|CELEBRITY|EMOTION|HOLIDAY")
#look for these regular expressions

#search the text for regex and prompt user
while True:
    match = regex.search(sentence)
    if match == None:
        break
    elif match.group() == "ADJECTIVE1":
        print ("Enter Adjective: ")
    elif match.group() == "ADJECTIVE2":
        print ("Enter Adjective: ")
    elif match.group() == "ADJECTIVE3":
        print ("Enter Adjective: ")
    elif match.group() == "NOUN":
        print ("Enter Noun: ")
    elif match.group() == "VERB1":
        print ("Enter Verb: ")
    elif match.group() == "VERB2":
        print("Enter Verb: ")
    elif match.group() == "ADVERB":
        print ("Enter Adverb: ")
    elif match.group() == "EMOTION":
        print ("Enter Emotion: ")
    elif match.group() == "CELEBRITY":
        print ("Enter Celebrity: ")



#replace regex with user's words
    word = input()
    sentence = sentence.replace(match.group(), word, 1)

#story with replaced words in new file
newFile = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\NewStoriez.txt", "w")
newFile.write(sentence)
newFile.close()


print(input("PRESS ENTER TO END."))