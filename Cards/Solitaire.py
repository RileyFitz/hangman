from Deck import Deck
from string import ascii_uppercase

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        self.win = False
        
    def fresh_deal(self):
        self.deck.reset_deck()
        for rows in range(7):
            for columns in range(rows,7):
                self.board[columns].append(self.deck.pop())

    def print_board(self):
        print("   1    2    3    4    5    6    7")
        print_board_object = self.gather_print_board_object()
        for j in range(self.find_max_list()):
            row = ascii_uppercase[j] + "  "
            for i in range(7):
                row += print_board_object[i][j] + "  "
            print(row)
            row = ""

    def gather_print_board_object(self):
        print_board = []
        for i in range(7):
            print_board.append(["   "]*self.find_max_list())
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                char = "" if self.board[i][j].short()[0]=="1" else " "
                print_board[i][j] = self.board[i][j].short() + char
        return print_board

    def find_max_list(self):
        list_len = [len(i) for i in self.board]
        return max(list_len)

def main():
    """Set up game steps"""
    game = Solitaire()
    game.fresh_deal()
    #while not game.win:
    ##print_board
    ##get and validate user input
    ##validate and users move
    ##check win
    print("main")

if __name__=="__main__":
    main()
