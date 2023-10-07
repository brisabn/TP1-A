from puzzle_tree import Node

# usando memoização 
def ids(puzzle):
    max_depth = 0

    while True:
        result = depth_limited_search(puzzle, max_depth)
        if result is not None:
            return result
        max_depth += 1

def depth_limited_search(puzzle, max_depth):
    visited = set()
    stack = [(Node(puzzle.initial_state), 0)]

    while stack:
        node, current_depth = stack.pop()
        state_hash = tuple(map(tuple, node.state))

        if state_hash in visited:
            continue

        if puzzle.is_goal_state(node.state):
            return node.get_solution_path()

        if current_depth < max_depth:
            visited.add(state_hash)
            children = [(child, current_depth + 1) for child in node.generate_children()]
            stack.extend(children)

    return None