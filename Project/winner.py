from cards_dealer import _FOUR_DECKS_, cards, points
from manager import Player
import random

def game(player_names, player_cards):
    players = []

    for name, card in zip(player_names, player_cards):
        point = points(card)
        p = Player(name, card, point)
        players.append(p)

    while len(players) > 1:
        for player in players:
            print(player)

        if is_winner(players):
            return False
    
        if is_tie(players):
            player_cards = cards()
            game([player.name for player in players], player_cards)
        else:
            game([player.name for player in players], [player.card for player in players])


def is_winner(players):
    # takes player with maximum points from all three players
    maximum_player = max(players, key=lambda p: p.point)
    max_points_players = [player for player in players if player.point == maximum_player.point]
    if len(max_points_players) == 1:
        print(f"The winner is {maximum_player.name} with {maximum_player.point} points!")
        return True
    else:
        # takes player with maximum suits from players with maximum scores
        print("Players got the same scores, let's start comparing suits...")
        maximum_suits = max(max_points_players, key=lambda p: p.same_suit)
        max_suits_players = [player for player in max_points_players if player.same_suit == maximum_suits.same_suit]
        if len(max_suits_players) == 1:
            print(f"The winner is {maximum_suits.name} with {maximum_suits.same_suit} same suits!")
            return True
        else:
            #takes player with maximum ranks from players with maximum points and maximum ranks
            print("Players got the same suits, let's start comparing ranks...")
            maximum_ranks = max(max_suits_players, key=lambda p: p.same_rank)
            max_ranks_players = [player for player in max_suits_players if player.same_rank == maximum_ranks.same_rank]
            if len(max_ranks_players) == 1:
                print(f"The winner is {maximum_ranks.name} with {maximum_ranks.same_rank} same ranks!")
                return True
            else:
                print("Players got the same ranks, let's get to another level...")
                return False
            
def is_tie(players):
    print("Here are your cards:")
    for player in players:
        print(f"{player.name} has: {player.cards}")

    no_exchange = True

    # Asks wether first player wants to change card or not
    choice_first = input(f"Does {players[0].name} want to exchange one card? (y/n): ")
    while choice_first != 'n' and choice_first != 'y':
        print("Invalid input! Try again!")
        choice_first = input(f"Does {players[0].name} want to exchange one card? (y/n): ")

    if choice_first == 'y':
        no_exchange = False
        exchange_card(players, 0)
    else:
        print("Okay, your cards stay the same. Let's move on...")

    # Asks wether second player wants to change card or not
    choice_second = input(f"Does {players[1].name} want to exchange one card? (y/n): ")
    while choice_second != 'n' and choice_second != 'y':
        print("Invalid input! Try again!")
        choice_second = input(f"Does {players[1].name} want to exchange one card? (y/n): ")

    if choice_second == 'y':
        no_exchange = False
        exchange_card(players, 1)
    else:
        print("Okay, your cards stay the same. Let's move on...")

    # Asks wether third player wants to change card or not
    choice_third = input(f"Does {players[2].name} want to exchange one card? (y/n): ")
    while choice_third != 'n' and choice_third != 'y':
        print("Invalid input! Try again!")
        choice_third = input(f"Does {players[2].name} want to exchange one card? (y/n): ")

    if choice_third == 'y':
        no_exchange = False
        exchange_card(players, 2)
    else:
        print("Okay, your cards stay the same. Let's move on...")

    # If no exchanges occurred, restart the game. Players remain the same
    if no_exchange:
        print("Okay, let's redeal the cards.")
        return True
    
    determine_loser(players)
    return False

def exchange_card(players, index):
    print("Your cards are:")
    for i in range(len(players[index].cards)):
        print(f"{i+1}. {players[index].cards[i]}")
    
    card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
    while card_to_exchange_index not in [1, 2, 3, 4, 5]:
        print("Invalid input! Try again!")
        card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
    
    del players[index].cards[card_to_exchange_index-1]
    
    players[index].cards.append(random.choice(_FOUR_DECKS_))
    print("Card exchanged successfully!")

def determine_loser(players):
    if len(players) == 1:
        return players[0]
    
    minimum_player = min(players, key=lambda p: p.point)
    min_points_players = [player for player in players if player.point == minimum_player.point]
    if len(min_points_players) == 1:
        print(f"The winner is {minimum_player.name} with {minimum_player.point} points!")
        players.remove(min_points_players[0])
    else:
        print("It's tie. Readealing the cards...")
    