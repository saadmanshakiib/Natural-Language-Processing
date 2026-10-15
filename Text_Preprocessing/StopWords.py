import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

text = "The food is very good and the service is excellent"

words = text.lower().split()

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word not in stop_words
]

print(filtered_words)