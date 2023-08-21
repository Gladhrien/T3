import random
from typing import Tuple, Callable

def min_move(state, depth:int, alpha:float, beta:float, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    if depth == 0 or state.is_terminal(): 
        return eval_func(state, state.player), (-1, -1)
    v = float('inf')
    a = (-1, -1)
    for move in state.legal_moves():
        max_v, _ = max_move(state.next_state(move), depth-1, alpha, beta, eval_func)
        if max_v < v:
            a = move
            v = max_v
        alpha = max(alpha, v)
        if alpha >= beta:
            break

    return v, a


def max_move(state, depth:int, alpha:float, beta:float, eval_func:Callable) -> Tuple[float, Tuple[int, int]]:
    if depth == 0 or state.is_terminal(): 
        return eval_func(state, state.player), (-1, -1)
    v = float('-inf')
    a = (-1, -1)
    for move in state.legal_moves():
        min_v, _ = min_move(state.next_state(move), depth-1, alpha, beta, eval_func)
        if min_v > v:
            a = move
            v = min_v
        beta = min(beta, v)
        if beta <= alpha:
            break

    return v, a


def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    _, a = max_move(state, max_depth, float('-inf'), float('inf'), eval_func)
    return a
