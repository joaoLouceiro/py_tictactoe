from tkinter import Tk
from pytactoe.board import Board

def main():
    window = Tk()
    window.title("PyTacToe")
    _ = window.config(padx=100, pady=50)
    Board(parent=window)
    window.mainloop()

if __name__ == "__main__":
    main()

