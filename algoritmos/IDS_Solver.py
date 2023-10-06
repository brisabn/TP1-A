import numpy as np
from puzzle_tree import Node

def depth_limited_search(node, puzzle, depth_limit):
    if np.array_equal(node.state, puzzle.goal_state):
        return node.get_solution_path()

    if depth_limit <= 0: # Verifica se a profundidade limite foi atingida
        return None

    children = node.generate_children() # filhos do nó atual
    for child in children:
        result = depth_limited_search(child, puzzle, depth_limit - 1) # busca em profundidade limitada nos filhos
        if result is not None:
            return result
    return None

def ids(puzzle):
    max_depth = 0
    while True:
        root = Node(puzzle.initial_state)
        result = depth_limited_search(root, puzzle, max_depth) # Realiza a busca em profundidade limitada com a profundidade máxima atual
        if result is not None:
            return result # Se uma solução for encontrada, retorna o caminho da solução
        max_depth += 1  # Aumenta a profundidade máxima e continua a busca