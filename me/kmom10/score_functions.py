#!/usr/bin/env python3
""" Score functions """

def find_category(wpm):
    """ Find category """
    if wpm < 10:
        category = "Sengångare"
    elif wpm < 20:
        category = "Snigel"
    elif wpm < 30:
        category = "Sjöko"
    elif wpm < 40:
        category = "Människa"
    elif wpm < 50:
        category = "Gasell"
    elif wpm < 60:
        category = "Struts"
    elif wpm < 70:
        category = "Gepard"
    elif wpm < 80:
        category = "Svärdfisk"
    elif wpm < 90:
        category = "Sporrgås"
    elif wpm < 100:
        category = "Taggsjärtseglare"
    elif wpm < 120:
        category = "Kungsörn"
    else:
        category = "Pilgrimsfalk"
    
    return category

def sort_score(data):
    """ Sort score in level and word score order """
    data_sorted = sorted(data.items(), key=lambda x: (x[1]['level'], float(x[1]['word_score'])), reverse = True)
    sorted_str = ""
    for item in data_sorted:
        first_spaces = 15 - len(item[1]['username'][:14])
        second_spaces = 10 - len(format(item[1]['word_score'], '.2f'))
        sorted_str += (item[1]['username'][:14] + " " * first_spaces + 
            format(item[1]['word_score'], '.2f') + " " * second_spaces)
        if item[1]['level'] == 1:
            sorted_str += "easy" + "\n"
        elif item[1]['level'] == 2:
            sorted_str += "medium" + "\n"
        elif item[1]['level'] == 3:
            sorted_str += "hard" + "\n"
    
    return sorted_str

def save_score(user_name, score_words, lev):
    """ Save user and score to file """
    if lev == "easy":
        level = 1
    elif lev == "medium":
        level = 2
    else:
        level = 3
    data = {}
    index = 0
    try:
        with open("score.txt", "r") as filehandler:
            for line in filehandler:
                score_float = line[15:25].split()
                if len(score_float) > 0:
                    word_score = float(score_float[0])
                    if "easy" in line[25:]:
                        data[index] = {"username": line[0:15], "word_score": word_score, "level": 1}
                    elif "medium" in line[25:]:
                        data[index] = {"username": line[0:15], "word_score": word_score, "level": 2}
                    elif "hard" in line[25:]:
                        data[index] = {"username": line[0:15], "word_score": word_score, "level": 3}
                index += 1
        
        data[index] = {"username": user_name, "word_score": score_words, "level": level}
        sorted_data = sort_score(data)
        
        with open("score.txt", "w") as filehandler:
            filehandler.write(sorted_data)
    except FileNotFoundError:
        first_spaces = 15 - len(user_name[:14])
        second_spaces = 10 - len(score_words)
        data = user_name[:14] + " " * first_spaces + score_words + " " * second_spaces + lev
        
        with open("score.txt", "w") as filehandler:
            filehandler.write(data)

def score(score_tup):
    """ Create score, score_tup includes: score words, score chars, wrong chars sorted, 
        gross wpm, net wpm, executed time """
    
    category = find_category(score_tup[4]) #net_wpm

    wrong_chars_string = ""
    for tup in score_tup[2]: #wrong chars sorted
        wrong_chars_string += tup[0] + ": " + str(tup[1]) + "\n"

    score_string = ("Word precision: " + format(float(score_tup[0]), '.2f') + "%\n" + 
        "Characters precision: " + format(float(score_tup[1]), '.2f') + "%\n" + 
        "Misspelled characters:\n" + wrong_chars_string + "\n" + "---------------------" + "\nTime: " + 
        str(score_tup[5]) + " minutes\n" + "Gross WPM: " + format(float(score_tup[3]), '.2f') + 
        "\nNet WPM: " + format(float(score_tup[4]), '.2f') + "\nYou write as a: " + category + "\n\n")

    return score_string
