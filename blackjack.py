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
        random.shuffle(deck)
        return deck
    
    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())
    
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