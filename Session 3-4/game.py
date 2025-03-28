from deck import Deck, Card


class Hand:
    def __init__(self):
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        return self._hand

    def __str__(self):
        return str(self.hand)

    @property
    def is_flush(self):
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True


# deck = Deck()
# deck.shuffle()
# h = Hand()
# print(h)

while True:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    if h.is_flush:
        print(h)
        break