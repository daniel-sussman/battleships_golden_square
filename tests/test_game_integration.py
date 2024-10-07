from lib.ship_placement import ShipPlacement
from lib.game import Game
from lib.player import Player
from lib.ship import Ship
from pytest import raises

game = Game()
player = Player(game, 'Daniel', is_human=False)

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game.assign_players('Daniel')
    unplaced_ships = game.player_one.unplaced_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    player.unplaced_ships = [Ship(2)]
    game.place_ship(player, length=2, orientation="vertical", row=3, col=2)
    assert player.ship_at(3, 2)
    assert player.ship_at(4, 2)
    assert not player.ship_at(3, 3)
    assert not player.ship_at(4, 3)
    assert not player.ship_at(3, 1)
    assert not player.ship_at(4, 1)

"""
As a player
So that I can have a coherent game
I would like ships to be constrained to be on the board
"""

def test_no_error_if_ship_on_board():
    ShipPlacement(
        player=player, game=game, length=10, orientation="horizontal", row=1, col=1)
    ShipPlacement(
        player=player, game=game, length=1, orientation="vertical", row=10, col=10)

def test_raises_exception_if_starting_cell_off_board():
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=5, orientation="horizontal", row=0, col=1)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=5, orientation="horizontal", row=11, col=1)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=5, orientation="horizontal", row=1, col=0)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=5, orientation="horizontal", row=1, col=11)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'
    
def test_raises_exception_if_placement_overruns_board():
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=3, orientation="vertical", row=9, col=1)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'
    with raises(Exception) as e:
        ShipPlacement(
            player=player, game=game, length=2, orientation="horizontal", row=1, col=10)
    error_message = str(e.value)
    assert error_message == 'That placement is invalid!'

"""
As a player
So that I can refine my strategy
I would like to know when I have sunk an opponent's ship
"""

def test_player_can_know_when_sunk_opponents_ship():
    player = Player(game, name='Daniel', is_human=True)
    opponent = Player(game, name='The enemy', is_human=False)
    ship_placement = ShipPlacement(game, opponent, length=2, orientation='horizontal', row=1, col=1)
    opponent.ships_placed = [ship_placement]
    player.takes_a_shot(opponent, 1, 1)
    player.takes_a_shot(opponent, 1, 2)
    