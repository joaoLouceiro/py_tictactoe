import pytest
from pytactoe.board import check_for_victory_and_return_winner, convert_number_to_symbol

def test_convert_number_zero_to_space():
    assert convert_number_to_symbol(0) == " "

def test_convert_number_one_to_circle():
    assert convert_number_to_symbol(1) == "O"

def test_convert_number_two_to_cross():
    assert convert_number_to_symbol(2) == "X"

def test_invalid_player_raises_error():
    with pytest.raises(KeyError) as ex:
        convert_number_to_symbol(3)

    assert ex.type is KeyError

@pytest.mark.parametrize("board,expected", [ 
                                            ( [[1, 1, 1],
                                               [0, 0, 0],
                                               [0, 0, 0]],
                                             (True, 1)),
                                            ( [[0, 0, 0],
                                               [1, 1, 1],
                                               [0, 0, 0]],
                                             (True, 1)),
                                            ( [[0, 0, 0],
                                               [0, 0, 0],
                                               [1, 1, 1]],
                                             (True, 1)),
                                            ( [[2, 2, 2],
                                               [0, 0, 0],
                                               [0, 0, 0]],
                                             (True, 2)),
                                            ( [[0, 0, 0],
                                               [2, 2, 2],
                                               [0, 0, 0]],
                                             (True, 2)),
                                            ( [[0, 0, 0],
                                               [0, 0, 0],
                                               [2, 2, 2]],
                                             (True, 2)),
                                            ])
def test_for_victory_row(board, expected):
    assert check_for_victory_and_return_winner(board=board) == expected

@pytest.mark.parametrize("board,expected", [ 
                                            ( [[1, 0, 0],
                                               [1, 0, 0],
                                               [1, 0, 0]],
                                             (True, 1)),
                                            ( [[0, 1, 0],
                                               [0, 1, 0],
                                               [0, 1, 0]],
                                             (True, 1)),
                                            ( [[0, 0, 1],
                                               [0, 0, 1],
                                               [0, 0, 1]],
                                             (True, 1)),
                                            ])
def test_for_victory_column(board, expected):
    assert check_for_victory_and_return_winner(board=board) == expected

@pytest.mark.parametrize("board,expected", [ 
                                            ( [[1, 1, 0],
                                               [0, 0, 0],
                                               [0, 0, 0]],
                                             (False, 0)),
                                            ( [[0, 0, 0],
                                               [0, 0, 0],
                                               [0, 0, 0]],
                                             (False, 0)),
                                            ( [[0, 0, 0],
                                               [0, 0, 0],
                                               [1, 2, 1]],
                                             (False, 0)),
                                            ( [[2, 1, 2],
                                               [0, 1, 0],
                                               [0, 2, 1]],
                                             (False, 0)),
                                            ( [[0, 0, 0],
                                               [2, 1, 2],
                                               [0, 0, 0]],
                                             (False, 0)),
                                            ( [[0, 0, 0],
                                               [0, 0, 0],
                                               [2, 1, 2]],
                                             (False, 0)),
                                            ])
def test_no_victory(board, expected):
    assert check_for_victory_and_return_winner(board=board) == expected

@pytest.mark.parametrize("board,expected", [ 
    # Main diagonal win for player 1
    ([[1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]], (True, 1)),
    # Main diagonal win for player 2
    ([[2, 0, 0],
      [0, 2, 0],
      [0, 0, 2]], (True, 2)),
    # Anti-diagonal win for player 1
    ([[0, 0, 1],
      [0, 1, 0],
      [1, 0, 0]], (True, 1)),
    # Anti-diagonal win for player 2
    ([[0, 0, 2],
      [0, 2, 0],
      [2, 0, 0]], (True, 2)),
])
def test_for_victory_diagonal(board, expected):
    assert check_for_victory_and_return_winner(board=board) == expected
