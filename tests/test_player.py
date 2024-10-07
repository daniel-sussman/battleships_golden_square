from lib.player import Player
from unittest.mock import Mock

game = Mock(name='game', rows=10, cols=10)
game.valid_cell.return_value = True
game.ship_at.return_value = False

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    player = Player(game, name='Daniel', is_human=True)
    for row in range(1, 11):
        for col in range(1, 11):
            assert not player.ship_at(row, col)

"""
As a player
So that I can win the game
I would like to be able to fire at my opponent's board
"""
ship_placement = Mock()
ship_placement.takes_a_hit.return_value = None

def test_player_can_fire_at_opponents_board():
    player = Player(game, name='Daniel', is_human=True)
    opponent = Player(game, name='Will', is_human=True)
    ship_placement.covers.return_value = True
    opponent.ships_placed = [ship_placement]
    target_row = 1
    target_col = 1
    player.takes_a_shot(opponent, target_row, target_col)
    assert opponent.hits == {(1, 1)}

def test_player_can_receive_a_miss():
    player = Player(game, name='Daniel', is_human=True)
    ship_placement.covers.return_value = False
    player.ships_placed = [ship_placement]
    player.receives_a_shot(1, 1)
    assert player.misses == {(1, 1)}

def test_player_can_receive_a_hit():
    player = Player(game, name='Daniel', is_human=True)
    ship_placement.covers.return_value = True
    player.ships_placed = [ship_placement]
    player.receives_a_shot(1, 1)
    assert player.hits == {(1, 1)}
