from lib.ship_placement import ShipPlacement

class Player():
    def __init__(self, game, name, is_human):
        self.game = game
        self.name = name
        self.is_human = is_human
        self.ships_placed = []
        self.unplaced_ships = []
        self.hits = set()
        self.misses = set()

    def assign_name(self, name):
        self.name = name
    
    def assign_game(self, game):
        self.game = game
    
    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return ship_placement
        return False
    
    def hit_at(self, row, col):
        return any(cell for cell in self.hits if cell == (row, col))
    
    def miss_at(self, row, col):
        return any(cell for cell in self.misses if cell == (row, col))

    def place_ship(self, ship_placement):
        self.unplaced_ships.remove(self._unplaced_ship(ship_placement.length))
        self.ships_placed.append(ship_placement)

    def takes_a_shot(self, opponent, target_row, target_col):
        if not 0 < target_row <= self.game.rows and 0 < target_col <= self.game.cols:
            raise Exception('Coordinates invalid!')
        if (target_row, target_col) in opponent.hits.union(opponent.misses):
            raise Exception("You've already fired at those coordinates.")
        
        return opponent.receives_a_shot(target_row, target_col)

    def receives_a_shot(self, target_row, target_col):
        target_present = self.ship_at(target_row, target_col)
        if target_present:
            self.hits.add((target_row, target_col))
            ship_sunk = target_present.takes_a_hit()
            if ship_sunk:
                self.ships_placed.remove(ship_sunk)
            return [True, ship_sunk]
        else:
            self.misses.add((target_row, target_col))
            return [False, None]

    def _unplaced_ship(self, length):
        try:
            return next(ship for ship in self.unplaced_ships if ship.length == length)
        except StopIteration:
            raise Exception(f"{self.name} doesn't have any unplaced ships of that size!")
