#generate random 1000 sentences from original 40 lines

import random 
from random import randint

lines = open("random.txt").readlines()

#empty the file first
open("random_sentences.txt", 'w').close()

#generate 1000 queries
for i in range(0,1000):
    sentence=""
    #sentence length from 2 to 10
    for i in range(randint(2,10)):
        #picking random line number in 40 orignial query lines
        line_number = randint(0,39)
        line=lines[line_number]
        words = line.split()
        new_word=random.choice(words)
        new_word=new_word.replace('\"', '')
        sentence = sentence + " " + new_word
    #append new generated sentence into the file
    with open("random_sentences.txt","a") as f:
        f.write("\"" + sentence + "\"\n")
