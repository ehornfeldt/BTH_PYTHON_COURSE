#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Main file """

import writing_functions

easy_file = "typing/easy.txt"
medium_file = "typing/medium.txt"
hard_file = "typing/hard.txt"
highscore = "score.txt"

def main():
    """ Program that tests your write-on-keyboard-skills """

    stop = False

    while not stop:
        
        print("----------------------------------\n")
        print("1) Test easy")
        print("2) Test medium")
        print("3) Test hard")
        print("4) Highscore")
        print("q) Quit")

        print("\nq: Quit")

        choice = input("\nYour choice: ")

        if choice == "q":
            print("Bye bye!")
            stop = True

        elif choice == "1":
            writing_functions.start_writing_test(easy_file, "easy")
        elif choice == "2":
            writing_functions.start_writing_test(medium_file, "medium")
        elif choice == "3":
            writing_functions.start_writing_test(hard_file, "hard")
        elif choice == "4":
            try:
                writing_functions.get_highscore(highscore)
            except FileNotFoundError:
                print("No score exists yet")
        else:
            print("Oops! Pick a choice from the menu")
        
        print("\n")


if __name__ == "__main__":
    main()
