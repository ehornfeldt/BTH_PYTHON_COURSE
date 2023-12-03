#!/usr/bin/env python3
""" Functions from kmom02 """

import marvin2

def greet():
    """ Prints a greeting """
    name = input("Vad heter du? ")
    print("\n", "Merlin säger:\n")
    print(f"Hej {name} - roligt att träffas!")


def celcius_to_fahrenheit(): 
    """ Converts Celcius to Farenheit """
    celsius = input("Ange grader i celsius (så får du svaret i farenheit): ")
    try:
        celsius = round(float(celsius) * 9 / 5 + 32, 2)
        print(celsius)
    except ValueError:
        print("Ange celcius i grader (siffror)")


def points_to_grade():
    """ Calculates a grade """
    #Kontrollerar att poängen som anges är i siffror
    while True:
        try:
            max_points = float(input("Ange maxpoäng: "))
            points = float(input("Ange dina poäng: "))
            break
        except ValueError:
            print("Ange siffror")
    grade = ""

    #Räknar ut betyget
    if points / max_points >= 0.9:
        grade = "A"
    elif points / max_points >= 0.8:
        grade = "B"
    elif points / max_points >= 0.7:
        grade = "C"
    elif points / max_points >= 0.6:
        grade = "D"
    elif points / max_points < 0.6:
        grade = "F"
    
    print("score:", grade)


def sum_and_average():
    """ Calculates a sum and average from two numbers """
    print("Ange dina nummer du vill summera, när du är nöjd skriver du 'done'")
    count_numbers = 0
    sum_numbers = 0

    #Kontrollerar att användaren skriver en siffra eller 'done'
    #Koden körs så länge använder inte skriver 'done'
    while True:
        nr_or_done = input("Nytt nummer: ")
        if nr_or_done == 'done':
            break
        
        else: 
            try:
                sum_numbers += float(nr_or_done)
                count_numbers += 1
            except ValueError:
                print("Ange ett nummer, eller 'done' om du är klar")
    
    print("The sum of all numbers are ", round(sum_numbers, 2), 
    " and the average is ", round(sum_numbers/count_numbers, 2))


def hyphen_string():
    """ Adds an extra letter with an hyphen """
    #Användaren kan skriva vilka tecken som helst.
    word = input("Skriv ett ord: ")
    play_word = ""
    nr_of_letters = 1

    for letter in word:
        for _ in range(nr_of_letters):
            play_word += letter
        nr_of_letters += 1
        if nr_of_letters == len(word) + 1:
            break
        play_word += "-"

    print(play_word)


def compare_numbers():
    """ Check if a number is smaller, larger or the same as another number """
    print("Ta reda på om en siffra är större, lika med eller mindre än en annan siffra."
    " Skriv din siffra eller skriv 'done' när du är klar")

    #Kontrollerar att använder skriver en siffra eller done - då bryts loopen
    while True:
        number = input("Skriv en siffra: ")
        if number == "done":
            break
        try:
            number = int(number)
            break
        except ValueError:
            print("not a number!")

    #Kontrollera att användaren skriver en till siffra eller done - då bryts loopen
    #Om användaren skrev done redan vid första inputen, bryts loopen
    while True:
        if number == "done":
            break

        next_number = input("Skriv en siffra: ")
        if next_number == "done":
            break
        
        try:
            next_number = int(next_number)

            if next_number > number:
                print("larger!")
            elif next_number == number:
                print("same!")
            else:
                print("smaller!")
            
            number = next_number

        except ValueError:
            print("not a number!")


def validate_ssn():
    """ Check if a personal number is valid """
    
    while True:
        person_nr = input("Skriv personnummer med 10 siffror: ")
        person_nr = person_nr.replace("-", "")

        try:
            int(person_nr)
            nr_sum = marvin2.calculate_luhna_sum(person_nr)

            if nr_sum % 10 == 0:
                print("Valid")
                break
            else:
                print("Not Valid")
                break

        except ValueError:
            print("Skriv in ditt personummer med siffror")


def robber_language():
    """ Convert a string t a robber string """
    word = input("Skriv ditt ord: ")
    consonants = 'bcdfghjklmnpqrstvwxz'
    rovar_word = ""

    for letter in word:
        if letter in consonants:
            rovar_word += letter + "o" + letter
        else:
            rovar_word += letter
    
    print(rovar_word)


def combined_words():
    """ Check if a second input includes in a first input """
    first_word = input("Skriv ett ord: ").upper()
    second_word = input("Skriv nästa ord: ").upper()
    not_included = False

    for letter in second_word:
        if letter not in first_word:
            not_included = True
            break
        first_word.replace(letter, "")
    
    if not_included:
        print("No match!")
    else:
        print("Match")


def multiplied_numbers():
    """ Check if a string with numbers includes 0-9 by multiply the number with 2 a defined nr of times """
    #Kontrollerar att användaren skriver in siffror och bryter då loopen
    while True: 
        try:
            number = int(input("Skriv din siffra: "))
            tries = int(input("Hur många ggr ska jag försöka? "))
            break
        except ValueError:
            print("Ange siffror")
        
    multi_nr = 2
    count = 0
    success = False

    for _ in range(tries):
        #Kontrollerar att siffrorna 0-9 är med i det angivna numret
        if all(i in str(number) for i in ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]):
            success = True
            break
        number *= multi_nr
        count += 1
    
    if success:
        print("Answer: ", count, " times")
    else:
        print("Answer: -1 times")


def two_names():
    """ Add two names together """
    vowels = "aeiouy"
    first_name = input("Skriv första namnet: ")
    second_name = input("Skriv andra namnet: ")
    #Sätter initialt index till sista boskstaven i ordet
    index_first_name = len(first_name) -1
    index_second_name = len(second_name) -1
    temp_index = 0

    for vowel in vowels:
        temp_index = first_name.find(vowel)
        if 0 <= temp_index <= index_first_name:
            index_first_name = temp_index
        temp_index = second_name.find(vowel)
        if 0 <= temp_index <= index_second_name:
            index_second_name = temp_index
    
    res_name = first_name[0 : index_first_name] + second_name[index_second_name : len(second_name)]
    print(res_name)


def players_points():
    """ Calculate points for defined players """
    users_input = input("Ange namnet på spelarna och dess poäng: ")

    player = ""
    score = 0
    win_lost = ""
    counted_players = ""
    result = ""
    this_player = False
    add_player = False


    for outer_letter in users_input:
        for inner_letter in users_input:
            if (outer_letter.lower() == inner_letter.lower() and 
            not outer_letter.lower() in counted_players.lower() and not inner_letter.isdigit()):
                this_player = True
                add_player = True
                if inner_letter.islower():
                    player = inner_letter
                    win_lost = "win"
                elif inner_letter.isupper():
                    player = inner_letter
                    win_lost = "lost"
            if this_player and inner_letter.isdigit() and win_lost == "win":
                score += int(inner_letter)
                this_player =  False
            elif this_player and inner_letter.isdigit() and win_lost == "lost":
                score -= int(inner_letter)
                this_player =  False
        
        if add_player:
            result += player.lower() + " " + str(score) + ", "
            add_player = False
        counted_players += outer_letter
        score = 0
    
    print(result)
