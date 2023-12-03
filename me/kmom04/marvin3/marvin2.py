#!/usr/bin/env python3
""" Functions from kmom03 """

import random
import math


def calculate_luhna_sum(ssn):
    """ Calculates the sum of a ssn """

    one_or_two = 2
    nr_sum = 0

    for number in ssn:
        if int(number) * one_or_two > 9:
            new_str = str(int(number) * one_or_two)
            for num in new_str:
                nr_sum += int(num)
        else:
            nr_sum += int(number) * one_or_two

        if one_or_two == 1:
            one_or_two = 2
        else:
            one_or_two = 1

    return nr_sum


def create_ssn(birth):
    """ Creates a whole personal number with 4 last numbers """
    last_three = random.randint(100, 999)
    ssn_sum = int(calculate_luhna_sum(birth + str(last_three)))

    sum_round = math.ceil(ssn_sum / 10.0) * 10
    last_number = sum_round - ssn_sum
    
    return birth + "-" + str(last_three) + str(last_number)


def get_acronym(meaning):
    """ Create a acronym from a users input """
    acronym = ""

    for letter in meaning:
        if letter.isupper():
            acronym += letter
    
    return acronym


def randomize_string(meaning):
    """ Randomize a string """
    random_meaning = [*meaning]
    random.shuffle(random_meaning)
    res = "".join(random_meaning)
    return res


def find_all_indexes(first_line, second_line):
    """ Find indexes from two user inputs """
    start = 0
    stop = len(first_line)
    indexes = ""

    while start < len(first_line):
        
        try:
            if indexes and first_line.index(second_line, start, stop):
                indexes += ","
            index = first_line.index(second_line, start, stop)
            indexes += str(index)
            start = index + 1
        except ValueError:
            break

    return indexes

def has_strings(first_word, second_word, third_word, fourth_word):
    """ Check if second- is at start, third- in middle and fourth word in the end of the first word """

    match_or_no = ""
    if first_word.startswith(second_word) and third_word in first_word and first_word.endswith(fourth_word):
        match_or_no = "Match"
    else:
        match_or_no = "No match"

    return match_or_no
