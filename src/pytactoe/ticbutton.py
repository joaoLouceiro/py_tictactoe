from tkinter import Button 

class TicButton(Button):
    def __init__(self, text: str, coord: tuple[int | str, int | str], player_callback=None, update_board_state=None):
        # player_callback should be a function that returns the current player (1 or 2)
        self.coord: tuple[int | str, int | str] = coord
        self.is_pressed: bool = False
        self.player_callback = player_callback
        self.update_board_state = update_board_state
        self.is_game_over = False
        super().__init__(text=text, command=self._make_press_command())

    def _make_press_command(self):
        # Returns a function that calls _on_press_button with the current player
        def command():
            if self.player_callback:
                player = self.player_callback()
                self._on_press_button(player)
        return command

    def _on_press_button(self, player: int):
        if not self.is_pressed and not self.is_game_over:
            self.is_pressed = True
            symbol = "O" if player == 1 else "X"
            self.config(text=symbol)
            if self.update_board_state:
                row, col = self.coord
                self.update_board_state(row, col, player)


