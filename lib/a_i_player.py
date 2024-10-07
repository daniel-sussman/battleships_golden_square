from lib.player import Player
from lib.target import Target
from lib.ship_placement import ShipPlacement
from string import ascii_uppercase
import random

class AIPlayer(Player):
    def __init__(self, game):
        self.targets = []
        super().__init__(game, name='the enemy', is_human = False)

    def place_ships(self):
        while any(self.unplaced_ships):
            ship = next(ship for ship in self.unplaced_ships)
            ship_orientation = random.choice(['vertical', 'horizontal'])
            max_row = self.game.rows - (ship.length - 1) if ship_orientation == 'vertical' else self.game.rows
            max_col = self.game.cols - (ship.length - 1) if ship_orientation == 'horizontal' else self.game.cols
            try:
                ship_placement = ShipPlacement(
                    game=self.game,
                    player=self,
                    length=ship.length,
                    orientation=ship_orientation,
                    row=random.randint(1, max_row),
                    col=random.randint(1, max_col),
                )
            except Exception as error:
                if str(error) == "There's already a ship there!":
                    continue
                else:
                    raise Exception(str(error))
            self.place_ship(ship_placement)
    
    def acquires_target(self, opponent):
        targets = [Target(y, x, opponent) for y in range(1, self.game.rows + 1) for x in range(1, self.game.cols + 1) if (y, x) not in opponent.hits and (y, x) not in opponent.misses]
        # print(self._show_ai_target_values(targets))
        max_target_value = max(t.value for t in targets)
        selected_target = random.choice(list(t for t in targets if t.value == max_target_value))
        return (selected_target.row, selected_target.col)
    
    def takes_a_shot(self, opponent, target_row, target_col):
        hit, sunk = super().takes_a_shot(opponent, target_row, target_col)
        if sunk:
            self._clear_sunk_target(opponent, target_row, target_col, sunk)
        return (hit, sunk)

    def _clear_sunk_target(self, opponent, target_row, target_col, sunk):
        for (axis, delta) in [(0, -1), (0, 1), (1, -1), (1, 1)]:
            if (target_row + delta * (1 - axis), target_col + delta * axis) in opponent.hits:
                cells_to_clear = [(target_row + incr * delta * (1 - axis), target_col + incr * delta * axis) for incr in range(sunk.length)]
                return self._clear_target(opponent, cells_to_clear)

    def _clear_target(self, opponent, cells_to_clear):
        for cell in cells_to_clear:
            opponent.hits.remove(cell)
            opponent.misses.add(cell)

    def _show_ai_target_values(self, targets):
        # for testing
        rows = ["    " + "   ".join(list(ascii_uppercase[:self.game.cols]))]
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                target_present = [f"{t.value:02}" for t in targets if t.row == row and t.col == col]
                if any(target_present):
                    row_cells.append(target_present[0])
                else:
                    row_cells.append("00")
            rows.append(f"{row:<4}" + "  ".join(row_cells))
        return "\n".join(rows)