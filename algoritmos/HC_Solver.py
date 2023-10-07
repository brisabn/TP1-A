import random

def hill(puzzle):
    current_state = puzzle.initial_state
    current_cost = h(puzzle, current_state)

    for _ in range(k):
        neighbors = get_neighbors(puzzle, current_state)
        if not neighbors:
            break  # No more neighbors to explore

        best_neighbor = min(neighbors, key=lambda x: h(puzzle, x))
        best_neighbor_cost = h(puzzle, best_neighbor)

        if best_neighbor_cost >= current_cost:
            break  # Local minimum, stop hill climbing

        current_state = best_neighbor
        current_cost = best_neighbor_cost

    if puzzle.is_goal_state(current_state):
        return puzzle.get_solution_path()
    else:
        return None

def h(puzzle, state):
    # This is a simple heuristic function that counts the number of misplaced tiles
    h_value = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != puzzle.goal_state[i][j]:
                h_value += 1
    return h_value

def get_neighbors(puzzle, state):
    empty_row, empty_col = puzzle.find_empty_position(state)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbors = []

    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if puzzle.is_valid_move(new_row, new_col):
            neighbor_state = puzzle.swap(state, empty_row, empty_col, new_row, new_col)
            neighbors.append(neighbor_state)

    random.shuffle(neighbors)  # Shuffle the order of neighbors for randomness
    return neighbors
