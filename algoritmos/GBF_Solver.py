import heapq
import numpy as np
from puzzle_tree import Node

def heuristic_greedy(state, goal_state):
    # Heurística: número de peças fora do lugar
    return np.sum(state != goal_state)

def gbf(puzzle):
    fila = []
    visited = set()

    initial_node = Node(puzzle.initial_state)
    heapq.heappush(fila, (heuristic_greedy(puzzle.initial_state, puzzle.goal_state), initial_node))

    while fila:
        _, current_node = heapq.heappop(fila)

        if np.array_equal(current_node.state, puzzle.goal_state):
            return current_node.get_solution_path()

        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(fila, (heuristic_greedy(child.state, puzzle.goal_state), child))

    return None