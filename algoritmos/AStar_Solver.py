from queue import PriorityQueue
from puzzle_tree import Node

def heuristic_mismatch(state, goal_state):
    # Heurística: número de peças fora do lugar
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

def astar(puzzle):
    initial_node = Node(puzzle.initial_state)

    if puzzle.is_goal_state(puzzle.initial_state):
        return [puzzle.initial_state]

    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, initial_node))  # inicialmente, a prioridade é 0

    while not priority_queue.empty():
        _, current_node = priority_queue.get()  # obtém o nó com a menor prioridade da fila de prioridade.
        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in visited:
                if puzzle.is_goal_state(child.state):
                    return child.get_solution_path()
                # calcula a prioridade do filho com base no custo atual e na heurística.
                priority = child.cost + heuristic_manhattan(child.state, puzzle.goal_state)
                priority_queue.put((priority, child))

    return None