import heapq
from puzzle_tree import Node

def heuristic_greedy(state, goal_state):
    # Heurística: número de peças fora do lugar
    return sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))

def gbf(puzzle):
    initial_node = Node(puzzle.initial_state)
    goal_state = puzzle.goal_state
    
    fila = []
    heapq.heappush(fila, (heuristic_greedy(initial_node.state, goal_state), initial_node))
    visited = set()

    while fila:
        _, current_node = heapq.heappop(fila)

        if puzzle.is_goal_state(current_node.state):
            return current_node.get_solution_path()

        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(fila, (heuristic_greedy(child.state, goal_state), child))

    return None