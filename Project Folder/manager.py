from collections import Counter


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def point(self):
        count = 0
        if self.rank == 'J':
            count = 11
        elif self.rank == 'Q':
            count = 12
        elif self.rank == 'K':
            count = 13
        elif self.rank == 'A':
            count = 20
        elif 2 <= int(self.rank) <= 10:
            count = self.rank

        return count

    def __str__(self):
        return str(self.rank) + self.suit


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.point = self.get_points()
        self.same_suit = self.max_same_suit()
        self.same_rank = self.max_same_rank()

    def get_points(self):
        return sum(card.point() for card in self.cards)

    def max_same_suit(self):
        counter = Counter(card.suit for card in self.cards)
        max_same_suit = max(counter.values())
        return max_same_suit

    def max_same_rank(self):
        counter = Counter(card.rank for card in self.cards)
        max_same_rank = max(counter.values())
        return max_same_rank

    def __str__(self):
        output_string = f"Player \033[1m{self.name}'s\033[0m current cards are: \n"
        for card in self.cards:
            output_string += str(card) + " "
        output_string += "\n"
        return output_string