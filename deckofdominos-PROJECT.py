from random import shuffle


class Card:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __repr__(self):
        return f"{self.side1} | {self.side2}"


class Deck:
    def __init__(self):
        sides1 = list(range(0, 9))
        sides2 = list(range(0, 9))
        self.cards = [Card(side1, side2) for side1 in sides1 for side2 in sides2]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        realnum = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt with")
        cards = self.cards[-realnum:]
        self.cards = self.cards[:-realnum]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand):
        return self._deal(hand)

    def shuffle(self):
        if self.count() < 81:
            raise ValueError("You need a full deck to shuffle")
        shuffle(self.cards)
        return self


domino = Deck()
domino.shuffle()
print(domino)
# print(domino.cards)
man1 = domino.deal_hand(5)
print(man1)
man12 = domino.deal_card()
print(man12)
