from lib.user_interface import UserInterface

class PlaceShips(UserInterface):
    def call(self, player):
        if not player.is_human:
            player.place_ships()
            return
        
        self._show(f"Welcome to the game, {player.name}!")
        self._show("Set up your ships first.")
        self._show(self._format_board(player))
        while player.unplaced_ships:
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message(player)))
            try:
                self._prompt_for_ship_placement(player)
            except Exception as error:
                self._show(str(error))
                continue
            self._show("This is your board now:")
            self._show(self._format_board(player))
