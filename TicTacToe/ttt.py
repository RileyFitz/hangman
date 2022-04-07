from string import digits
from os import system, name

class ttt_board():
    def __init__(self):
        self.xTurn = True
        self.winner = ""
        self.board_state = [["1","2","3"],["4","5","6"],["7","8","9"]]
        self.clear_scr = True

    def print_board(self):
        '''
        Prints board in interface. Clears screen by default.
        '''
        if self.clear_scr:
            self.clear_screen()
        for i in range(2):
            print(f' {self.board_state[i][0]} | {self.board_state[i][1]} | {self.board_state[i][2]}')
            print(' __|___|__')
        print(f' {self.board_state[2][0]} | {self.board_state[2][1]} | {self.board_state[2][2]}')

    def clear_screen(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear')
        print('\n')

    def toggle_clear_scr(self):
        self.clear_scr = not self.clear_scr

    def check_winner(self):
        '''
        Checks all winning move possiblities, and for stalemate.
        Changes winner accordingly.
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

        # Check stalemate.
        for i in range(len(self.board_state)):
            for j in range(len(self.board_state[i])):
                if not self.board_state[i][j] in digits:
                    return # Skip setting tie as there is a numeral available.
        self.winner = 'T'

    def make_validated_move(self):
        '''
        Retrieves and ensures a valid move in entered by the player.
        Checks for valid numeral, and open space.
        '''
        player = 'X' if self.xTurn else 'O'
        accepted_chars = digits[1:10] # Returns string of digits 1-9.
        while True:
            try:
                print(" Select space: ")
                attempt = input()
                if attempt in accepted_chars and len(attempt) == 1:
                    for i, x in enumerate(self.board_state):
                        if attempt in x:
                            for j in range(len(x)):
                                if x[j] == attempt:
                                    self.board_state[i][j] = player
                                    return # Escape the while loop.

                print(f' The value \'{attempt}\', is not valid. Try {accepted_chars}..')
            except Exception as e:
                print(f' Huh... you were able to get the following error..\n{e}\n')
                print(f' However, this is not valid. Try {accepted_chars}..')

    def initiate_game(self):
        '''
        This starts an entire self hosted game.
        Currently there is no interupt built in.
        This function will progress to a completetion state.
        '''
        while self.winner == "":
            self.print_board()
            self.make_validated_move()
            self.check_winner()
            self.xTurn = not self.xTurn
        self.print_board()
        print('\n 3 in a row!!!')
        print(f' The winner is {self.winner}!')

if __name__=='__main__':
    game = ttt_board()
    game.initiate_game()
