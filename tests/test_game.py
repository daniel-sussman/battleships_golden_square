from lib.game import Game
from unittest.mock import Mock

player_one = Mock()
player_two = Mock()
"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

def test_can_switch_turns():
    game = Game()
    game.player_one = player_one
    game.player_two = player_two
    game.active_player = player_one
    game.opponent = player_two
    game.end_turn()
    assert game.active_player == player_two
    game.end_turn()
    assert game.active_player == player_one
