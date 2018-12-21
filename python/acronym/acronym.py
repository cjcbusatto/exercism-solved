def abbreviate(words):
    return ''.join([word[0].upper()
                    for word in words.replace("-", " ").split() if word[0].isalpha()])
