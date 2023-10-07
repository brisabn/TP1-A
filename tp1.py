import sys
import numpy as np
from puzzle_tree import EightPuzzle
from algoritmos.BFS_Solver import bfs
from algoritmos.IDS_Solver import ids
from algoritmos.UCS_Solver import ucs
from algoritmos.GBF_Solver import gbf
from algoritmos.AStar_Solver import astar
from algoritmos.HC_Solver import hill

if __name__ == "__main__":
    # Conferindo se tem os parâmetros da linha de comando
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Uso: python nome_do_programa.py <algoritmo> <estado_inicial> [PRINT]")
        sys.exit(1)

    # Escolha do Algoritmo
    algorithm_choice = sys.argv[1]
    if algorithm_choice not in ['B', 'I', 'U', 'A', 'G', 'H']:
        print("Escolha de algoritmo inválida.")
        sys.exit(1)

    # Puzzle recebido
    input_state = sys.argv[2].split()
    if len(input_state) != 9:
        print("O estado inicial deve conter 9 números separados por espaço.")
        sys.exit(1)
    initial_state = np.array([int(x) for x in input_state]).reshape(3, 3)

    # Verifique se "PRINT" está presente na linha de comando
    print_enabled = len(sys.argv) == 4 and sys.argv[3].upper() == "PRINT"

    # Criação do Puzzle
    puzzle = EightPuzzle(initial_state)

    # Execução da solucao do Algoritmo
    if algorithm_choice == 'B':
      solution = bfs(puzzle)
    elif algorithm_choice == 'H':
      solution = hill(puzzle)
    elif algorithm_choice == 'I':
       solution = ids(puzzle)
    elif algorithm_choice == 'U':
      solution = ucs(puzzle)
    elif algorithm_choice == 'A':
      solution = astar(puzzle)
    elif algorithm_choice == 'G':
      solution = gbf(puzzle)

    # Resultado
    if solution:
        print("Solução encontrada em", puzzle.count_steps(solution), "passos:")
        if print_enabled:
            puzzle.print_steps(solution)
    else:
        print("Nenhuma solução encontrada.")