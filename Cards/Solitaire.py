import random
import os
from subprocess import call

def clear_screen():
    # Windows
    if os.name == "nt":
        _ = call("cls", shell=True)
    # Mac and Unix/Linux
    else:
        _ = call("clear")

# Card class represents a single playing card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = False

    def __repr__(self):
        return f"{self.rank}{self.suit}"


# Deck class represents a deck of playing cards
class Deck:
    def __init__(self):
        ranks = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]
        suits = ["♠", "♣", "♥", "♦"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0


# SolitaireGame class represents the game and its logic
class SolitaireGame:
    def __init__(self):
        self.deck = Deck()
        self.stock = []
        self.waste = []
        self.foundations = [[] for _ in range(4)]
        self.tableau = [[] for _ in range(7)]

    def deal_initial_cards(self):
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.deal()
                if j == i:
                    card.face_up = True
                self.tableau[i].append(card)

        while not self.deck.is_empty():
            self.stock.append(self.deck.deal())

    def display_game(self):
        clear_screen()
        print("Stock: {} cards".format(len(self.stock)))
        print("Waste: {}".format(self.waste[-1] if self.waste else "Empty"))

        print("\nFoundations:")
        for i, foundation in enumerate(self.foundations):
            print("Foundation {}: {}".format(i + 1, foundation[-1] if foundation else "Empty"))

        print("\nTableau:")
        max_pile_size = max(len(pile) for pile in self.tableau)
        for row in range(max_pile_size):
            pile_row = []
            for pile in self.tableau:
                if row < len(pile):
                    card = pile[row]
                    pile_row.append(str(card) if card.face_up else "X")
                else:
                    pile_row.append(" ")
            print("  ".join(pile_row))

    def play(self):
        self.deal_initial_cards()

        while True:
            self.display_game()

            move = input("Enter a move (e.g., 'stock', 'waste', 'tableau 1', 'foundation 1'): ")
            move = move.lower().split()

            if move[0] == "stock":
                if self.stock:
                    card = self.stock.pop()
                    card.face_up = True
                    self.waste.append(card)
                else:
                    print("Stock is empty.")
            elif move[0] == "waste":
                if self.waste:
                    card = self.waste.pop()
                    card.face_up = True
                    self.stock.append(card)
                else:
                    print("Waste is empty.")
            elif move[0] == "tableau":
                pile_idx = int(move[1]) - 1
                if pile_idx >= 0 and pile_idx < 7:
                    if self.tableau[pile_idx]:
                        card = self.tableau[pile_idx][-1]
                        if card.face_up:
                            self.waste.append(self.tableau[pile_idx].pop())
                        else:
                            card.face_up = True
                    else:
                        print("Tableau pile is empty.")
                else:
                    print("Invalid tableau pile.")
            elif move[0] == "foundation":
                foundation_idx = int(move[1]) - 1
                if foundation_idx >= 0 and foundation_idx < 4:
                    if self.waste:
                        card = self.waste[-1]
                        if card.rank == "A":
                            if not self.foundations[foundation_idx]:
                                self.foundations[foundation_idx].append(self.waste.pop())
                            else:
                                print("Invalid move. Foundation already has a card.")
                        else:
                            if self.foundations[foundation_idx]:
                                last_card = self.foundations[foundation_idx][-1]
                                if card.suit == last_card.suit and card.rank == str(int(last_card.rank) + 1):
                                    self.foundations[foundation_idx].append(self.waste.pop())
                                else:
                                    print("Invalid move. Card doesn't follow the foundation's sequence.")
                            else:
                                print("Invalid move. Foundation requires an 'A' card to start.")
                    else:
                        print("Waste is empty.")
                else:
                    print("Invalid foundation pile.")
            elif move[0] == "quit":
                break
            else:
                print("Invalid move.")

            print()

            if self.is_game_won():
                print("Congratulations! You have won the game!")
                break

    def is_game_won(self):
        return all(len(foundation) == 13 for foundation in self.foundations)


# Start the game
game = SolitaireGame()
game.play()

