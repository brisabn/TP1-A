from puzzle_tree import Node

def heuristic(state, goal_state):
    # Heurística: número de peças fora do lugar
    return sum(state[i][j] != goal_state[i][j] for i in range(3) for j in range(3))

def hill(puzzle):
    k = 1000
    current_node = Node(puzzle.initial_state)
    lateral_moves_count = 0 
    path = [current_node.state]  # Inicializa a lista de caminho com o estado inicial

    while lateral_moves_count < k:
        children = current_node.generate_children()  

        if not children:
            break

        # ordena filhos com base na heurística
        children.sort(key=lambda node: heuristic(node.state, puzzle.goal_state))
        best_child = min(children, key=lambda node: heuristic(node.state, puzzle.goal_state))

        # se a heurística do melhor filho for maior ou igual à heurística do nó atual, paramos a busca
        if heuristic(best_child.state, puzzle.goal_state) >= heuristic(current_node.state, puzzle.goal_state):
            break

        # melhor filho envolve um movimento lateral?
        lateral_move = any(
            best_child.state[i][j] != current_node.state[i][j]
            for i in range(3)
            for j in range(3)
        )

        if lateral_move:
            lateral_moves_count += 1

        # atualizamos o nó atual para o melhor filho e adicionamos o estado ao caminho
        current_node = best_child
        path.append(current_node.state)

    if current_node.state == puzzle.goal_state:
        return path  # Retorna o caminho percorrido
    else:
        return path  # Retorna o caminho até onde chegou

