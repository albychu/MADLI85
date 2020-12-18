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



file = open(r"C:\Users\12016\PycharmProjects\pythonProject\Stor-E\Storiezz.txt")
sentence = file.read()
file.close()
regex = re.compile(r"ADJECTIVE|NOUN|VERB|ADVERB|CELEBRITY|EMOTION")

while True:
    match = regex.search(sentence)
    if match == None:
        break
    elif match.group() == "ADJECTIVE":
        print ("Enter Adjective: ")
    elif match.group() == "NOUN"
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




#import webbrowser
#import time
#import random

#while True:
#    sites = random.choice(['youtube.com/watch?v=dQw4w9WgXcQ', 'youtube.com/watch?v=dQw4w9WgXcQ', 'youtube.com/watch?v=dQw4w9WgXcQ'])
#    visit = "http://{}".format(sites)
#    webbrowser.open(visit)
#    seconds = random.randrange(2, 1000)
#    time.sleep(seconds)

#read from file
#def ReadRandomLine():
 #   f=open("Fill Storiezz.txt", "r")
 #   lines=f.readlines()
 #   print(lines)
 #   f.close()
#ReadRandomLine()
