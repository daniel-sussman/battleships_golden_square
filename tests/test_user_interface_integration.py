import unittest

from lib.user_interface import UserInterface
from lib.assign_players import AssignPlayers
from lib.place_ships import PlaceShips
from lib.do_battle import DoBattle
from lib.game import Game
from lib.player import Player
from lib.ship_placement import ShipPlacement
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def _one_player_scenario(self):
        io = TerminalInterfaceHelperMock()
        game = Game()
        interface = UserInterface(io, game)
        io.expect_print("How many players?")
        io.provide("1")
        io.expect_print("What is your name?")
        io.provide("Daniel")
        AssignPlayers(io, game).call()
        return [io, interface, game]
    
    def _two_player_scenario(self):
        io = TerminalInterfaceHelperMock()
        game = Game()
        interface = UserInterface(io, game)
        io.expect_print("How many players?")
        io.provide("2")
        io.expect_print("Player One: What is your name?")
        io.provide("Daniel")
        io.expect_print("Player Two: What is your name?")
        io.provide("Will")
        AssignPlayers(io, game).call()
        return [io, interface, game]
    
    def _ship_setup_scenario(self):
        io, interface, game = self._one_player_scenario()
        player = game.player_one
        io.expect_print("Welcome to the game, Daniel!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Enter coordinates:")
        io.provide("B3")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  S  ~  ~  ~  ~  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Enter coordinates:")
        io.provide("F4")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  S  ~  ~  ~  S  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Enter coordinates:")
        io.provide("A8")
        io.expect_print("Daniel doesn't have any unplaced ships of that size!")
        io.expect_print("You have these ships remaining: 3, 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Enter coordinates:")
        io.provide("A8")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  S  ~  ~  ~  S  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "8   S  S  S  S  S  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("You have these ships remaining: 3, 3")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Enter coordinates:")
        io.provide("F3")
        io.expect_print("There's already a ship there!")
        io.expect_print("You have these ships remaining: 3, 3")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Enter coordinates:")
        io.provide("F3")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  S  S  S  ~  ~",
            "4   ~  S  ~  ~  ~  S  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "8   S  S  S  S  S  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("You have these ships remaining: 3")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Enter coordinates:")
        io.provide("I9")
        io.expect_print("That placement is invalid!")
        io.expect_print("You have these ships remaining: 3")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Enter coordinates:")
        io.provide("G9")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  S  S  S  ~  ~",
            "4   ~  S  ~  ~  ~  S  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "8   S  S  S  S  S  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  S  S  S  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        PlaceShips(io, game).call(player)
        game.player_two.ships_placed = [
            ShipPlacement(
                game=game,
                player=game.player_two,
                length=2,
                orientation='horizontal',
                row=1,
                col=1)]
        game.player_two.unplaced_ships = []
        return [io, interface, game]
    
    def _do_battle_scenario(self):
        io, interface, game = self._ship_setup_scenario()
        game.player_one.hits = {(8, 1)} # Enemy has already hit our battleship
        game.player_one.misses = {(7, 1), (9, 1)} # Enemy will next try (8, 2)
        io.expect_print("The enemy has been sighted.")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("Daniel, fire at target!")
        io.expect_print("Enter coordinates:")
        io.provide('A1')
        io.expect_print("Daniel's shot has landed. A direct hit!")
        io.expect_print("OK.")
        io.provide("")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  S  ~  ~  ~  S  S  S  ~  ~",
            "4   ~  S  ~  ~  ~  S  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "7   •  ~  ~  ~  ~  S  ~  ~  ~  ~",
            "8   X  X  S  S  S  ~  ~  ~  ~  ~",
            "9   •  ~  ~  ~  ~  ~  S  S  S  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("The enemy's shot has landed. A direct hit!")
        io.expect_print("OK.")
        io.provide("")
        io.expect_print("\n".join([
            "    A  B  C  D  E  F  G  H  I  J",
            "1   X  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "3   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "4   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "5   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~",
            "10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"
        ]))
        io.expect_print("Daniel, fire at target!")
        io.expect_print("Enter coordinates:")
        io.provide('B1')
        io.expect_print("Daniel's shot has landed. A direct hit!")
        io.expect_print("Daniel has sunk the enemy's Destroyer!")
        io.expect_print("OK.")
        io.provide("")
        io.expect_print("The enemy's fleet is annihilated. Daniel is victorious!")
        io.expect_print("OK.")
        io.provide("")
        DoBattle(io, game).call()
        return [io, interface, game]

    def test_one_player_scenario(self):
        _, _, game = self._one_player_scenario()
        assert game.player_one.name == 'Daniel'
    
    def test_ship_setup_places_all_ships(self):
        _, _, game = self._ship_setup_scenario()
        assert game.player_one.unplaced_ships == []
        assert len(game.player_one.ships_placed) == 5

    def test_do_battle(self):
        io, interface, game = self._do_battle_scenario()