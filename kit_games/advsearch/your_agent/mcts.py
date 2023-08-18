from math import log, sqrt
import random
from time import time
from typing import Tuple

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

C = 1
MAX_TIME = 5
class Nodo:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move

        self.children = []
        self.wins = 0
        self.visits = 0
        self.possible_moves = state.legal_moves()

    def ucb_select(self):
        selection = sorted(self.children, key = lambda c: c.wins/c.visits + 2*C*sqrt(2*log(self.visits)/c.visits))
        return selection
    
    def add_child(self, move, state):
        n = Nodo(state, self, move)
        self.possible_moves.remove(move)
        self.children.append(n)

        return n

def backpropagation(nodo: Nodo, result):
    while nodo != None:
        nodo.visits += 1
        nodo.wins += result
        nodo = nodo.parent
    
def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo retorna uma jogada ilegal
    # Remova-o e coloque a sua implementacao do MCTS

    start_time = time()
    raiz = Nodo(state)

    while time() - start_time < MAX_TIME:
        nodo = raiz

        while nodo.possible_moves == [] and nodo.children != []:
            nodo = nodo.ucb_select()

        while not nodo.state.is_terminal():
            move = random.choice(nodo.possible_moves)
            new_state = nodo.state.copy().next_state(move)
            next_node = Nodo(new_state, nodo, move)
            nodo = nodo.add_child(next_node, move, new_state)

        winner = nodo.state.winner()
        result = 0
        if winner == state.player:
            result = 1
        elif winner == state.get_board().opponent(state.player):
            result = -1

        backpropagation(nodo, result)

    return nodo.state.move



