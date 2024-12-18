from collections import Counter

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def point(self):
        if self.rank == 'J':
            count = 11
        elif self.rank == 'Q':
            count = 12
        elif self.rank == 'K':
            count = 13
        elif self.rank == 'A':
            count = 20
        elif int(self.rank) >= 2 and int(self.rank) <= 10:
            count = self.rank
            
        return count
    
    def __str__(self):
        return str(self.rank) + ' of ' + self.suit

    def __repr__(self):
        return self.__str__()
    

class Player():
    def __init__(self, name, cards, point):
        self.name = name
        self.cards = cards
        self.point = point
        self.same_suit = self.max_same_suit()
        self.same_rank = self.max_same_rank()

    def max_same_suit(self):
        counter = Counter(card.suit for card in self.cards)
        max_same_suit = max(counter.values())
        return max_same_suit

    def max_same_rank(self):
        counter = Counter(card.rank for card in self.cards)
        max_same_rank = max(counter.values())
        return max_same_rank

    def __str__(self):
        return f"Name: {self.name}\nCards: {str(self.cards)}\nPoints: {self.point}\n"

    def __repr__(self):
        return self.__str__()