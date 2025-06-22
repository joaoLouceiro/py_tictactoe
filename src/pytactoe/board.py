from tkinter import Tk, Canvas, messagebox

from pytactoe.ticbutton import TicButton

current_player = [1]  # Use a list for mutability in nested scope

class Board():
    def __init__(self, parent=None) -> None:
        board_state = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        self.board_state = board_state
        self.buttons = []  # Store references to all buttons
        self.player1_score = 0
        self.player2_score = 0
        self.score_var = None
        self.score_label = None
        self.score_frame = None
        self.grid_frame = None
        if parent is not None:
            from tkinter import StringVar, Label, Frame
            self.score_var = StringVar()
            self.update_score_text()
            # Create frames for layout
            self.score_frame = Frame(parent)
            self.score_frame.pack(pady=(10, 0))
            self.grid_frame = Frame(parent)
            self.grid_frame.pack(pady=(10, 10))
            self.score_label = Label(self.score_frame, textvariable=self.score_var, font=("Arial", 16))
            self.score_label.pack()
            self.__init_buttons__()

    def __init_buttons__(self) -> None:
        for i_row, row in enumerate(self.board_state):
            button_row = []
            for i_col, col in enumerate(row):
                btn = TicButton(
                    text=" ",
                    coord=(i_row, i_col),
                    player_callback=self.player_callback,
                    update_board_state=self.update_board_state
                )
                if self.grid_frame is not None:
                    btn.grid(row=i_row, column=i_col, in_=self.grid_frame)
                button_row.append(btn)
            self.buttons.append(button_row)

    def player_callback(self):
        player = current_player[0]
        # Switch player for next turn
        current_player[0] = 2 if current_player[0] == 1 else 1
        return player

    def update_score_text(self):
        if self.score_var is not None:
            self.score_var.set(f"Player 1 (O): {self.player1_score}    Player 2 (X): {self.player2_score}")

    def reset_board(self):
        self.board_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        for i_row, row_btns in enumerate(self.buttons):
            for i_col, btn in enumerate(row_btns):
                btn.config(text=" ", state='normal')
                btn.is_pressed = False
        global current_player
        current_player[0] = 1

    def update_board_state(self, row, col, player):
        self.board_state[row][col] = player
        victory, winner = self.check_for_victory_and_return_winner()
        if victory:
            if self.buttons:
                for row_btns in self.buttons:
                    for btn in row_btns:
                        btn.config(state='disabled')
            if winner == 1:
                self.player1_score += 1
            elif winner == 2:
                self.player2_score += 1
            self.update_score_text()
            if self.buttons:
                from tkinter import messagebox
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_board()

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
