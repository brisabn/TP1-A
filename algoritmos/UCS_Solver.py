import numpy as np
from puzzle_tree import Node
import heapq

def ucs(puzzle):
    visited = set() 
    fila = []
    root = Node(puzzle.initial_state)

    heapq.heappush(fila, (0, root)) # Adiciona o nó raiz à fila de prioridade com custo 0

    while fila:
        cost, current_node = heapq.heappop(fila)  # Remove o nó com menor custo da fila de prioridade

        if np.array_equal(current_node.state, puzzle.goal_state):
            return current_node.get_solution_path()

        visited.add(tuple(current_node.state.ravel()))  # Adiciona o estado atual ao conjunto de nós explorados
        children = current_node.generate_children()

        for child in children:
            # Verifica se o filho não foi explorado ainda
            if tuple(child.state.ravel()) not in visited:
                # Calcula o custo total do caminho até o filho
                total_cost = child.cost + cost

                # Adiciona o filho à fila de prioridade com o custo total
                heapq.heappush(fila, (total_cost, child))
    return None