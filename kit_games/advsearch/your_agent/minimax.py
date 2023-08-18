import random
from typing import Tuple, Callable

def alpha_beta_pruning(state, depth:int, alpha:float, beta:float, eval_func:Callable) -> float:
    
    if depth == 0 or state.is_terminal():
        return eval_func(state, state.player)
    
    is_max = False
    if state.player == 'W':
        is_max = True
    
    if is_max:
        value = 

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
    moves = state.legal_moves()

    if len(moves) == 0:
        return (-1, -1)
    
    best_value = 0
    best_move = None

    for move in moves:

    raise NotImplementedError()
