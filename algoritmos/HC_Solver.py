import numpy as np
from puzzle_tree import Node

def heuristic(state, goal_state):
    # Heurística: número de peças fora do lugar
    return np.sum(state != goal_state)

def hill(puzzle):
    k = 10
    current_node = Node(puzzle.initial_state)
    while k > 0:
        children = current_node.generate_children()
        if not children:
            break

        children.sort(key=lambda node: heuristic(node.state, puzzle.goal_state))
        best_child = children[0]

        if heuristic(best_child.state, puzzle.goal_state) >= heuristic(current_node.state, puzzle.goal_state):
            break

        current_node = best_child
        k -= 1

    if np.array_equal(current_node.state, puzzle.goal_state):
        return current_node.get_solution_path()
    else:
        return None