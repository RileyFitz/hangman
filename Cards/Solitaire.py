from Deck import Deck

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        
        def serve_fresh_deal():
            self.deck.reset_deck()
            for rows in range(7):
                for columns in range(rows,7):
                    self.board[columns].append(self.deck.pop())

