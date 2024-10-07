from lib.user_interface import UserInterface

class DoBattle(UserInterface):
    def call(self):
        self._show("The enemy has been sighted.")

        while self.game.player_one.ships_placed and self.game.player_two.ships_placed:
            player, opponent = [self.game.active_player, self.game.opponent]
            hit, sunk = self._prompt_for_shot(player, opponent)
            if not player.is_human:
                self._show(self._format_board(opponent, ships_visible=True))
            self._show(f"{player.name.capitalize()}'s shot has landed. A direct hit!" if hit else f"{player.name.capitalize()}'s shot has missed.")
            if sunk:
                self._show(f"{player.name.capitalize()} has sunk {opponent.name}'s {self._name_of(sunk)}!")
            self._prompt("OK.")
            self.game.end_turn()
        
        self._show(f"{self.game.active_player.name.capitalize()}'s fleet is annihilated. {self.game.opponent.name.capitalize()} is victorious!")
        self._prompt("OK.")