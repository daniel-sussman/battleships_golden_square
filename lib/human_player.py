from lib.player import Player

class HumanPlayer(Player):
    def __init__(self, game, name):
        super().__init__(game, name, is_human=True)