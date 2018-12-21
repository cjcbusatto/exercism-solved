def is_pangram(sentence):
    if len(set(sentence.lower()) & set("abcdefghijklmnopqrstuvwxyz")) == 26:
        return True
    return False
