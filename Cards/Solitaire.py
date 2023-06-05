from Deck import Deck

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        self.win = false
        
    def fresh_deal(self):
        self.deck.reset_deck()
        for rows in range(7):
            for columns in range(rows,7):
                self.board[columns].append(self.deck.pop())
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
