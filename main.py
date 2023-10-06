# import sys
# import numpy as np
# from puzzle_tree import EightPuzzle
# from algoritmos.BFS_Solver import bfs
# from algoritmos.IDS_Solver import ids
# from algoritmos.UCS_Solver import ucs
# from algoritmos.GBF_Solver import gbf
# from algoritmos.AStar_Solver import astar
# from algoritmos.HC_Solver import hill

# if __name__ == "__main__":
#     # Conferindo se tem os parâmetros da linha de comando
#     if len(sys.argv) < 3 or len(sys.argv) > 4:
#         print("Uso: python nome_do_programa.py <algoritmo> <estado_inicial> [PRINT]")
#         sys.exit(1)

#     # Escolha do Algoritmo
#     algorithm_choice = sys.argv[1]
#     if algorithm_choice not in ['B', 'I', 'U', 'A', 'G', 'H']:
#         print("Escolha de algoritmo inválida.")
#         sys.exit(1)

#     # Puzzle recebido
#     input_state = sys.argv[2].split()
#     if len(input_state) != 9:
#         print("O estado inicial deve conter 9 números separados por espaço.")
#         sys.exit(1)
#     initial_state = np.array([int(x) for x in input_state]).reshape(3, 3)

#     # Verifique se "PRINT" está presente na linha de comando
#     print_enabled = len(sys.argv) == 4 and sys.argv[3].upper() == "PRINT"

#     # Criação do Puzzle
#     puzzle = EightPuzzle(initial_state)

#     # Execução da solucao do Algoritmo
#     #if algorithm_choice == 'B':
#     solution = bfs(puzzle)
#     #elif algorithm_choice == 'H':
#     solution = hill(puzzle)
#     #elif algorithm_choice == 'I':
#     solution = ids(puzzle)
#     #elif algorithm_choice == 'U':
#     solution = ucs(puzzle)
#     #elif algorithm_choice == 'A':
#     solution = astar(puzzle)
#     #elif algorithm_choice == 'G':
#     solution = gbf(puzzle)

#     # Resultado
#     if solution:
#         print("Solução encontrada em", puzzle.count_steps(solution), "passos:")
#         if print_enabled:
#             puzzle.print_steps(solution)
#     else:
#         print("Nenhuma solução encontrada.")


import time
import matplotlib.pyplot as plt
from collections import defaultdict
from puzzle_tree import EightPuzzle
from algoritmos.BFS_Solver import bfs
from algoritmos.IDS_Solver import ids
from algoritmos.UCS_Solver import ucs
from algoritmos.GBF_Solver import gbf
from algoritmos.AStar_Solver import astar
from algoritmos.HC_Solver import hill

# Dicionário de casos de teste
inputs = {
    7: [[1, 5, 2], [4, 8, 0], [7, 6, 3]],
    10: [[5, 8, 2], [1, 0, 3], [4, 7, 6]],
    13: [[5, 8, 2], [0, 7, 3], [1, 4, 6]],
    16: [[8, 7, 2], [5, 0, 3], [1, 4, 6]],
    19: [[8, 0, 7], [5, 3, 2], [1, 4, 6]],
    22: [[0, 8, 7], [5, 4, 2], [1, 6, 3]],
    25: [[8, 4, 7], [5, 6, 0], [1, 3, 2]],
    28: [[8, 4, 7], [6, 2, 3], [5, 1, 0]],
    31: [[8, 6, 7], [2, 5, 4], [3, 0, 1]],
}

algorithms = {
    'BFS': bfs,
    'IDS': ids,
    'UCS': ucs,
    'GBF': gbf,
    'AStar': astar,
    'HC': hill,
}

results = defaultdict(list)

for depth, initial_state in inputs.items():
    for algorithm_name, algorithm_func in algorithms.items():
        start_time = time.time()
        puzzle = EightPuzzle(initial_state)
        solution = algorithm_func(puzzle)
        end_time = time.time()

        if solution:
            depth_of_tree = len(solution)
        else:
            depth_of_tree = float('inf')

        results[algorithm_name].append((end_time - start_time, depth_of_tree))

# Plotagem dos resultados
for algorithm_name, data in results.items():
    execution_times, depth_of_trees = zip(*data)
    plt.figure()
    plt.scatter(execution_times, depth_of_trees)
    plt.xlabel('Tempo de Execução (s)')
    plt.ylabel('Profundidade da Árvore')
    plt.title(f'{algorithm_name} - Análise de Desempenho')
    plt.show()
