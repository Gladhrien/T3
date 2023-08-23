import random
from typing import Tuple

from ..othello.board import Board
from ..othello.gamestate import GameState
from .minimax import minimax_move
from .othello_minimax_mask import evaluate_mask


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_custom)


def potential(state, player: str) -> float:
    board = state.get_board()
    opponent = Board.opponent(player)
    sum = 0
    for i in range(8):
        for j in range(8):
            for direction in Board.DIRECTIONS:
                if board.tiles[i][j] == opponent:
                    move = (i, j) + direction
                    if board.is_within_bounds(move) and board.tiles[move[0]][move[1]] == Board.EMPTY:
                        sum += 1
    return sum


def evaluate_custom(state, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player.
    If the state is terminal, returns its utility.
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    if state.is_terminal():
        legal_moves = 0
    else:
        legal_moves = len(state.legal_moves())
    potential_moves = potential(state, player)
    mask = evaluate_mask(state, player)
    combined_mobility = 0.6 * legal_moves + 0.4 * potential_moves
    return 0.5 * combined_mobility + 0.5 * mask
