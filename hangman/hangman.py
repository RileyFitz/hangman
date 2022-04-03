from string import ascii_lowercase
from utils import *

def main():
    word = select_from_wordbank()
    win, attempts = play_game(word)
    if not win:
        print_hangman(attempts)
        print('You didn\'t guess the word in time! Your man was hung! (⌣́_⌣̀)')
        print(f'The word you were trying to guess was: {word.upper()}\n')
        print('Try your skill in another game!')
    else:
        print_hangman(attempts)
        print(f'You saved your man with {6-attempts} guesses remaining!\nCongratulations!\n')
        print('Try your luck with another game!')

def play_game(word):
    '''
    Main game mechanics contained here. 
    '''
    used = ''
    unused = ascii_lowercase
    attempts = 0
    win = False
    message = ''

    while attempts < 6 and not win:
        print_hangman(attempts)
        print_info(word, used, unused)
        print(message)
        curr_guess = validated_guess(used)
        unused = unused.replace(curr_guess,'')
        used += curr_guess
        if not curr_guess in word:
            attempts += 1
            message = f'The letter \"{curr_guess}\" is not in the word.'
        else:
            message = f'The letter \"{curr_guess}\" is in the word!'
            win = check_win(word, used)
    return win, attempts

if __name__=="__main__":
    main()
