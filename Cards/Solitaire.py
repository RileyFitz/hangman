from Deck import Deck

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        for i in range(7):
            for j in range(i,7):
                self.board[j].append(self.deck.pop())

