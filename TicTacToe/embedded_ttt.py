from ttt import ttt_board

class embedded_ttt_board(ttt_board):
    def __init__(self):
        self.board_state = []
        for i in range(9):
            self.board_state.append(ttt_board())
            self.board_state[i].toggle_clear_scr()

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(f'\
 {self.board_state[i*3].board_state[j*3]}|{self.board_state[i*3].board_state[j*3+1]}|{self.board_state[i*3].board_state[j*3+2]} | \
 {self.board_state[i*3+1].board_state[j*3]}|{self.board_state[i*3+1].board_state[j*3+1]}|{self.board_state[i*3+1].board_state[j*3+2]} | \
 {self.board_state[i*3+1].board_state[j*3]}|{self.board_state[i*3+2].board_state[j*3+1]}|{self.board_state[i*3+2].board_state[j*3+2]}\
                ')
            if i != 2:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
