from textblob import TextBlob

text = "I realy love learnig NLP. It is realy intresting and helpfull. I want to be a succesful maching learnig enginer."

textblb = TextBlob(text)

print(textblb.correct())

inputText = input("Enter Text : ")
textblb2 = TextBlob(inputText)
print("Corrected Line : ", textblb2.correct())


