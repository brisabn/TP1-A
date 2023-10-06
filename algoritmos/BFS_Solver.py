from collections import deque
import numpy as np
from puzzle_tree import Node

def bfs(puzzle):
    fila = deque() # Inicialize uma fila para a busca em largura
    root = Node(puzzle.initial_state) # Crie o nó raiz com o estado inicial
    fila.append(root) # Adicione o nó raiz à fila

    visited = set()  # Inicialize um conjunto para rastrear estados visitados
    visited.add(root) 

    while fila:
        current_node = fila.popleft() # Retire o nó da frente da fila

        # Verifique se o estado atual é o estado objetivo
        if np.array_equal(current_node.state, puzzle.goal_state):
            return current_node.get_solution_path() # Se sim, retorne o caminho para a solução

        children = current_node.generate_children()  # Gere os filhos do nó atual

        # Verifique se o estado do filho já foi visitado
        for child in children:
            if child not in visited:
                fila.append(child)  # Adicione o filho à fila para explorar
                visited.add(child)  # Marque o filho como visitado

    # Se a fila estiver vazia e nenhum objetivo for encontrado, retorne None (sem solução)
    return None 