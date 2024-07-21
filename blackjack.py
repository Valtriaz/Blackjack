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