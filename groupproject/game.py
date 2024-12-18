# from idlelib.grep import walk_error
from random import randint
from player import *
import database

# TODO final: 1. make output better,
# TODO        2. add full winning condition (outside of points)
# TODO        3. put repeated code into functions
# TODO        4. error handling
# TODO : presentation
# TODO : MD file

# presentation - together
# md file - beso
# code lika : 1, 4
# code nia : 2, 3

class Game(object):
    COLORS = database.COLORS
    VALUES = database.VALUES
    POINTS = database.POINTS

    def __init__(self):
        self.used_cards = {}
        self.players = []

    def add_player(self, player: "Player"):
        if len(self.players) >= 3:
        print("The game has reached its maximum capacity of 3 players. Please wait for the next game.")
    else:
        self.players.append(player)
        print(f"Player '{player.name}' has been successfully added to the game.")

    # -TODO- color/value generate straight from the list
    def generate_card_code(self):
        while True:
            color = randint(1, 4)
            value = randint(2, 14)
            code = str(color) + str(value)
            if self.used_cards.get(code):
                if self.used_cards[code] < 4:
                    self.used_cards[code] += 1
                    return code
            else:
                self.used_cards[code] = 1
                return code

    def add_card_back(self, card):
        self.used_cards[card] -= 1

    def card_decode(self, card_code):
        color = card_code[0]
        value = card_code[1:]
        return f"{self.VALUES[value]}{self.COLORS[color]}"

    def card_point(self, card_code):
        return self.POINTS[card_code[1:]]


def grand_game_loop():
    weird_poker = Game()
    # game creation
    print("Welcome to Weird Poker! Let the fun begin.")
    # adding players to the game
    for i in range(1, 4):
        name = input(f"Player {i}, please enter your name: ")
        player_i = Player(name, weird_poker)
        weird_poker.add_player(player_i)
    while len(weird_poker.players) > 1:
        game_loop(weird_poker)

# -TODO- add function that determines the winner if the points are equal but the number of things aren't
def find_loser(weird_poker):
    min_points = 10000
    min_player = None

    for player in weird_poker.players:
        if player.points < min_points:
            min_points = player.points
            min_player = player

    for player in weird_poker.players:
        if player.points == min_points and player is not min_player:
            print("Points are equal, dealing again.")
            return None
    return min_player

# -TODO- make better output
def game_loop(weird_poker):
    for player in weird_poker.players:
        player.add_cards()
        print(f"{player.name}'s cards have been dealt:")
        player.print_cards()
        player.count_points()
        print()

    # change card
    change_card = False
    for player in weird_poker.players:
        user_answer = input(f"{player.name}, would you like to change any of your cards? (y/n): ").strip().lower()
        if user_answer == "y":
            index = int(input("Enter the index of the card you want to change (starting from 0): "))
            player.change_card(index)
            print("Your card has been successfully changed.")
            change_card = True
            player.count_points()

    if change_card:
        for player in weird_poker.players:
            print(f"{player.name}'s updated cards are:")
            player.print_cards()
            print()

    # -TODO- implement winner logic
    # see the looser
    min_player = find_loser(weird_poker)
    if min_player is None:
        return

    print(f"{min_player.name} has {min_player.points} points and has been eliminated from the game.")
    weird_poker.players.remove(min_player)

    if len(weird_poker.players) == 1:
        print(f"Congratulations {weird_poker.players[0].name}! You have won the game with {weird_poker.players[0].points} points.")
        return

    min_player = find_loser(weird_poker)
    if min_player is None:
        return
    print(f"{min_player.name} has {min_player.points} points and has been eliminated from the game.")
    weird_poker.players.remove(min_player)

    print(f"Congratulations {weird_poker.players[0].name}! You have won the game with {weird_poker.players[0].points} points.")

def main():
    grand_game_loop()

if __name__ == "__main__":
    main()
