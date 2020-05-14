# Gabriel Martinez
# April 2020

import sys
import json

# CLASS: Finds if a word matches the letters of another word.
class Unscramble:
    # METHOD: Initializes program.
    def __init__(self):
        self.__file_type = ""
        self.__input_letters = ""
        self.__dictionary = []
        self.__matched_letters = []
        self.__takeInput()
    
    #FUNCTION: Takes Input and decides what functions to call.
    def __takeInput(self):
        self.__dictionary_path = sys.argv[1]
        self.__file_type = self.__dictionary_path.split('.')[1]
        self.__storeDictionary()
        if  len(sys.argv) == 2:
            self.__findMostCommonLetters()
        elif len(sys.argv) == 3:
            self.__input_letters = ''.join(sorted(sys.argv[2]))
            self.__searchWord(self.__input_letters)


    # FUNCTION: Stores dictionary txt file into a list of words.
    def __storeDictionary(self):
        if self.__file_type == "txt":
            with open(self.__dictionary_path, 'r') as file:
                data = file.read()
            self.__dictionary = [line for line in data.split('\n') if line.strip()]
        if self.__file_type == "json":
            with open(self.__dictionary_path, 'r') as json_file:
                self.__dictionary = json.load(json_file)

    # FUNCTION: Searches dictionary for the letters of a word that appear
    # the most.
    def __findMostCommonLetters(self):
        most_common_letters = ""
        most_matches = 0
        checked_letters = ["" for words in  self.__dictionary]
        checked__count = 0
        for word in self.__dictionary:
            letters = ''.join(sorted(word))
            print(word)
            if letters not in checked_letters:
                checked_letters[checked__count] = letters
                checked__count = checked__count + 1
                matches = self.__searchWord(letters)
                if matches > most_matches:
                    most_matches = matches
                    most_common_letters = letters
        print("Most common letters in a word: {} \n Appeared {} Times".format
            (most_common_letters, most_matches))

    
    # FUNCTION: Searches dictionary to see if letters in input word matches.
    def __searchWord(self, letters):
        match_count = 0
        for word in self.__dictionary:
            sorted_word = ''.join(sorted(word))
            if(letters == sorted_word):
                match_count = match_count + 1
        return match_count

# FUNCTION: Main
if __name__ == "__main__":
    unscramble = Unscramble()
    sys.exit(0)
