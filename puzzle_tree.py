class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):  # usado no Uniform Cost Search
        return self.cost < other.cost

    def get_solution_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))

    def generate_children(self):
        children = []
        empty_row, empty_col = self.find_empty_position()
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if self.is_valid_move(new_row, new_col):
                new_state = self.swap(empty_row, empty_col, new_row, new_col)
                cost = self.cost + 1  # incrementa o custo quando vai para outro estado
                children.append(Node(new_state, self, move, cost))

        return children

    def find_empty_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3

    def swap(self, r1, c1, r2, c2):
        new_state = [list(row) for row in self.state]
        new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
        return new_state


class EightPuzzle:
    # colocar nodo como um atributo do puzzle?
    def __init__(self, initial_state):
        self.goal_state = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]]
        self.initial_state = initial_state

    def is_goal_state(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    return False
        return True

    def count_steps(self, solution):
        return len(solution)-1 if solution else 0

    def print_state(self, state):
        for row in state:
            row_str = ' '.join(' ' if cell == 0 else str(cell) for cell in row)
            print(row_str)
        
    def print_steps(self, solution):
        self.print_state(self.initial_state)
        print()

        for state in solution[1:]:
            self.print_state(state)
            print()

        if not self.is_goal_state(solution[-1]):
            print("O path não atingiu a solução do estado objetivo.")