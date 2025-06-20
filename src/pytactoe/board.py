from tkinter import Tk, Canvas

from pytactoe.ticbutton import TicButton

current_player = [1]  # Use a list for mutability in nested scope

class Board():
    def __init__(self) -> None:
        board_state = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.board_state = board_state
        self.__init_buttons__()

    def __init_buttons__(self) -> None:
        for i_row, row in enumerate(self.board_state):
            for i_col, col in enumerate(row):
                TicButton(
                    text=" ",
                    coord=(i_row, i_col),
                    player_callback=self.player_callback,
                    update_board_state=self.update_board_state
                ).grid(row=i_row, column=i_col)

    def player_callback(self):
        player = current_player[0]
        # Switch player for next turn
        current_player[0] = 2 if current_player[0] == 1 else 1
        return player

    def update_board_state(self, row, col, player):
        self.board_state[row][col] = player
        victory, winner = self.check_for_victory_and_return_winner()
        if victory:
            Canvas().create_text(400, 150, text=f"Player {winner} wins!", font=("Arial", 40, "italic"))

    def check_for_victory_and_return_winner(self):
        # Check rows
        board = self.board_state
        for row in board:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return True, row[0]
        # Check columns
        for col in range(3):
            if board[0][col] != 0 and board[0][col] == board[1][col] == board[2][col]:
                return True, board[0][col]
        # Check diagonals
        if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
            return True, board[0][0]
        if board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
            return True, board[0][2]
        return False, 0

window = Tk()
window.title("PyTacToe")
_ = window.config(padx=100, pady=50)


Board()

window.mainloop()
