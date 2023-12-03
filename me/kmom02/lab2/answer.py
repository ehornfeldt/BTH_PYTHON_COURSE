#!/usr/bin/env python3

"""
d19e5abd35455b012e7c37307fed3822
python
lab2
v4
elre23
2023-08-14 10:03:58
v4.0.0 (2019-03-05)

Generated 2023-08-14 12:03:58 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 1, `dice2` = 4
# and `dice3` = 3.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 1
dice2 = 4
dice3 = 3

answ = dice1 > dice2

ANSWER = answ

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice_sum = dice1 + dice2 + dice3

if dice_sum > 11:
    answ = 'big'
else:
    answ = 'small'

ANSWER = answ

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 4 and `dice5` = 1 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 4
dice5 = 1

dice_sum = dice_sum + dice4 + dice5

if dice_sum < 11:
    answ = 'small'
elif 11 <= dice_sum < 21:
    answ = 'intermediate'
else:
    answ = 'big'

ANSWER = answ

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'restaurant'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = 'restaurant'

answ = 's' in summer_word

ANSWER = answ

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_str = ''
for nr in range(11):
    my_str += str(nr) + ','


ANSWER = my_str

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#

consonants = 'bcdfghjklmnpqrstvwxz'
new_word =  ''

for letter in summer_word:
    if consonants.find(letter) != -1:
        new_word = new_word + letter

ANSWER = new_word

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 30 to 60 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

odd_numbers = 0
for nr in range(30, 61):
    if (nr % 2) != 0:
        odd_numbers += nr

ANSWER = odd_numbers

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 5 and ends when the value is
# greater than 34, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

value = 5
values_str = ''

while value < 35:
    values_str += str(value) + ','
    value += 3

ANSWER = values_str

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 7 from 16, 68 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

value = 16
n = 0

while n < 68:
    value -= 7
    n += 1

ANSWER = value

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 8, 8!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 8 is `8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

n = 1
total = 1
while n < 9:
    total *= n
    n += 1

ANSWER = total

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'internationalization'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

word = 'internationalization'
reversed_word = ''

for letter in word:
    reversed_word = letter + reversed_word

ANSWER = reversed_word

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers (Not using
# new plates which can have more letters). The numbers range from 001 to 999.
# Using one of the four common rules of arithmetics (+, -, *, /), on how many
# of the numberplates can the two first numbers give the third number? We
# only care about the numbers, we ignore letters for this assignment.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Examples:
# '123' can be combined to 1 + 2 = 3. So this numberplate is good. Since this
# matched on + operator, we don't continue checking with the other operators.
# '129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#
nr_one = 0
nr_two = 0
nr_three = 1

count = 0

while True:
    if nr_one + nr_two == nr_three: 
        count += 1
    elif nr_one - nr_two == nr_three:
        count += 1
    elif nr_one * nr_two == nr_three:
        count += 1
    elif nr_two != 0 and nr_one / nr_two == nr_three:
        count += 1
    
    if nr_one < 10:
        nr_one += 1
    else:
        nr_one = 0
        if nr_two < 10:
            nr_two += 1
        else:
            nr_two = 0
            if nr_three < 10:
                nr_three += 1
            else:
                break
    
ANSWER = count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
