import heapq
import numpy as np
from puzzle_tree import Node

def heuristic_manhattan(state, goal_state):
    # Heurística: Distância de Manhattan
    goal_positions = {goal_state[i, j]: (i, j) for i in range(3) for j in range(3)}
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i, j] != 0:
                goal_row, goal_col = goal_positions[state[i, j]]
                total_distance += abs(i - goal_row) + abs(j - goal_col)
    return total_distance

def astar(puzzle):
    fila = []
    visited = set()

    initial_node = Node(puzzle.initial_state)
    heapq.heappush(fila, (initial_node.cost + heuristic_manhattan(puzzle.initial_state, puzzle.goal_state), initial_node))

    while fila:
        _, current_node = heapq.heappop(fila)

        if np.array_equal(current_node.state, puzzle.goal_state):
            return current_node.get_solution_path()

        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(fila, (child.cost + heuristic_manhattan(child.state, puzzle.goal_state), child))

    return None