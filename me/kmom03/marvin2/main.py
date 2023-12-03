#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Main file """

import marvin1
import marvin2

def main():
    """ The main function """
    cat_image = r"""
   /\     /\
  {  `---'  }
  {  O   O  }
  ~~>  V  <~~
   \  \|/  /
    `-----'__
    /     \  `^\_
   {       }\ |\_\_   W
   |  \_/  |/ /  \_\_( )
    \__/  /(_E     \__/
      (  /
       MM
	"""

    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    stop = False

    while not stop:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(cat_image)
        print("Hej! Jag heter Merlin och svarar gärna på dina frågor. Vad vill du ha hjälp med?")
        print('Du har följande val:')
        print("1 - Presentera dig för Merlin")
        print("2 - Konvertera celsius till farenheit")
        print("3 - Ta reda på ditt betyg")
        print("4 - Ta reda på summan och medelvärdet för en mängd tal")
        print("5 - Lek med ett ord")
        print("6 - Ta reda på om en siffra som är större eller mindre än en annan")
        print("7 - Validera personnummer")
        print("8 - Rövarspråket")
        print("9 - Skapa personnummer")
        print("10 - Skapa acronym")
        print("11 - Slumpa en mening")
        print("12 - Hitta index")
        print("a1 - Kolla om vissa bokstäver finns i ett ord")
        print("a2 - Kontrollera att ett multiplicerat nummer har siffrorna 0-9 i sig")
        print("a3 - Slå ihop två namn")
        print("a4 - Räkna ut spelares poäng")
        print("b1 - Kolla om en sträng innehåller 3 andra strängar")
        print("q - Avsluta.")

        choice = input("Ditt val: ")

        if choice == "q":
            print("Hej då och välkommen åter!")
            stop = True

        elif choice == "1":
            marvin1.greet()

        elif choice == "2": 
            marvin1.celcius_to_fahrenheit()

        elif choice == "3":
            marvin1.points_to_grade()

        elif choice == "4":
            marvin1.sum_and_average()

        elif choice == "5":
            marvin1.hyphen_string()
		
        elif choice == "6":
            marvin1.compare_numbers()

        elif choice == "7":
            marvin1.validate_ssn()
	
        elif choice == "8":
            marvin1.robber_language()

        elif choice == "9":
            birth = input("Skriv in ditt födelsedatum i formen ÅÅMMDD: ")
            ssn = marvin2.create_ssn(birth) 
            print(ssn)
        
        elif choice == "10":
            meaning = input("Skriv en mening: ")
            acronym = marvin2.get_acronym(meaning)
            print(acronym)
        
        elif choice == "11":
            meaning = input("Skriv en mening: ")
            random_meaning = marvin2.randomize_string(meaning)
            print(meaning + " --> " + random_meaning)

        elif choice == "12":
            first_line = input("Skriv ditt första ord: ")
            second_line = input("Skriv ditt andra ord: ")
            indexes = marvin2.find_all_indexes(first_line, second_line)
            print(indexes)

        elif choice == "a1":
            marvin1.combined_words()

        elif choice == "a2":
            marvin1.multiplied_numbers()

        elif choice == "a3":
            marvin1.two_names()

        elif choice == "a4":
            marvin1.players_points()

        elif choice == "b1":
            first_word = input("Skriv ett ord: ")
            second_word = input("Skriv ett andra ord: ")
            third_word = input("Skriv ett tredje ord: ")
            fourth_word = input("Skriv ett fjärde ord: ")
            match_or_no = marvin2.has_strings(first_word, second_word, third_word, fourth_word)
            print(match_or_no)

        else:
            print("Välj ett alternatv ur menyn.")
        
        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
