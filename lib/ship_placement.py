class ShipPlacement:
    def __init__(self, game, player, length, orientation, row, col):
        self.game = game
        self.player = player
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.hits = 0
        self._validate()

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length
        
    def takes_a_hit(self):
        self.hits += 1
        return self if self.hits == self.length else None
        
    def _validate(self):
        axis = 0 if self.orientation == "vertical" else 1
        current_cell = [self.row, self.col]
        for _ in range(self.length):
            if not self.game.valid_cell(*current_cell):
                raise Exception('That placement is invalid!')
            if self.game.ship_at(self.player, *current_cell):
                raise Exception("There's already a ship there!")
            current_cell[axis] += 1

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
