#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The cat with a simple menu to start up with.
The cat doesnt do anything, just presents a menu with some choices.
You should add functinoality to the cat.
"""

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

cat_name = 'Merlin'

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(cat_image)
    print("Hej! Jag heter ", cat_name, " och svarar gärna på dina frågor. Vad vill du ha hjälp med?")
    print('Du har följande val:')
    print("1 - Presentera dig för ", cat_name)
    print("2 - Konvertera celsius till farenheit")
    print("3 - Ta reda på ditt betyg")
    print("4 - Ta reda på summan och medelvärdet för en mängd tal")
    print("5 - Lek med ett ord")
    print("6 - Ta reda på om en siffra som är större eller mindre än en annan")
    print("7 - Validera personnummer")
    print("8 - Rövarspråket")
    print("a1 - Kolla om vissa bokstäver finns i ett ord")
    print("a2 - Kontrollera att ett multiplicerat nummer har siffrorna 0-9 i sig")
    print("a3 - Slå ihop två namn")
    print("a4 - Räkna ut spelares poäng")
    print("q - Avsluta.")

    choice = input("Ditt val: ")

    if choice == "q":
        print("Hej då och välkommen åter!")
        stop = True

    elif choice == "1":
        name = input("Vad heter du? ")
        print("\n", cat_name, " säger:\n")
        print(f"Hej {name} - roligt att träffas!")

    elif choice == "2": 
        celsius = input("Ange grader i celsius (så får du svaret i farenheit): ")
        try:
            celsius = round(float(celsius) * 9 / 5 + 32, 2)
            print(celsius)
        except ValueError:
            print("Ange celcius i grader (siffror)")

    elif choice == "3":
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
        
        print("score: ", grade)

    elif choice == "4":
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

    elif choice == "5":
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
    
    elif choice == "6":
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

    elif choice == "7":
        while True:
            person_nr = input("Skriv personnummer med 10 siffror: ")
            person_nr = person_nr.replace("-", "")

            #Kontrollerar att användaren skrivit in ett personnummer med siffror efter att - är borta
            try:
                int(person_nr)
                one_or_two = 2
                nr_sum = 0

                for nr in person_nr:
                    if int(nr) * one_or_two > 9:
                        new_str = str(int(nr) * one_or_two)
                        for n in new_str:
                            nr_sum += int(n)
                    else:
                        nr_sum += int(nr) * one_or_two

                    if one_or_two == 1:
                        one_or_two = 2
                    else:
                        one_or_two = 1

                if nr_sum % 10 == 0:
                    print("Valid")
                    break
                else:
                    print("Not Valid")
                    break

            except ValueError:
                print("Skriv in ditt personummer med siffror")

    
    elif choice == "8":
        word = input("Skriv ditt ord: ")
        consonants = 'bcdfghjklmnpqrstvwxz'
        rovar_word = ""

        for letter in word:
            if letter in consonants:
                rovar_word += letter + "o" + letter
            else:
                rovar_word += letter
        
        print(rovar_word)

    elif choice == "a1":
        first_word = input("Skriv ett ord: ").upper()
        second_word = input("Skriv nästa ord: ").upper()
        not_included = False

        for letter in second_word:
            if letter not in first_word:
                not_included = True
                break
            first_word = first_word.replace(letter, "1", 1)
        
        if not_included:
            print("No match!")
        else:
            print("Match!")

    elif choice == "a2":
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
            print(count, "times")
        else:
            print("-1 times")

    elif choice == "a3":
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

    elif choice == "a4":
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

    else:
        print("Välj ett alternatv ur menyn.")

    if not stop:
        input("\nPress enter to continue...")
