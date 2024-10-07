from lib.user_interface import UserInterface

class AssignPlayers(UserInterface):
    def call(self):
        players = 0
        while not players in [1, 2]:
            response = self._prompt("How many players?")
            players = int(response.strip())
        if players == 2:
            self.game.assign_players(self._prompt("Player One, what is your name?"), self._prompt("Player Two, what is your name?"))
        else:
            self.game.assign_players(self._prompt("What is your name?"))
