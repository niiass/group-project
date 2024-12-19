import random
from manager import Card

_SUITS_ = ['♠️', '♥️', '♦️', '♣️']
_RANKS_ = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
four_decks = [Card(suit, rank) for suit in _SUITS_ for rank in _RANKS_] * 4

def names():
    print("Enter players names!")
    names_array = []
    for i in range(3):
        name = input(f"Player {i + 1}: ")
        while name in names_array:
            print("Player with such name already exists! Try again!")
            name = input(f"Player {i + 1}: ")

        names_array.append(name)

    return names_array


def cards():
    all_cards = []
    for i in range(3):
        player_cards = []
        for _ in range(5):
            card = random.choice(four_decks)
            four_decks.remove(card)
            player_cards.append(card)

        all_cards.append(player_cards)

    return all_cards


def points(cards_array):
    return sum(card.point() for card in cards_array)