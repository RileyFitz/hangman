

class ttt_board():
    def __init__(self):
        self.xTurn = True
        self.winner = ""
        self.board_state = [ [' '] * 3 for _ in range(3)]

    def print_board(self):
        print('printing board')

    def check_winner(self):
        player = 'X' if self.xTurn else 'O'

        for i in range(3):
            # Row check.
            if self.board_state[i][0] == self.board_state[i][1] == self.board_state[i][2] == player:
                return True
            # Column check.
            if self.board_state[0][i] == self.board_state[1][i] == self.board_state[2][i] == player:
                return True

        # Diagonals.
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] == player:
            return True
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] == player:
            return True

        return False # True false logic may not suffice here. Check back

    def make_move(self):
        pass

game = ttt_board()
game.print_board()
