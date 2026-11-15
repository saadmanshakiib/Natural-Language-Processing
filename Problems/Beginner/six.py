from collections import Counter

text = "python is easy and python is powerful"

words = text.split()

frequency = Counter(words)

max_count = max(frequency.values())

for word, count in frequency.items():
    if count == max_count:
        print(word, ":", count)