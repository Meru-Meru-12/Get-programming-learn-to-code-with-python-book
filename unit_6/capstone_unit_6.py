# The problem
# You're given two files containing text. Using the names of the files, write a program that reads the documents and uses a metric to determine how similar they are.
# Documents that are exactly the same should get a score of 1, and documents that don't have any words in common should get a score of 0.

def read_text(filename):
    inFile =  open(filename, 'r')
    line = inFile.read()
    return line

text =  read_text("sonnet18.txt")
print(read_text("sonnet18.txt"))

import string

def find_words(text):
    """
    text: string
    returns: list of words from input text
    """
    text = text.replace("\n", " ")
    for char in string.punctuation:
        text = text.replace(char, "")
    
    words = text.split(" ")
    return words

words = find_words(text)

def frequencies(words):
    """
    words: list of words
    returns: frequency dictionary for input words
    """
    freq_dict = {}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
        return freq_dict

freq_dict = frequencies(words)

def calculate_similarity(dict1, dict2):
    """
    dict1: frequency dictionary for one text
    dict2: frequency dictionnary for another text
    returns: float, representing how similar both texts are to each other
    """
    diff = 0
    total = 0
    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict1[word] - dict2[word])
        else:
            diff += dict1[word]
    
    for word in dict2.keys():
        if word not in dict1.keys():
            diff += dict2[word]
    total = sum(dict1.values()) + sum(dict2.values())
    difference = diff / total
    similar = 1.0 - difference

    return round(similar, 2)

text_1 = read_text("sonnet18.txt")
text_2 = read_text("sonnet19.txt")
words_1 = find_words(text_1)
words_2 = find_words(text_2)
freq_dict_1 = frequencies(words_1)
freq_dict_2 = frequencies(words_2)
print(calculate_similarity(freq_dict_1, freq_dict_2))