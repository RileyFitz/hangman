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
        '''
        Uh oh, i don't think the previous print board functions will work.
        They make new lines with each pass, and this board shouldnt have any..
            This would need to print out one entire line at a time...
            1|2|3 | 1|2|3 | 1|2|3 -- print entire line
            4|5|6 | 4|5|6 | 4|5|6
            7|8|9 | 7|8|9 | 7|8|9
            ______________________

            I think to "fix" this I will need to create a new function to print
                game boards line by line. May need to provide a line number
                of which to print..
                def print_board_line(self, line)
        '''
        #if self.clear_scr:
        #    self.clear_screen()

        #print(self.board_state[0][0].board_state)
        for i in range(3):
            self.print_board_line(i)
            print('________________________________')
            print('________________________________')

    def print_board_line(self, line):
        for i in range(3):
            # this needs to be a single line printed. But spacing errors may occur.
            print(f'\
 {self.board_state[line][0].board_state[i][0]}\
 |\
{self.board_state[line][0].board_state[i][1]}\
 |\
{self.board_state[line][0].board_state[i][2]}\
 ||\
 {self.board_state[line][1].board_state[i][0]}\
 |\
{self.board_state[line][1].board_state[i][1]}\
 |\
{self.board_state[line][1].board_state[i][2]}\
 ||\
 {self.board_state[line][2].board_state[i][0]}\
 |\
{self.board_state[line][2].board_state[i][1]}\
 |\
{self.board_state[line][2].board_state[i][2]}\
            ')
