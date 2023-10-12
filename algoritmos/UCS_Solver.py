from puzzle_tree import Node
from queue import PriorityQueue

def ucs(puzzle):
    initial_node = Node(puzzle.initial_state)

    if puzzle.is_goal_state(puzzle.initial_state):
        return [puzzle.initial_state]

    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, initial_node))

    while not priority_queue.empty():
        cost, current_node = priority_queue.get() # obtém o nó com o menor custo da fila de prioridade
        visited.add(tuple(map(tuple, current_node.state)))

        if puzzle.is_goal_state(current_node.state):
            return current_node.get_solution_path()

        # gera os filhos do nó atual
        for child in current_node.generate_children():
            child_state_tuple = tuple(map(tuple, child.state))
            if child_state_tuple not in visited:
                priority_queue.put((child.cost, child)) # adiciona o filho à fila de prioridade com seu custo

    return None
