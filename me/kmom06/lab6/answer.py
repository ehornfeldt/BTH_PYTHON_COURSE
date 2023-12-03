#!/usr/bin/env python3

"""
f7cf040e5ab4ef3524cb6f58a502af16
python
lab6
v4
elre23
2023-09-10 13:52:54
v4.0.0 (2019-03-05)

Generated 2023-09-10 15:52:54 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#



# --------------------------------------------------------------------------
# Section 1. Files
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `quotes.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#

filename = 'quotes.txt'

with open(filename, "r") as filehandle:
    file_content = filehandle.read()

ANSWER = len(file_content)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 1.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = file_content.split('\n')[0]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of quotes.txt and remove the 5 last rows.
# Then replace line number 5 with the new string "I am replaced".
# Then, create a new file called `newQuotes.txt` where you save the new
# changes. Replace `newQuotes.txt` if it already exists.
#
# Answer with the new content inside `newQuotes.txt`. Don't have a "\n" on
# the last line.
#
# Write your code below and put the answer into the variable ANSWER.
#

quote_file = "newQuotes.txt"

with open(filename, "r") as filehandler2:
    lines = filehandler2.readlines()
    new_lines = lines[:-5]
    new_lines[4] = "I am replaced\n"
    new_content = "".join(new_lines).strip()

with open(quote_file, "w") as filehandler3:
    filehandler3.write(new_content)

with open(quote_file, "r") as filehandler4:
    content = filehandler4.read()

ANSWER = content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"The important thing is not to stop questioning."*
#
# Write your code below and put the answer into the variable ANSWER.
#

with open(quote_file, "a") as f:
    f.write("\n" + "The important thing is not to stop questioning.")

with open(quote_file, "r") as f2:
    content = f2.read()

ANSWER = content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines that `passwords.txt` has and create a new
# file called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#

pass_file = "passwords.txt"
new_pass_file = "newPasswords.txt"

with open(pass_file, "r") as handle:
    lines = handle.readlines()

nr_of_empty_lines = 0
new_content = []

for line in lines:
    if line == "\n":
        nr_of_empty_lines += 1
    else:
        new_content.append(line)

new_content = "".join(new_content)

with open(new_pass_file, "w") as handle_write:
    handle_write.write(new_content)

with open(new_pass_file, "r") as handle_new_file:
    new_file = handle_new_file.read()

result = "passwords.txt has " + str(nr_of_empty_lines) + " empty lines and contains: " + new_file

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 1, 2 and 3 from `quotes.txt` to a new
# file that you create called `extraQuotes.txt`. Replace `extraQuotes.txt` if
# it already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: - Jon
# Doe"
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#

extra_quotes_file = "extraQuotes.txt"
with open(filename, "r") as handle:
    lines= handle.readlines()
temp = lines[:3]
new_content = "".join(temp).strip()

with open(extra_quotes_file, "w") as handle:
    handle.write(new_content)

with open(extra_quotes_file, "r") as handle:
    extra_quotes = handle.read()
characters = 0
chars_second_line = ""
nr_of_lines = 1

for letter in extra_quotes:
    if not letter == "\n":
        characters += 1
    if letter == "\n":
        nr_of_lines += 1
    if nr_of_lines == 2 and not letter == "\n":
        chars_second_line += letter

result = ("The file has " + str(characters) + " characters and the 9 first of the second row are: " + 
    chars_second_line[:9])

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)


dbwebb.exit_with_summary()
