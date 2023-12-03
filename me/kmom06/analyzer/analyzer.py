#!/usr/bin/env python3
""" Functions for text analyzing """

from operator import itemgetter

def open_file(text_file, read_lines = False):
    """ Open file """
    with open(text_file, "r") as filehandler:
        content = filehandler.read()
    
    if read_lines:
        with open(text_file, "r") as filehandler:
            content = filehandler.readlines()

    return content

def remove_punctations(text):
    """ Remove punctaion, comma etc. from string """
    punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''  
    for letter in text:
        if letter in punc:
            text = text.replace(letter, "")
    return text


def sort_data(data, reverse = False):
    """ Sort data """
    data_sorted = sorted(data.items(), key=itemgetter(1, 0), reverse = reverse) #sort firt by key, then by value
    return data_sorted

def get_printable_data(data, text_file, letters = False):
    """ Create a printable string """
    if letters:
        nr_words = get_letters(text_file)
    else:
        nr_words = get_words(text_file)

    res_str = ""
    for item in data:
        calc = round(item[1] / nr_words * 100, 1)
        res_str += item[0] + ": " + str(item[1]) + " | " + str(calc) +  "%\n"
    
    return res_str.strip()

def get_lines(text_file):
    """ Return the number of lines from a file """
    lines = open_file(text_file, True)
    return len(lines)

def get_words(text_file):
    """ Return the number of lines from a file """
    words = open_file(text_file)
    words = words.split()
    return len(words)

def get_letters(text_file):
    """ Return the number of lines from a file """
    letters = open_file(text_file)
    clean_letters = remove_punctations(letters)
    clean_letters = clean_letters.split()
    clean_letters = "".join(clean_letters)

    return len(clean_letters)

def create_dict(text):
    """ Create a dictionary with nr of words or letters """
    new_dict = {}
    for item in text:
        if new_dict.get(item.lower()):
            new_dict[item.lower()] += 1
        else:
            new_dict[item.lower()] = 1

    return new_dict

def get_word_freq(text_file, nr_freq):
    """ Get the frequency of each word """
    text = open_file(text_file)
    text = remove_punctations(text)
    words = text.split()

    word_dict = create_dict(words)
    sorted_data = sort_data(word_dict, True)
    res = get_printable_data(sorted_data[:nr_freq], text_file) #send only the first nr of data

    return res

def get_letter_freq(text_file, nr_freq):
    """ Get the frequency of each word """
    letters = open_file(text_file)
    clean_letters = remove_punctations(letters)
    clean_letters = clean_letters.split()
    clean_letters = "".join(clean_letters)

    letter_dict = create_dict(clean_letters)
    sorted_data = sort_data(letter_dict, True)
    res = get_printable_data(sorted_data[:nr_freq], text_file, True) #send only the first nr of data
    
    return res

def get_all(text_file, nr_freq):
    """ Get all information """
    lines = get_lines(text_file)
    words = get_words(text_file)
    letters = get_letters(text_file)
    word_freq = get_word_freq(text_file, nr_freq)
    letter_freq = get_letter_freq(text_file, nr_freq)

    res = str(lines) + "\n" + str(words) + "\n" + str(letters) + "\n" + word_freq + "\n" + letter_freq

    return res

def write_to_file(data):
    """ Write data to a file """
    new_file = "output.txt"
    with open(new_file, "w") as filehandler:
        filehandler.write(data)
  
def write_data(alt, text_file, nr_freq):
    """ Write data to a new file """
    if alt == "lines":
        lines = str(get_lines(text_file))
        write_to_file(lines)
    elif alt == "words":
        words = str(get_words(text_file))
        write_to_file(words)
    elif alt == "letters":
        letters = str(get_letters(text_file))
        write_to_file(letters)
    elif alt == "word_frequency":
        word_freq = get_word_freq(text_file, nr_freq)
        write_to_file(word_freq)
    elif alt == "letter_frequency":
        letters_freq = get_letter_freq(text_file, nr_freq)
        write_to_file(letters_freq)
    elif alt == "all":
        all_data = get_all(text_file, nr_freq)
        write_to_file(all_data)
    elif alt == "change":
        print("Can't write 'change' to a file")
    else:
        print("Alternetive doesn't exist")
