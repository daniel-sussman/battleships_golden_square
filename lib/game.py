from lib.human_player import HumanPlayer
from lib.a_i_player import AIPlayer
from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols

    def assign_players(self, player_one_name, player_two_name=None):
        self.player_one = HumanPlayer(self, player_one_name)
        self.player_two = HumanPlayer(self, player_two_name) if player_two_name else AIPlayer(self)
        for player in [self.player_one, self.player_two]:
            player.unplaced_ships = self._fleet()
        self.active_player = self.player_one
        self.opponent = self.player_two

    def place_ship(self, player, length, orientation, row, col):
        ship_placement = ShipPlacement(
            game=self,
            player=player,
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        player.place_ship(ship_placement)

    def ship_at(self, player, row, col):
        for ship_placement in player.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def valid_cell(self, row, col):
        return 0 < row <= self.rows and 0 < col <= self.cols

    def end_turn(self):
        self.active_player, self.opponent = [self.opponent, self.active_player]

    def _fleet(self):
        return [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]