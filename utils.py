from csv import reader
from random import choice
from sys import argv
from os import system
from string import ascii_lowercase

def print_info(word, used, unused):
    '''
    Prints informative messages to ensure easy gameplay.
    '''
    blanks_string = ''
    print(f'Remaining letters: {unused}')
    print(f'Guessed letters: {used}')

    for let in word:
        if let in used:
            blanks_string += f'{let.upper()} '
        else:
            blanks_string += '_ '
    print(f'\n{blanks_string}\n')

def check_win(word, used):
    count = 0
    for let in word:
        if let in used:
            count += 1
    if count == len(word):
        return True
    return False

def validated_guess(used):
    '''
    Ensures that only a single letter can be returned as an attempted guess.
    '''
    while True:
        try:
            inp = input('Next guess: ').lower()
            if len(inp) > 1 or inp not in ascii_lowercase:
                print("Guess's must be a single letter. Please try again..")
            elif inp in used:
                print(f'You already guessed {inp}. Please try a different guess.')
            else:
                return inp
        except Exception as e:
            print(f'The following exception occured.\n{e}')
            print('Please try an input again.')

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
            word = choice(words).strip().lower()
            word = ''.join([i for i in word if not i.isdigit()]) # Removes any possible digits.
            return word
    except Exception as e:
        print(e)
        print("There above error occured while trying to load the wordbank..\nQuitting")
        quit()

def print_hangman(guesses=0):
    '''
    I know the if's ain't pretty, it's what I got atm.
    '''
    system('clear') # Only supports mac and linux systems.
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
    print('|_______\n')
