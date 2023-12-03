#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Main file """

import analyzer

def main():
    """ A word counter """

    stop = False
    filename = "phil.txt"
    nr_freq = 7

    while not stop:
        
        print("----------------------------------\n")
        print("lines: get nr of lines")
        print("words: get number of words")
        print("letters: get number of letters")
        print("word_frequency: get the frequnecy of the words")
        print("letter_frequency: get the frequency of the letters")
        print("all: get all information")
        print("change: change file")
        print("write [choice]: write the above choices to a new file")

        print("\nq: Quit")

        choice = input("\nYour choice: ").lower()

        if choice == "q":
            print("Bye bye!")
            stop = True

        elif choice == "lines":
            lines = analyzer.get_lines(filename)
            print(lines)
        elif choice == "words":
            words = analyzer.get_words(filename)
            print(words)
        elif choice == "letters":
            letters = analyzer.get_letters(filename)
            print(letters)
        elif choice == "word_frequency":
            word_freq = analyzer.get_word_freq(filename, nr_freq)
            print(word_freq)
        elif choice == "letter_frequency":
            letter_freq = analyzer.get_letter_freq(filename, nr_freq)
            print(letter_freq)
        elif choice == "all":
            all_data = analyzer.get_all(filename, nr_freq)
            print(all_data)
        elif choice == "change":
            new_file = input("Enter a new filename: ")
            filename = new_file
            print(new_file, "is set!")
        elif "write" in choice:
            alt = choice.split()
            try:
                analyzer.write_data(alt[1], filename, nr_freq)
            except IndexError:
                print("Missing choice alternative")

        else:
            print("Oops! Pick a choice from the menu")
        
        print("\n")

if __name__ == "__main__":
    main()
