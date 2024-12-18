from cards_dealer import names, cards
from winner import game

def main():
    print("Welcome to the cards game! Rules are described in Rules.md file. Hope you'll enjoy it.")
    player_names = names()
    player_cards = cards()

    game(player_names, player_cards)
    
    print("The game has ended!")

if __name__ == "__main__":
    main()