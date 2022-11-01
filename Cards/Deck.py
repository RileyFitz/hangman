from random import shuffle

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        print(f'{self.value} of {self.suit}')

    def return_vals(self):
        return value, suit
        
class Deck():
    def __init__(self):
        self.deck_list = self.generate_deck()

    def generate_deck(self):
        suits = ['spades', 'clubs', 'diamonds', 'hearts']
        values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        deck = []
        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return deck
        
    def shuffle_deck(self):
        return shuffle(self.deck_list)

    def list_deck(self, num=1):
        if num=='all' or (num > len(self.deck_list)):
            num = len(self.deck_list)
        if not isinstance(num, int):
            print(f'{num} is not valid number for listing the cards')
        
        for i in range(num):
            self.deck_list[i].print_card()

    def reset_deck(self):
        self.deck_list = self.generate_deck()

    def pop(self):
        return self.deck_list.pop()
