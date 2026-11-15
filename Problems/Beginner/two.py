def normalize_text(text):

    text = text.lower()
    text = text.strip()
    text = " ".join(text.split()) # join words in single space

    return text

text = "  HELLO   WORLD   Welcome To NLP  "

print(normalize_text(text))
