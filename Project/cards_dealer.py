import random
from manager import Card

_SUITS_ = ['Spade', 'Heart', 'Diamond', 'Club']
_RANKS_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
_FOUR_DECKS_ = [Card(suit, rank) for suit in _SUITS_ for rank in _RANKS_]*4


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
    all_cards = []
    for i in range(3):
        player_cards = []
        for _ in range(5):
            card = random.choice(_FOUR_DECKS_)
            player_cards.append(card)
        all_cards.append(player_cards)
    
    return all_cards

def points(cards):
    return sum(card.point() for card in cards)