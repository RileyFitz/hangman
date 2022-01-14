from csv import reader
from random import choice
from sys import argv

def main():
    # Load word bank
    word = select_from_wordbank()


def select_from_wordbank(wordbank='wordbank.csv'):
    '''
    Loads a csv file, and returns a list of words contained.
    Defaults to wordbank.csv but supports external csv files.
    '''
    try:
        if len(argv) > 1:
            wordbank = argv[1]
        with open(wordbank, newline='') as csvfile:
            csv_words =  reader(csvfile)
            words = list(csv_words)[0]
            word = choice(words).strip()
            return word
    except Exception as e:
        print(e)
        print("There above error occured while trying to load the wordbank..\nQuitting")
        quit()

def print_hangman(guesses=0):
    '''
    I know the if's ain't pretty, it's what I got atm.
    '''
    head, torso, larm, rarm, lleg, rleg = '','',' ','','',''

    if guesses >= 1:
        head = 'O'
    if guesses >= 2:
        torso = '|'
    if guesses >= 3:
        larm = '/'
    if guesses >= 4:
        rarm = '\\'
    if guesses >= 5:
        lleg = '/'
    if guesses >= 6:
        rleg = '\\'

    print('_______')
    print(f'|    |')
    print(f'|    {head}')
    print(f'|   {larm}{torso}{rarm} ')
    print(f'|   {lleg} {rleg} ')
    print('|_______')

if __name__=="__main__":
    main()
