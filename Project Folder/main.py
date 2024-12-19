from cards_dealer import names
from winner import game


def main():
    print("Welcome to the cards game! Rules are described in information.md file. Hope you'll enjoy it.")
    player_names = names()

    game(player_names)

    print("\nThe game has ended!")


if __name__ == "__main__":
    main()