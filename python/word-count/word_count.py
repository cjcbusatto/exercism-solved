from functools import reduce
import string

# A map-reduce approach for the word-counter problem using python

# There are many different ways to solve this problem,
# the more pythonic I found uses the dict subclass Counter
# https://docs.python.org/3.1/library/collections.html#collections.Counter


def prepare_data(phrase):
    # remove special characters that does not add to the word counter purpose
    translation_table = str.maketrans(dict.fromkeys('!"#$%&()*+-./:;<=>?@[\]^`{|}~'))
    # space, comma and underline are considered the valid word separators
    return phrase.translate(translation_table).replace(",", " ").replace("_", " ").split()


def mapper(word):
    if word[0] != "'" and word[-1] != "'":
        return {word.lower(): 1}

    # in case the word is quoted, should be unquoted for word count purpose
    return {word[1:-1].lower(): 1}


def reducer(word, word2):
    # when the compared word does not have the key,
    # i.e., they are not equal, add 0 to the current word counter
    for key in word2:
        word[key] = word.get(key, 0) + word2.get(key, 0)
    return word


def word_count(phrase):
    mapper_output = list(map(mapper, prepare_data(phrase)))
    return reduce(reducer, mapper_output)
