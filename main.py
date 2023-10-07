import sys
import timeit
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
    
    # Criação do Puzzle
    initial_state = [numbers[:3], numbers[3:6], numbers[6:]]
    puzzle = EightPuzzle(initial_state)

    # Função para medir o tempo de execução do algoritmo
    def measure_execution_time():
        start_time = timeit.default_timer()
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
        end_time = timeit.default_timer()
        return solution, end_time - start_time

    # Medir o tempo de execução
    solution, execution_time = measure_execution_time()

    # Resultado
    if solution:
        print("Solução encontrada em", puzzle.count_steps(solution), "passos")
        if print_enabled:
            puzzle.print_steps(solution)
        
        # Imprimir o tempo de execução no arquivo de texto existente (modo 'a' para append)
        with open("tempo_bfs.txt", "a") as file:
            file.write("{:.6f}\n".format(execution_time))
    else:
        print("Nenhuma solução encontrada.")
