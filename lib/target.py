class Target():
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player
        self.game = self.player.game
        self.value = self._get_value()

    def _get_value(self):
        value = 0
        for (axis, delta) in [(0, -1), (0, 1), (1, -1), (1, 1)]:
            value += self._get_directional_value(axis, delta)
        return value

    def _get_directional_value(self, axis, delta):
        directional_value = 0

        for i in range(1, 3):
            next_cell = (self.row + delta * i * (1 - axis), self.col + delta * i * axis)
            if not self.game.valid_cell(*next_cell) or next_cell in self.player.misses:
                return directional_value # no more value in this direction

            if next_cell in self.player.hits and not directional_value == 1:
                directional_value += 15 * i # value of previous hit
            else:
                directional_value += 1 * i # value of untried cell

        return directional_value