from Deck import Deck

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        
    def fresh_deal(self):
        self.deck.reset_deck()
        for rows in range(7):
            for columns in range(rows,7):
                self.board[columns].append(self.deck.pop())
def main():
    """Set up game steps"""
    x = Solitaire()
    x.fresh_deal()
    print("main")

if __name__=="__main__":
    main()
