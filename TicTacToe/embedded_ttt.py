from ttt import ttt_board
from string import digits

class embedded_ttt_board(ttt_board):
    def __init__(self):
        super().__init__()
        self.board_state = []
        for i in range(9):
            self.board_state.append(ttt_board())

    def print_board(self):
        self.clear_screen()
        for i in range(3):
            for j in range(3):
                print(f'\
 {self.board_state[i*3].board_state[j*3]}|{self.board_state[i*3].board_state[j*3+1]}|{self.board_state[i*3].board_state[j*3+2]} | \
 {self.board_state[i*3+1].board_state[j*3]}|{self.board_state[i*3+1].board_state[j*3+1]}|{self.board_state[i*3+1].board_state[j*3+2]} | \
 {self.board_state[i*3+2].board_state[j*3]}|{self.board_state[i*3+2].board_state[j*3+1]}|{self.board_state[i*3+2].board_state[j*3+2]}')
            if i != 2:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'It is {"X" if self.xTurn else "O"}\'s turn!')
        
    def get_validated_board(self):
        '''
        Returns an int representing a valid board without a winner.
        '''
        print('Please select a board to make a move on..')
        board = self.get_validated_move()
        if self.board_state[board].winner != "":
            print(f'This board has been won by {self.board_state[board].winner}\nTry a different board')
            board =  self.get_validated_board()
        return int(board)

    def check_winner(self):
        '''
        Checks all winning move possiblities, and for stalemate.
        Changes winner accordingly.
        '''
        player = 'X' if self.xTurn else 'O'
        for i in range(3):
            # Row check.
            if self.board_state[i*3].winner == self.board_state[i*3+1].winner == self.board_state[i*3+2].winner == player:
                self.winner = player
            # Column check.
            if self.board_state[i].winner == self.board_state[i+3].winner == self.board_state[i+6].winner == player:
                self.winner = player

        # Diagonals.
        if self.board_state[0].winner == self.board_state[4].winner == self.board_state[8].winner == player:
            self.winner = player
        if self.board_state[2].winner == self.board_state[4].winner == self.board_state[6].winner == player:
            self.winner = player

        # Check stalemate.
        for i, x in enumerate(self.board_state):
            if x.winner == '':
                return # Skip bc there are open spots.
        self.winner = 'T'

    def initiate_game(self):
        while self.winner == '':
            # print_board
            self.print_board()
            # get emb_board input
            board = self.get_validated_board()
            # Make move on validated board.
            move = self.board_state[board].get_validated_move()
            self.board_state[board].board_state[move] = 'X' if self.xTurn else 'O'
            # Change player on selected board, necessary for the winner check.
            self.board_state[board].xTurn = True if self.xTurn else False
            #Check winner on said board
            self.board_state[board].check_winner()
            # Check emb_ttt winner
            self.check_winner()
            # Change player
            self.xTurn = not self.xTurn
        print('\n 3 boards in a row!!!')
        print(f' The winner is {self.winner}!')

if __name__=='__main__':
    game = embedded_ttt_board()
    game.initiate_game()
