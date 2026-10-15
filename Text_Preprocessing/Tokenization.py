import string
from collections import Counter
import re
from traceback import print_stack

string1 = "Hello !! Sadman, Now Welcome To The Natural Language Processing World, Sadman is in 10th Semester Now. Natural Language Processing is Great"
print("Without Tokenization : ", string1)

string_split = string1.split()
print("Splitting String : ",string_split)

string_lower = string1.lower()
print("Lower Case String : ",string_lower.split())

clean_text = string1.translate(
    str.maketrans("", "", string.punctuation)
)

print("Removing Punctuation : ",clean_text)

counts = re.findall(r"\b\w+\b",string1.lower())
print("Total Words : ",Counter(counts))
