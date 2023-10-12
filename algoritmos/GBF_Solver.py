import heapq
from puzzle_tree import Node

def heuristic_mismatch(state, goal_state):
    # Heurística: Número de peças fora do lugar
    return sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))

def heuristic_manhattan(state, goal_state):
    # Heurística: Distância de Manhattan
    goal_positions = {goal_state[i][j]: (i, j) for i in range(3) for j in range(3)}
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = goal_positions[state[i][j]]
                total_distance += abs(i - goal_row) + abs(j - goal_col)
    return total_distance

def gbf(puzzle):
    initial_node = Node(puzzle.initial_state)
    goal_state = puzzle.goal_state
    
    fila = []
    # fila de prioridade!
    heapq.heappush(fila, (heuristic_mismatch(initial_node.state, goal_state), initial_node)) 
    visited = set()

    while fila:
        _, current_node = heapq.heappop(fila) # remove nó da fila com menor estimativa heurística

        if puzzle.is_goal_state(current_node.state):
            return current_node.get_solution_path()

        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children(): # gera filhos do nó atual
            if tuple(map(tuple, child.state)) not in visited:
                heapq.heappush(fila, (heuristic_mismatch(child.state, goal_state), child))

    return None