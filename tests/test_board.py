import pytest
from pytactoe.board import Board

@pytest.mark.parametrize("board,expected", [ 
    ([[1, 1, 1], [0, 0, 0], [0, 0, 0]], (True, 1)),
    ([[0, 0, 0], [1, 1, 1], [0, 0, 0]], (True, 1)),
    ([[0, 0, 0], [0, 0, 0], [1, 1, 1]], (True, 1)),
    ([[2, 2, 2], [0, 0, 0], [0, 0, 0]], (True, 2)),
    ([[0, 0, 0], [2, 2, 2], [0, 0, 0]], (True, 2)),
    ([[0, 0, 0], [0, 0, 0], [2, 2, 2]], (True, 2)),
])
def test_for_victory_row(board, expected):
    b = Board()
    b.board_state = [row[:] for row in board]
    assert b.check_for_victory_and_return_winner() == expected

@pytest.mark.parametrize("board,expected", [ 
    ([[1, 0, 0], [1, 0, 0], [1, 0, 0]], (True, 1)),
    ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], (True, 1)),
    ([[0, 0, 1], [0, 0, 1], [0, 0, 1]], (True, 1)),
])
def test_for_victory_column(board, expected):
    b = Board()
    b.board_state = [row[:] for row in board]
    assert b.check_for_victory_and_return_winner() == expected

@pytest.mark.parametrize("board,expected", [ 
    ([[1, 1, 0], [0, 0, 0], [0, 0, 0]], (False, 0)),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], (False, 0)),
    ([[0, 0, 0], [0, 0, 0], [1, 2, 1]], (False, 0)),
    ([[2, 1, 2], [0, 1, 0], [0, 2, 1]], (False, 0)),
    ([[0, 0, 0], [2, 1, 2], [0, 0, 0]], (False, 0)),
    ([[0, 0, 0], [0, 0, 0], [2, 1, 2]], (False, 0)),
])
def test_no_victory(board, expected):
    b = Board()
    b.board_state = [row[:] for row in board]
    assert b.check_for_victory_and_return_winner() == expected

@pytest.mark.parametrize("board,expected", [ 
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], (True, 1)),
    ([[2, 0, 0], [0, 2, 0], [0, 0, 2]], (True, 2)),
    ([[0, 0, 1], [0, 1, 0], [1, 0, 0]], (True, 1)),
    ([[0, 0, 2], [0, 2, 0], [2, 0, 0]], (True, 2)),
])
def test_for_victory_diagonal(board, expected):
    b = Board()
    b.board_state = [row[:] for row in board]
    assert b.check_for_victory_and_return_winner() == expected

def test_board_state_update():
    board = Board()
    board.update_board_state(0, 0, 1)
    assert board.board_state[0][0] == 1
    board.update_board_state(1, 1, 2)
    assert board.board_state[1][1] == 2

def test_score_increments_on_win():
    board = Board()
    # Simulate a win for player 1
    board.update_board_state(0, 0, 1)
    board.update_board_state(0, 1, 1)
    board.update_board_state(0, 2, 1)
    assert board.player1_score == 1
    assert board.player2_score == 0

def test_board_resets_after_win():
    board = Board()
    board.update_board_state(0, 0, 1)
    board.update_board_state(0, 1, 1)
    board.update_board_state(0, 2, 1)
    # After win, board should be reset
    assert all(cell == 0 for row in board.board_state for cell in row)
