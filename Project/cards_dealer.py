import random
from card import Card

_SUITS_ = ['Spade', 'Heart', 'Diamond', 'Club', 'Spade', 'Heart', 'Diamond', 'Club', 'Spade', 'Heart', 'Diamond', 'Club', 'Spade', 'Heart', 'Diamond', 'Club']
_RANKS_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

def names():
    print("Enter players names!")
    names = []
    for i in range(3):
        name = input(f"Player {i+1}: ")
        while name in names:
            print("Player with such name already exists! Try again!")
            name = input(f"Player {i+1}: ")

        names.append(name)
    
    return names

def cards():
    cards = []
    for i in range(3):
        card = []
        for _ in range(5):
            p = Card(random.choice(_SUITS_), random.choice(_RANKS_))
            card.append(p)
        cards.append(card)
    
    return cards

def points(cards):
    counter = 0
    for card in cards:
        counter += card.point()

    return counter