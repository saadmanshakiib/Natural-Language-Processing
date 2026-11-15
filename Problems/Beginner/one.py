from collections import Counter

from Text_Preprocessing.StopWords import text
from Text_Preprocessing.Tokenization2 import sents

text = input("Enter a sentence : ")

words = len(text.split())
print("Total Words : ",words)

sents = 0
for i in text:
    if i in "?.!":
        sents += 1

print("Total Sentence : ",sents)

print("Characters : ", len(text))