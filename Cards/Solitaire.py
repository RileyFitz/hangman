from Deck import Deck
from string import ascii_uppercase

class Solitaire():
    def __init__(self):
        self.deck = Deck()
        self.board = [[],[],[],[],[],[],[]]
        self.aces = [[],[],[],[]]
        self.win = False
        self.temp_stock = []
        self.stock_flips = 0
        
    def fresh_deal(self):
        self.deck.reset_deck()
        self.deck.shuffle_deck()
        for rows in range(7):
            for columns in range(rows,7):
                self.board[columns].append(self.deck.pop())
        for card in self.deck.deck_list:
            card.revealed = True

    def print_board(self):
        print('BOARD')
        for column in self.board:
            if len(column) > 0:
                column[-1].revealed = True
        print("   1    2    3    4    5    6    7")
        print_board_object = self.generate_print_board_object()
        for j in range(self.find_max_list()):
            row = ascii_uppercase[j] + " "*2
            for i in range(7):
                row += print_board_object[i][j] + " "*2
            print(row)
            row = ""
        print('\n')

    def print_aces(self):
        print("ACES")
        print("Spades(AS)  Hearts(AH)  Dmnds(AD)  Clubs(AC)")
        rtn_str = ""
        for i in range(4):
            if len(self.aces[i])==1:
                rtn_str += self.aces[0][i].short() + " "*6
            else:
                rtn_str += "Empty" + " "*7
        print(rtn_str)
        print('\n')

    def print_stock(self):
        print('STOCK')
        try:
            print(f'Top of Stock: {self.temp_stock[-1]} (ST)')
        except:
            print(f'No stock card is flipped yet, pop one!')
        print(f'There are {len(self.deck.deck_list)} cards left in the stock')
        print(f'You have flipped the stock {self.stock_flips} times')
        print('\n')

    def generate_print_board_object(self):
        print_board = []
        for i in range(7):
            print_board.append([" "*3]*self.find_max_list())
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                char = "" if self.board[i][j].short()[0]=="1" else " "
                print_board[i][j] = self.board[i][j].short() + char
        return print_board

    def find_max_list(self):
        list_len = [len(i) for i in self.board]
        return max(list_len)
    
    def get_valid_user_move(self):
        valid_from = False
        while not valid_from:
            move_from_row, move_from_col = self.get_valid_move_input(True)
            valid_from = self.validate_move_from(move_from_row, move_from_col)
        move_to_row, move_to_col = self.get_valid_move_input(False)
        valid_to = self.validate_move_to(move_to_row, move_to_col, move_from_row, move_from_col) 
        if not valid_to:
            print('The move FROM: '
                f'{self.get_card(True, move_from_row, move_from_col)} '
                f' and  TO: {self.get_card(False, move_to_row, move_to_col)} '
                'is not valid. Try again')
            return
        # Move cards and any that may lie below, AKA moving stacks.

    def validate_move_to(self, trow, tcol, frow, fcol):
        from_card = self.get_card(True, frow, fcol)
        to_card = self.get_card(False, trow, tcol)
        if (to_card == []): # If empty Ace 
            if (from_card.value == "Ace"):
                return True
            else:
                return False

        # Not same card
        if (from_card != to_card): 
            # Colors are different
            if (from_card.color != to_card.color): 
                # to card is top of stack
                if (self.board[trow][-1] == to_card): 
                    # From is one less than To
                    if (self.get_card_number(to_card)-1 == self.get_card_number(from_card)):
                        return True
        return False

    def get_card_number(self, card):
        card_vals = {"Ace": 1, "Jack": 11, "Queen": 12, "King":13}
        try:
            return int(card.value)
        except:
            return card_vals[card.value]

    def get_card(self, isFrom, row, col):
        if (row == -1):
            if (isFrom):
                return self.temp_stock[-1]
            else: 
                return self.aces[-col -1]
        return self.board[row][col]

    def validate_move_from(self, row, col):
        # If stock card choosen
        if (row == -1):
            try:
                if (self.temp_stock[-1]):
                    return True
            except:
                self.pop_stock()
                self.display_board()
                print("Stock was popped for you, try again.")
                return False
        
        # Check if card exists, and is revealed.
        try:
            # If spot has revealed attribute, it exists.
            if (self.board[col][row].revealed):
                return True
            print("This card has not been revealed yet. Try again.")
            return False
        except:
            print("This position does not contain a card. Try again.")
            return False
    
    def get_valid_move_input(self, isFrom):
        input_text = "Select a card to move "
        if (isFrom):
            input_text += "FROM: "
        else:
            input_text += "TO: "
        
        while True:
            user_input = input(input_text)
            # From moves include Stock
            if (isFrom):
                if (user_input.upper() == "ST"):
                    return -1, 0
            # To moves include Aces
            if (not isFrom and user_input[0].upper() == "A" and user_input.isalpha()):
                aces_dict = {"S":-1, "H":-2, "D":-3, "C":-4}
                return -1, aces_dict[user_input[1].upper()]

            if len(user_input) == 2 and user_input[0].isalpha() and user_input[1].isdigit():
                return int(ord(user_input[0]) - ord('a')), int(user_input[1])-1
            else:
                print("Invalid input. Please try again.")
    
    def user_action(self):
        print("Please choose to pop the stock(1) or make a move(2)")
        action = self.get_user_action()
        if (action == "1"):
            self.pop_stock()
        else:
            self.get_valid_user_move()

    def pop_stock(self):
        if (len(self.deck.deck_list) > 0):
            self.temp_stock.append(self.deck.pop())
        else:
            self.stock_flips += 1
            self.temp_stock.reverse()
            self.deck.deck_list = self.temp_stock
            self.temp_stock = []

    def get_user_action(self):
        while True:
            user_input = input("Enter 1(pop) or 2(move): ")

            if user_input == "1" or user_input == "2":
                return user_input
            else:
                print("Invalid input. Please enter 1 or 2.")

    def display_board(self):
        self.print_board()
        self.print_aces()
        self.print_stock()

def main():
    """Set up game steps"""
    game = Solitaire()
    game.fresh_deal()
    #while not game.win:
    game.display_board()
    # Decide pop or move
    game.user_action()
    # Check win

if __name__=="__main__":
    main()
