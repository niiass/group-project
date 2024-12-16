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
            print("Number of players in a game is full, please wait for a new game. ")
        else:
            self.players.append(player)
            print(f"Adding the player {player.name} to the game...")

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
    print("Welcome to the game!")
    # adding players to the game
    for i in range(1, 4):
        name = input(f"Player {i}, enter your name: ")
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
        print(f"Player {player.name}s cards are: ")
        player.print_cards()
        player.count_points()
        print()

    # change card
    change_card = False
    for player in weird_poker.players:
        user_answer = input(f"Player {player.name}, do you want to change any cards? (y/n): ")
        if user_answer == "y":
            index = int(input("Enter the index of the card you want to change (starting from 0): "))
            player.change_card(index)
            print("Card successfully changed.")
            change_card = True
            player.count_points()

    if change_card:
        for player in weird_poker.players:
            print(f"Player {player.name}s current cards are: ")
            player.print_cards()
            print()

    # -TODO- implement winner logic
    # see the looser
    min_player = find_loser(weird_poker)
    if min_player is None:
        return

    print(f"Player {min_player.name} has {min_player.points} points, and lost.")
    weird_poker.players.remove(min_player)

    if len(weird_poker.players) == 1:
        print(f"Player {weird_poker.players[0].name} has won with {weird_poker.players[0].points}, congratulations.")
        return

    min_player = find_loser(weird_poker)
    if min_player is None:
        return
    print(f"Player {min_player.name} has {min_player.points} points, and lost.")
    weird_poker.players.remove(min_player)

    print(f"Player {weird_poker.players[0].name} has won with {weird_poker.players[0].points}, congratulations.")

def main():
    grand_game_loop()

if __name__ == "__main__":
    main()
