import sys
from puzzle_tree import EightPuzzle
from algoritmos.BFS_Solver import bfs
from algoritmos.IDS_Solver import ids
from algoritmos.UCS_Solver import ucs
from algoritmos.GBF_Solver import gbf
from algoritmos.AStar_Solver import astar
from algoritmos.HC_Solver import hill

if __name__ == "__main__":
    # Conferindo se tem os parâmetros da linha de comando
    if len(sys.argv) < 10 or len(sys.argv) > 12:
        print("Uso: python nome_do_programa.py <algoritmo> <n1> <n2> <n3> <n4> <n5> <n6> <n7> <n8> <n9> [PRINT]")
        sys.exit(1)

    # Escolha do Algoritmo
    algorithm_choice = sys.argv[1]
    if algorithm_choice not in ['B', 'I', 'U', 'A', 'G', 'H']:
        print("Escolha de algoritmo inválida.")
        sys.exit(1)

    # Verifique se "PRINT" está presente na linha de comando
    print_enabled = len(sys.argv) == 12 and sys.argv[11].upper() == "PRINT"

    # Puzzle recebido
    input_state = sys.argv[2:11]
    numbers = [int(x) for x in input_state]

    # Verificando se há 9 números
    if len(numbers) != 9:
        print("Você deve fornecer exatamente 9 números.")
        sys.exit(1)

    # Verificando se os números são diferentes
    if len(numbers) != len(set(numbers)):
        print("Os números devem ser diferentes.")
        sys.exit(1)

    # Criação do Puzzle
    initial_state = [numbers[:3], numbers[3:6], numbers[6:]]
    puzzle = EightPuzzle(initial_state)
    
    # Execução da solução do Algoritmo
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
        print(puzzle.count_steps(solution))
        if print_enabled:
            puzzle.print_steps(solution)
    else:
        print("O path de solução não foi encontrado")