#################################################################
# solver.py
#################################################################

from copy import deepcopy
from board.validator import is_valid_placement

def solve_board(sudoku_grid):
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] is None:
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid_placement(sudoku_grid, row, col, num):
                        sudoku_grid[row][col] = num
                        solved = solve_board(sudoku_grid)  # Recursive call
                        if solved:
                            return sudoku_grid
                        sudoku_grid[row][col] = None  # Backtrack
                return None  # Trigger backtracking if no number works
    return sudoku_grid  # Return solved grid if no empty cells remain


def count_solutions(sudoku_grid):
    solution_count = [0]  # Mutable container to keep track of solutions

    def backtrack_count(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] is None:
                    for num in range(1, 10):
                        if is_valid_placement(grid, row, col, num):
                            grid[row][col] = num
                            backtrack_count(grid)
                            grid[row][col] = None  # Backtrack
                    return  # Return early after exploring this branch
        solution_count[0] += 1

    backtrack_count(deepcopy(sudoku_grid))  # Use a copy to avoid modifying the original
    return solution_count[0]

if __name__ == "__main__":
    # Example board
    sudoku_grid = [
        [5, 3, None, None, 7, None, None, None, None],
        [6, None, None, 1, 9, 5, None, None, None],
        [None, 9, 8, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9],
    ]

    print("Original Board:")
    from .generator import display_board_terminal
    display_board_terminal(sudoku_grid)

    # Check solutions
    solutions = count_solutions(sudoku_grid)
    if solutions == 0:
        print("The Sudoku has no solution.")
    elif solutions == 1:
        print("The Sudoku has a unique solution.")
        solve_board(sudoku_grid)
        print("Solved Board:")
        display_board_terminal(sudoku_grid)
    else:
        print(f"The Sudoku has {solutions} solutions.")
