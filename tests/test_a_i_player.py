from lib.a_i_player import AIPlayer
from unittest.mock import Mock

game = Mock(name='game', rows=10, cols=10)
game.valid_cell.return_value = True
game.ship_at.return_value = False

def test_place_all_ships_assigns_all_the_ships():
    player = AIPlayer(game)
    player.unplaced_ships = [Mock(length=2), Mock(length=3), Mock(length=3), Mock(length=4), Mock(length=5)]
    player.place_ships()
    assert not any(player.unplaced_ships)
    assert len(player.ships_placed) == 5

def test_with_existing_target_fires_a_shot_close_by():
    player = AIPlayer(game)
    opponent = AIPlayer(game)
    opponent.hits = {(5, 5)}
    coords = player.acquires_target(opponent)
    assert coords in [(4, 5), (6, 5), (5, 4), (5, 6)]

def test_avoids_repeating_previous_misses():
    player = AIPlayer(game)
    opponent = AIPlayer(game)
    opponent.hits = {(5, 5)}
    opponent.misses = {(4, 5), (5, 4), (5, 6)}
    assert player.acquires_target(opponent) == (6, 5)

def test_zeros_in_on_correct_axis():
    player = AIPlayer(game)
    opponent = AIPlayer(game)
    opponent.hits = {(5, 5), (5, 6)}
    opponent.misses = {(5, 7)}
    assert player.acquires_target(opponent) == (5, 4)
