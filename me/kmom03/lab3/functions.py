#!/usr/bin/env python3
""" Modules """

def multiplication(nr_one, nr_two):
    """ Function multiplying two nummbers """
    try:
        return nr_one * nr_two

    except ValueError:
        print("Only numbers can be multiplied")
        return -1

def funny_word(word):
    """ Function returning a funny word """
    return str(word) + " is a funny word"

def decider(arg):
    """ 
    Functtion returning a square if argument is a number, or a funny word if arggument is a string
    """
    if isinstance(arg, int):
        return multiplication(arg, arg)
    return funny_word(arg)

def double_decider(arg_one, arg_two):
    """ Function doing decider function with two arguments """
    arg_one_str = str(decider(arg_one))
    arg_two_str = str(decider(arg_two))

    return arg_one_str + " and the square is " + arg_two_str
