from cards_dealer import names, cards, points
from card import Player
from winner import is_winner

def main():
    print("Welcome to the cards game! Rules are described in Rules.md file. Hope you'll enjoy it.")
    player_names = names()
    player_cards = cards()
    players = []

    for name, card in zip(player_names, player_cards):
        point = points(card)
        p = Player(name, card, point)
        players.append(p)
    
    print(players)
    print(f"Max point {is_winner(players)}")

if __name__ == "__main__":
    main()