from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = [
    "playing",
    "played",
    "eating",
    "gaming",
    "nothing",
    "played",
    "running",
    "studying",
    "studies"
]
for word in words:
    print(word," : ",stemmer.stem(word))