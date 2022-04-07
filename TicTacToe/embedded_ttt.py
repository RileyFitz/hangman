from ttt import ttt_board

class embedded_ttt_board(ttt_board):
    def __init__(self):
        board_state = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append(ttt_board())
                temp[j].toggle_clear_scr()
            board_state.append(temp)
        self.board_state = board_state

    def print_board(self):
        pass
