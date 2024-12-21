#################################################################
# solver.py
#################################################################

from  board.solver_lib import solveBoard, countSolutions, isValidPlacement

def is_valid_placement(sudoku_grid, row, col, num):
    """
    Use the C++ implementation of isValidPlacement to validate placements.
    """
    converted_grid = [[cell if cell is not None else 0 for cell in row] for row in sudoku_grid]
    return isValidPlacement(converted_grid, row, col, num)

def solve_board(sudoku_grid):
    converted_grid = [[cell if cell is not None else 0 for cell in row] for row in sudoku_grid]
    solved = solveBoard(converted_grid) # Call the C++ function
    solved_grid = [[cell if cell != 0 else None for cell in row] for row in converted_grid]
    return solved_grid if solved else None

def count_solutions(sudoku_grid):
    converted_grid = [[cell if cell is not None else 0 for cell in row] for row in sudoku_grid]
    return countSolutions(converted_grid)

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
