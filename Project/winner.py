def is_winner(players):
    maximum_point = max([player.point for player in players])
    return maximum_point