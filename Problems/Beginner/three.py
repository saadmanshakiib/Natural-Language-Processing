def remove_punctuation(text):

    result = ""

    for char in text:
        if char.isalnum() or char.isspace():
            result += char

    return result


text = "Hello! How are you? I'm learning NLP."

clean_text = remove_punctuation(text)

print(clean_text)