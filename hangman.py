from csv import reader
from random import choice
from sys import argv

def main():
    # Load word bank
    words = get_wordbank()
    for word in words:
        print(word)

def get_wordbank(wordbank='wordbank.csv'):
    '''
    Loads a csv file, and returns a list of words contained. 
    '''
    try:
        if len(argv) > 1:
            wordbank = argv[1]
        with open(wordbank, newline='') as csvfile:
            csv_words =  reader(csvfile)
            words = list(csv_words)
            return words[0]
    except Exception as e:
        print(e)
        print("There above error occured while trying to load the wordbank..\nQuitting")
        quit()

if __name__=="__main__":
    main()
