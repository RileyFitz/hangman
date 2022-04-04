from string import digits
from os import system, name

class ttt_board():
    def __init__(self):
        self.xTurn = True
        self.winner = ""
        self.board_state = [[1,2,3],[4,5,6],[7,8,9]]

    def print_board(self, clear_scr=True):
        '''
        Prints board in interface. clears screan by default.
        '''
        if clear_scr:
            self.clear_screen()
        for i in range(2):
            print(f'{self.board_state[i][0]} | {self.board_state[i][1]} | {self.board_state[i][2]}')
            print('__|___|__')
        print(f'{self.board_state[2][0]} | {self.board_state[2][1]} | {self.board_state[2][2]}')

    def clear_screen(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def check_winner(self):
        '''
        Need to add ability to set winner to TIE!!
        Currently bugged, takes a full round to commence,
            to validate winner and end game.
            - Actually takes 2 rounds to complete now...
        '''
        player = 'X' if self.xTurn else 'O'
        for i in range(3):
            # Row check.
            if self.board_state[i][0] == self.board_state[i][1] == self.board_state[i][2] == player:
                self.winner = player
            # Column check.
            if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] == player:
                self.winner = player

        # Diagonals.
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] == player:
            self.winner = player
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] == player:
            self.winner = player

        # Check stalemate
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i]))
                if self.board_state[i][j] in digits:
                    self.winner = 'T'

    def initiate_game(self):
        '''

        This starts an entire self hosted game.
        Currently there is no interupt built in.
        This function will progress to a completetion state.

        '''
        while self.winner == "":
            self.print_board()
            self.check_winner()
            self.make_validated_move()
        print(f'The winner is {self.winner}!')

    def make_validated_move(self):
        '''
        something about this function
        '''
        player = 'X' if self.xTurn else 'O'
        accepted_chars = digits[1:10] # Returns string of digits 1-9.
        while True:
            try:
                print("Select space: ")
                attempt = input()
                if attempt in accepted_chars and len(attempt) == 1:
                    for i, x in enumerate(self.board_state):
                        if int(attempt) in x:
                            for j in range(len(x)):
                                if x[j] == int(attempt):
                                    self.board_state[i][j] = player
                                    self.xTurn = not self.xTurn # This may need to be executed elsewhere.
                                    return # Escape the while loop.

                print(f'The value \'{attempt}\', is not valid. Try {accepted_chars}..')
            except Exception as e:
                print(f'Huh... you were able to get the following error..\n{e}\n')
                print(f'However, this is not valid. Try {accepted_chars}..')

game = ttt_board()
game.initiate_game()
