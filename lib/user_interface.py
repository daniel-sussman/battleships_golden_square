from string import ascii_uppercase

class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game

    def run(self):
        from lib.assign_players import AssignPlayers
        from lib.place_ships import PlaceShips
        from lib.do_battle import DoBattle
        AssignPlayers(self.io, self.game).call()
        PlaceShips(self.io, self.game).call(self.game.player_one)
        PlaceShips(self.io, self.game).call(self.game.player_two)
        DoBattle(self.io, self.game).call()

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self, player):
        ship_lengths = [str(ship.length) for ship in player.unplaced_ships]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self, player):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        coords = self._prompt("Enter coordinates:")
        ship_col, ship_row = (coords[:1], coords[1:])
        self.game.place_ship(
            player,
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=ascii_uppercase.index(ship_col.upper()) + 1,
        )
        self._show("OK.")
        
    def _prompt_for_shot(self, player, opponent):
        if not player.is_human:
            target_row, target_col = player.acquires_target(opponent)
            return player.takes_a_shot(opponent, target_row, target_col)

        self._show(self._format_board(opponent, ships_visible=False))
        self._show(f"{player.name}, fire at target!")
        while True:
            coords = self._prompt("Enter coordinates:")
            target_col, target_row = (coords[:1], coords[1:])
            try:
                return player.takes_a_shot(opponent, int(target_row), ascii_uppercase.index(target_col.upper()) + 1)
            except Exception as e:
                print(str(e))
                continue

    def _name_of(self, ship_placement):
        if ship_placement.length == 2:
            return 'Destroyer'
        elif ship_placement.length == 3:
            return 'Submarine'
        elif ship_placement.length == 4:
            return 'Battleship'
        elif ship_placement.length == 5:
            return 'Carrier'
        else:
            return 'ship'

    def _format_board(self, player, ships_visible=True):
        rows = ["    " + "  ".join(list(ascii_uppercase[:self.game.cols]))]
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if player.hit_at(row, col):
                    row_cells.append("X")
                elif player.miss_at(row, col):
                    row_cells.append("•")
                elif player.ship_at(row, col) and ships_visible:
                    row_cells.append("S")
                else:
                    row_cells.append("~")
            rows.append(f"{row:<4}" + "  ".join(row_cells))
        return "\n".join(rows)

