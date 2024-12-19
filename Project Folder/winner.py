from dealer import four_decks
from manager import Player
import random
import time
from dealer import cards


def clear_screen_and_delay(delay=0):
    time.sleep(delay)
    for i in range(0, 50):
        print("")


def game(player_names):
    players = []
    player_cards = cards()
    for name, card in zip(player_names, player_cards):
        p = Player(name, card)
        p.point = p.get_points()
        p.same_suit = p.max_same_suit()
        p.same_rank = p.max_same_rank()

        players.append(p)

    if len(players) > 1:
        clear_screen_and_delay(4)
        print("Distributing cards...")
        clear_screen_and_delay(2)
        for player in players:
            print(player)
        exchange_card(players)

        print("Updated cards after exchanges:")
        for player in players:
            print(player)
        clear_screen_and_delay(2)
        if determine_loser(players):
            game([player.name for player in players])
        else:
            if not determine_winner(players):
                game([player.name for player in players])

    else:
        print(
            f"\nCongratulations to \033[1m{players[0].name}\033[0m for winning with a score of \033[1m{players[0].point}\033[0m points!\nA well-earned victory\nwell played! 🏆🎉")


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
                print(f"{i + 1}. {player.cards[i]}")
            try:
                card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
                while card_to_exchange_index not in [1, 2, 3, 4, 5]:
                    print("Invalid input! Try again!")
                    card_to_exchange_index = int(input("Which card do you want to change? (1-5): "))
                # returning the card back into deck, so it can be chosen again if needed
                four_decks.append(player.cards[card_to_exchange_index - 1])
                del player.cards[card_to_exchange_index - 1]
                # removing the new random card from the available
                random_card = random.choice(four_decks)
                four_decks.remove(random_card)

                player.cards.append(random_card)
                player.point = player.get_points()
                player.same_suit = player.max_same_suit()
                player.same_rank = player.max_same_rank()
                print("Card exchanged successfully!")
            except ValueError:
                print("Error occurred, invalid input! Cards remain the same.")
        # If input is n, do not change any card
        elif choice == 'n':
            print("Okay, your cards stay the same. Let's move on...")


def determine_loser(players):
    minimum_player = min(players, key=lambda p: p.point)
    min_points_players = [player for player in players if player.point == minimum_player.point]
    if len(min_points_players) == 1:
        print(f"{minimum_player.name} has to leave the game with the lowest points: {minimum_player.point}!\n")
        for card in minimum_player.cards:
            four_decks.append(card)
        players.remove(min_points_players[0])
        return True
    else:
        print("It's tie. Re-dealing the cards...")
        return False


def determine_winner(players):
    # takes player with maximum suits from players with maximum scores
    print("Players got the same scores, let's start comparing suits...")
    maximum_suits = max(players, key=lambda p: p.same_suit)
    max_suits_players = [player for player in players if player.same_suit == maximum_suits.same_suit]
    if len(max_suits_players) == 1:
        print(
            f"\nCongratulations to \033[1m{players[0].name}\033[0m for winning with \033[1m{players[0].same_suit} same suits\033[0m! \nA well-earned victory\nwell played! 🏆🎉")

        return True
    else:
        # takes player with maximum ranks from players with maximum points and maximum ranks
        print("Players got the same suits, let's start comparing ranks...")
        maximum_ranks = max(max_suits_players, key=lambda p: p.same_rank)
        max_ranks_players = [player for player in max_suits_players if player.same_rank == maximum_ranks.same_rank]
        if len(max_ranks_players) == 1:
            print(
                f"\nCongratulations to \033[1m{players[0].name}\033[0m for winning with \033[1m{players[0].same_rank} same ranks\033[0m! \nA well-earned victory\nwell played! 🏆🎉")
            return True
        else:
            print("Players got the same ranks, let's re-deal the cards...")
            return False
