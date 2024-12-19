from cards_dealer import _FOUR_DECKS_
from manager import Player, Card
import random

def game(player_names, player_cards):
    players = []
    for name, card in zip(player_names, player_cards):
        p = Player(name, card)
        p.point = p.get_points()
        p.same_suit = p.max_same_suit()
        p.same_rank = p.max_same_rank()
        
        players.append(p)

    if len(players) > 1:
        for player in players:
            print(player)

        exchange_card(players)
        
        print("Updated cards after exchanges:")
        for player in players:
            print(player)
        
        if determine_loser(players):
            game([player.name for player in players], [player.cards for player in players])
        else:
            if not determine_winner(players):
                game([player.name for player in players], [player.cards for player in players])

    else:
        print(f"Congratulations! Winner is {players[0].name}!")


def exchange_card(players):
    for player in players:
        choice = input(f"Does {player.name} want to exchange one card? (y/n): ")
        # Make sure that input is y or n
        while choice != 'n' and choice != 'y':
            print("Invalid input! Try again!")
            choice = input(f"Does {player.name} want to exchange one card? (y/n): ")
        # If choice is y, let player exchange one card
        if choice == 'y':
            print("Your cards are:")
            for i in range(len(player.cards)):
                print(f"{i+1}. {player.cards[i]}")
            try:
                card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
                while card_to_exchange_index not in [1, 2, 3, 4, 5]:
                    print("Invalid input! Try again!")
                    card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
                
                del player.cards[card_to_exchange_index-1]
                player.cards.append(random.choice(_FOUR_DECKS_))
                player.point = player.get_points()
                player.same_suit = player.max_same_suit()
                player.same_rank = player.max_same_rank()
                print("Card exchanged successfully!")
            except ValueError:
                print("Error occured, invalid input! Cards remain the same.")
        # If input is n, do not change any card
        elif choice == 'n':
            print("Okay, your cards stay the same. Let's move on...")


def determine_loser(players):
    minimum_player = min(players, key=lambda p: p.point)
    min_points_players = [player for player in players if player.point == minimum_player.point]
    if len(min_points_players) == 1:
        print(f"{minimum_player.name} has to leave the game with the lowest points: {minimum_player.point}!\n")
        players.remove(min_points_players[0])
        return True
    else:
        print("It's tie. Readealing the cards...")
        return False

def determine_winner(players):
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
                print("Players got the same ranks, let's redeal the cards...")
                return False
            