from functools import cmp_to_key


def sorting(card1, card2):
    if card1[0] == card2[0]:
        if card1[1:] < card2[1:]:
            return -1
        elif card1[0] > card2[0]:
            return 1
        else:

            return 0
    elif card1[0] > card2[0]:
        return 1
    else:
        return -1

class Player:
    def __init__(self, name, game):
        self.name = name
        self.cards = []
        self.points = 0
        self.num_same_cards = 0
        self.num_same_values = 0
        self.game = game

    def count_points(self):
        sorted_list = sorted(self.cards, key=cmp_to_key(sorting))
        temp_num_same_cards = 0
        temp_num_same_values = 0
        for i in range(1, 5):
            card = sorted_list[i]
            self.points += self.game.card_point(card)
            if card[0] == sorted_list[i - 1][0]:
                temp_num_same_cards += 1
            else:
                self.num_same_cards = max(self.num_same_cards, temp_num_same_cards)

            if card[1:] == sorted_list[i - 1][1:]:
                temp_num_same_values += 1
            else:
                self.num_same_values = max(self.num_same_values, temp_num_same_values)

    def add_cards(self):
        for i in range(0, 5):
            card = self.game.generate_card_code()
            self.cards.append(card)

    def change_card(self, index):
        # remove a card from the used_cards
        print(index, len(self.cards))
        self.game.add_card_back(self.cards[index])
        # generate a new card
        self.cards[index] = self.game.generate_card_code()
        return self.cards

    def print_cards(self):
        for i in range(0, 5):
            print(self.game.card_decode(self.cards[i]), end = ", ")

    def __str__(self):
        final_string = f"{self.name}: "
        for card in self.cards:
            final_string += '\n' + self.game.card_decode(card)
        return final_string + '\n'