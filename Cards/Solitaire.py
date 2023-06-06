from Deck import Deck

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
        print_board = []
        for i in range(7):
            print_board.append(["  "]*self.find_max_list())
            #shouldnt be 13, should be longest list in board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print_board[i][j] = self.board[i][j]
        print(print_board)

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
