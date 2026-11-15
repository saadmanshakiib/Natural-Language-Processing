
import nltk

nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize , word_tokenize

sents = "I realy enjoy lernning Natural Langauge Processng becaus it helps computors understnd human langauge. I am curently studing machin lernning, artifical inteligence, and deep lernning. I belive that NLP is an amazng technolgy that can help us develp inteligent chatbots, automatd transltion systems, and smart text analysys tools. I want to imprve my programing skils and becum a succesful maching lernning enginer in the future."

print(word_tokenize(sents))




