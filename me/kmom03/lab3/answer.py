#!/usr/bin/env python3

"""
96e132832d6ccc8686f1165a5f5eb4d2
python
lab3
v4
elre23
2023-08-18 08:32:05
v4.0.0 (2019-03-05)

Generated 2023-08-18 10:32:05 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
import functions


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'test'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def valid_password(password):
    """ Function checking if password is valid """
    nr_of_characters = False
    contain_upper = False
    contain_lower = False
    contain_number = False

    if len(password) > 8:
        nr_of_characters = True

    for letter in password:
        if letter.isdigit():
            contain_number = True
        elif letter.isupper():
            contain_upper = True
        elif letter.islower():
            contain_lower =  True
        
        if contain_number and contain_upper and contain_lower:
            break
    
    return nr_of_characters and contain_number and contain_upper and contain_lower 

ANSWER = valid_password("test")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'anoth3ePw0Rd'.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = valid_password("anoth3ePw0rd")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy. Your solution should be
# case-insensitive.
#
# Answer with the number of vowels in the following text:
#
# 'How brief our moment of life is. How to be steadfast, and strong, and in
# control of yourself.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(word):
    """ Function checking how many vowels a word has """
    vowels = "aeiouy"
    res_string = ""

    for letter in word:
        if letter.upper() in vowels.upper():
            res_string += letter
    
    return len(res_string)

ANSWER = number_of_vowels("How brief our moment of life is. " 
"How to be steadfast, and strong, and in control of yourself.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value anoth3ePw0Rd the function should return the following
# string: 'anoth3ePw0Rd is a valid password and contains 3 vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: secretpassw0rd.
#
# Write your code below and put the answer into the variable ANSWER.
#

def analyze_password(password):
    """ Function checking if password is valid and how many vowels the password has """
    is_passw_valid = valid_password(password)
    nr_of_vowels = number_of_vowels(password)

    valid = ""
    if not is_passw_valid:
        valid = "not"

    result = password + " is " + valid + " a valid password and contains " + str(nr_of_vowels) + " vowels."

    return result


ANSWER = analyze_password("secretpassw0rd")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `multiplication` that takes
# two arguments. The function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 81 and 69.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = functions.multiplication(81, 69)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'beach' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = functions.funny_word("beach")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `decider`. The function takes
# one argument. If the argument is a string return a call to `funny_word()`,
# if the argument is an integer return the square of the argument by using
# the `multiplication` function.
#
# Answer with a call to the function `decider` with the value
# `hemidemisemiquaver` as argument.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = functions.decider("hemidemisemiquaver")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# 'blunderbuss' and 84 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = functions.double_decider("blunderbuss", 84)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)


dbwebb.exit_with_summary()
