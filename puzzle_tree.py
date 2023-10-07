class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):  # Used in Uniform Cost Search
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
                cost = self.cost + 1  # Increment the cost when moving to the new state
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
    def __init__(self, initial_state):
        # Define the goal state
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
        # Function to print the puzzle state
        for row in state:
            print(' '.join(map(str, row)))

    def print_steps(self, solution):
        if solution:
            current_state = [list(row) for row in self.initial_state]
            for state in solution:
                self.print_state(current_state)
                current_state = [list(row) for row in state]
                print()  # Add a blank line after each state
