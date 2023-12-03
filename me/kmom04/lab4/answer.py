#!/usr/bin/env python3

"""
10ad68dd8d794b34f8d8e884bd160c49
python
lab4
v4
elre23
2023-08-26 08:05:14
v4.0.0 (2019-03-05)

Generated 2023-08-26 10:05:14 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [bumblebee, floor] and [tiger, tiger].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_one = ['bumblebee', 'floor']
list_two = ['tiger', 'tiger']

added_list = list_one + list_two


ANSWER = added_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Add the words 'hotdog' and 'jacket' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = ['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker']
my_list.insert(1, 'hotdog')
my_list.insert(2, 'jacket')


ANSWER = my_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Replace the third word with: 'tablet'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = ['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker']
my_list[2] = 'tablet'


ANSWER = my_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [flute, guitar, drums, piano, bass]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = ['flute', 'guitar', 'drums', 'piano', 'bass']
my_list.sort(reverse = True)


ANSWER = my_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'Whitaker'
#
# from the list:
#
# > [Dafoe, Sheen, Berenger, Depp, Whitaker]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = ['Dafoe', 'Sheen', 'Berenger', 'Depp', 'Whitaker']
my_list.remove('Whitaker')


ANSWER = my_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = [67, 50, 2, 39, 15]


ANSWER = sum(my_list)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [98, 5, 12, 369, 1]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = [98, 5, 12, 369, 1]
average = round(sum(my_list)/len(my_list), 1)


ANSWER = average

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?wind?is?blowing"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_string = "The?wind?is?blowing"
my_list = my_string.split('?')
my_string = " ".join(my_list)


ANSWER = my_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [reggae, rock, blues, jazz, opera]
#
# and replace the second and third element with
#
# > "picture, canvas"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

my_list = ['reggae', 'rock', 'blues', 'jazz', 'opera']
my_list[1:3] = ['picture', 'canvas']


ANSWER = my_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [d, c, b, a, e]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ['d', 'c', 'b', 'a', 'e']
list2 = ['d', 'c', 'b', 'a', 'e']


ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = list1


ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "s"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1[0:1] = 's'


ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [567, 23, 12, 36, 7]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

def sort_list(list_to_be_sorted):
    """ Sort list in ascending order and multiply all vales with 10 """

    list_to_be_sorted.sort()
    for i, item in enumerate(list_to_be_sorted):
        list_to_be_sorted[i] = item * 10
    
    return list_to_be_sorted


ANSWER = sort_list([567, 23, 12, 36, 7])

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [98, 5, 12, 369, 1]
#
# as argument.
#
# The function should multiply all even numbers by 3 and add 9 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#

def modify_list(list_to_be_modified):
    """ Modify list by multiply even numbers with 3 and add 9 to odd numbers """

    modified_list = []
    for item in list_to_be_modified:
        if item % 2 == 0:
            modified_list.append(item * 3)
        else:
            modified_list.append(item + 9)
    
    modified_list.sort(reverse = True)

    return modified_list


ANSWER = modify_list([98, 5, 12, 369, 1])

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
