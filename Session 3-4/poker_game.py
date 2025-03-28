from deck import Deck, Card
from collections import Counter

class PokerHand:
    def __init__(self, deck):
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def get_matching_suit_cards(self):
        suits = [card.suit for card in self.cards]
        suit_counts = Counter(suits)

        # Find the suit that appears at least 4 times
        for suit, count in suit_counts.items():
            if count >= 4:
                # Return only the cards with that suit
                return [card for card in self.cards if card.suit == suit]
        return None

# Simulation
count = 0
matches = 0

while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    matching_cards = hand.get_matching_suit_cards

    if matching_cards:
        matches += 1
        print(f"Match #{matches} (Hand #{count + 1}): {matching_cards}")

    count += 1

print(f"\nIt took {count} hands to find 1000 hands with 4 or more cards of the same suit.")
