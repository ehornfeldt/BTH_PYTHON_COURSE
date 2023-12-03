#!/usr/bin/env python3
""" Functions for training writing speed and corecctness """
from operator import itemgetter
import time
import score_functions

def read_file(filename):
    """ Read file """
    with open(filename, "r") as filehandler:
        content = filehandler.read()

    return content

def sort_data(data, reverse = False):
    """ Sort data """
    data_sorted = sorted(data.items(), key=itemgetter(1, 0), reverse = reverse)
    return data_sorted

def calculate_time(seconds):
    """ Get time i minutes """
    minutes = 0
    if seconds <= 60:
        minutes = 1
    elif seconds > 60:
        rest = seconds % 60
        minutes = (seconds - rest) / 60
        if rest >= 30:
            minutes += 1
    
    return minutes

def get_diff(data, user_data):
    """ If user word/line is longer or shorter then original, return the diff """
    diff = ""
    if len(user_data) > len(data):
        diff = user_data[len(data):]
    elif len(user_data) < len(data):
        diff = data[len(user_data):]
    return diff

def find_right_letters(word, user_word, data):
    """ Find, calculate and save right characters """
    for index, letter in enumerate(word):
        try:
            if letter == user_word[index]:
                data[1] += 1 #right chars
            else:
                if data[2].get(letter):
                    data[2][letter] += 1 #wrong chars
                else:
                    data[2][letter] = 1 #wrong chars
        except IndexError:
            #The user input word is shorter than original, ignoring and continuing.
            pass
    
    diff = get_diff(word, user_word)
    if len(diff) > 0:
        if len(user_word) > len(word):
            data[1] -= len(diff) #right chars
        for letter in diff:
            if data[2].get(letter):
                data[2][letter] += 1 #wrong chars
            else:
                data[2][letter] = 1 #wrong chars

    return data

def find_right_words(words, user_words, data):
    """ Find and calculate right words """
    for index, word in enumerate(words):
        try:   
            if user_words[index]:
                if word == user_words[index]:
                    data[0] += 1 #right words
                temp = find_right_letters(word, user_words[index], data)   
                data[1] = temp[1] #right chars
                data[2] = temp[2] #wrong chars
        except IndexError:
            #The user input line is shorter than original. Calculate wrong chars from the rest of the orginial words
            find_right_letters(word, "", data)

    diff = get_diff(words, user_words)
    if len(diff) > 0 and len(user_words) > len(words):
        data[0] -= len(diff) #right words
        for word in diff:
            find_right_letters("", word, data)

    return data

def split_lines(lines, user_lines):
    """ Splitting lines into line """
    #data will include: right words, right chars, wrong chars
    data = [0, 0, {}]

    for index, line in enumerate(lines):
        words = line.split()
        user_words = user_lines[index].split()
        temp = find_right_words(words, user_words, data)
        data[0] = temp[0] #right words
        data[1] = temp[1] #right chars
        data[2] = temp[2] #wrong chars
    
    return data

def calc_user_words(user_lines):
    """ Calculate total user input words """
    nr_words = 0
    for line in user_lines:
        nr_words += len(line.split())
    
    return nr_words

def calculate_score(data, total_words, total_chars, exec_time, total_user_words):
    """ Calculate score """
    #right words is data[0]
    #right chars is data[1]
    #wrong chars is data[2]

    score_words = data[0] / total_words * 100 #right words / total words
    score_chars = data[1] / total_chars * 100 #right chars / total chars
    wrong_chars_sorted = sort_data(data[2], True) #wrong chars

    executed_time = calculate_time(exec_time)
    wrong_words = total_user_words - data[0]
    gross_wpm = total_user_words / executed_time
    net_wpm = gross_wpm - (wrong_words / executed_time)

    return (score_words, score_chars, wrong_chars_sorted, gross_wpm, net_wpm, executed_time)

def get_lines(content):
    """ Display lines from file and save user lines """
    lines = content.splitlines()
    user_lines = []

    for line in lines:
        print(line)
        user_input = input()
        user_lines.append(user_input)

    return user_lines

def start_writing_test(filename, level):
    """ Starting the writing test """
    content = read_file(filename)
    start_time = time.time()
    user_lines = get_lines(content)
    executed_time = time.time() - start_time
    lines = content.splitlines()

    total_words = len(content.split())
    total_user_words = calc_user_words(user_lines)
    total_chars = len(content) - content.count(" ") - content.count("\n")

    #Calculate words and characters, starting with splitting lines
    result = split_lines(lines, user_lines)
    score_tup = calculate_score(result, total_words, total_chars, executed_time, total_user_words)

    print("\nWell done!")
    input("Press enter to see your score")
    printable_score = score_functions.score(score_tup)
    print("\n------------------------------------------")
    print("Your score:")
    print("------------------------------------------")
    print(printable_score)

    user_name = input("Enter your name to add to highscore: ")
    score_functions.save_score(user_name, score_tup[0], level)

def get_highscore(filename):
    """ Get high score """
    print(read_file(filename))
