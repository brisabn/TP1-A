from collections import deque
from puzzle_tree import Node

def bfs(puzzle):
    initial_node = Node(puzzle.initial_state)

    if puzzle.is_goal_state(puzzle.initial_state):
        return [puzzle.initial_state]

    visited = set()
    queue = deque([initial_node])

    while queue:
        current_node = queue.popleft()
        visited.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in visited:
                if puzzle.is_goal_state(child.state):
                    return child.get_solution_path()
                queue.append(child)

    return None