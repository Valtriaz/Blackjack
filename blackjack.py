import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False
    
    def create_deck(self):
        deck = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 11):
                deck.append((value, suit))
            for face_card in ['Jack', 'Queen', 'King', 'Ace']:
                deck.append((face_card, suit))
            for face_card in ['Ace']:
                deck.append((ace, suit))
        random.shuffle(deck)
        return deck
    
    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())
    
    def calculate_hand_value(self, hand):
        total = 0
        num_aces = 0
        for card in hand:
            if isinstance(card[0], int):
                total += card[0]
            elif card[0] in ['Jack', 'Queen', 'King']:
                total += 10
            elif card[0] == 'Ace':
                num_aces += 1
                total += 11
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total
    
    def print_hands(self, reveal_dealer=False):
        print("\nPlayer's Hand:", ", ".join([f"{card[0]} of {card[1]}" for card in self.player_hand]))
        print("Player's Score:", self.player_score)
        
        if reveal_dealer:
            print("\nDealer's Hand:", ", ".join([f"{card[0]} of {card[1]}" for card in self.dealer_hand]))
            print("Dealer's Score:", self.dealer_score)
        else:
            print("\nDealer's Hand:", f"{self.dealer_hand[0][0]} of {self.dealer_hand[0][1]}, Hidden")
    
    def player_turn(self):
        while not self.game_over:
            self.print_hands()
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player_hand.append(self.deck.pop())
                self.player_score = self.calculate_hand_value(self.player_hand)
                if self.player_score > 21:
                    print("\nPlayer busts! Dealer wins.")
                    self.game_over = True
            elif action == 's':
                break
            else:
                print("Invalid input! Please enter 'h' or 's'.")
    
    def dealer_turn(self):
        while self.dealer_score < 16 and not self.game_over:
            self.dealer_hand.append(self.deck.pop())
            self.dealer_score = self.calculate_hand_value(self.dealer_hand)
        
        self.print_hands(reveal_dealer=True)
        
        if self.dealer_score > 21:
            print("\nDealer busts! Player wins.")
        elif self.dealer_score > self.player_score:
            print("\nDealer wins.")
        elif self.dealer_score < self.player_score:
            print("\nPlayer wins!")
        else:
            print("\nIt's a tie!")
        
        self.game_over = True
    
    def play_game(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()
        self.player_score = self.calculate_hand_value(self.player_hand)
        self.dealer_score = self.calculate_hand_value(self.dealer_hand)
        
        self.print_hands()
        self.player_turn()
        
        if not self.game_over:
            self.dealer_turn()

if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
