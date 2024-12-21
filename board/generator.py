#################################################################
# generator.py
#################################################################

from board.validator import is_valid_placement, is_board_valid
from board.solver import count_solutions
import random

def fill_board_backtracking(sudoku_grid):
    """Fill the Sudoku board using backtracking."""
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] is None:
                for num in random.sample(range(1, 10), 9):  # Random order
                    if is_valid_placement(sudoku_grid, row, col, num):
                        sudoku_grid[row][col] = num
                        if fill_board_backtracking(sudoku_grid):  # Recursive call
                            return True
                        sudoku_grid[row][col] = None  # Backtrack
                return False  # Trigger backtracking
    return True

def remove_random_cell(sudoku_grid, empty_cells_ratio=0.7):
    # remove num_empty_cells (at random)
    num_empty_cells = int(empty_cells_ratio * 81)

    # Randomly remove `num_empty_cells` from the filled board
    all_positions = [(row, col) for row in range(9) for col in range(9)]
    empty_positions = random.sample(all_positions, num_empty_cells)

    for row, col in empty_positions:
        sudoku_grid[row][col] = None

    return sudoku_grid

def generate_board(empty_cells_ratio=0.3):
    sudoku_grid = [[None for _ in range(9)] for _ in range(9)]
    fill_board_backtracking(sudoku_grid)
    sudoku_grid = remove_random_cell(sudoku_grid, empty_cells_ratio)

    return sudoku_grid

def generate_board_with_one_solution(empty_cells_ratio=0.3):
    """Generate a Sudoku board with only one solution."""
    # Step 1: Generate a fully solved Sudoku board
    sudoku_grid = [[None for _ in range(9)] for _ in range(9)]
    fill_board_backtracking(sudoku_grid)

    # Step 2: Randomly remove cells while maintaining uniqueness
    all_positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(all_positions)  # Randomize order of positions

    for row, col in all_positions:
        # Backup the current value
        backup_value = sudoku_grid[row][col]
        sudoku_grid[row][col] = None  # Remove the cell

        # Check if the board still has exactly one solution
        if count_solutions(sudoku_grid) != 1:
            # Revert the change if it breaks uniqueness
            sudoku_grid[row][col] = backup_value

        # Stop if we've removed enough cells
        num_empty_cells = sum(cell is None for row in sudoku_grid for cell in row)
        if num_empty_cells >= int(empty_cells_ratio * 81):
            break

    return sudoku_grid



def display_board_terminal(sudoku_grid):
    """Display the Sudoku board with 3x3 grid separations."""
    for i, row in enumerate(sudoku_grid):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        row_display = ""
        for j, cell in enumerate(row):
            if j % 3 == 0:
                row_display += "| "
            row_display += f"{cell if cell != None else ' '} "
        row_display += "|"
        print(row_display)
    print("+-------+-------+-------+")

if __name__ == "__main__":
    # sudoku_grid = [
    #                 [5, 3, None, None, 7, None, None, None, None],
    #                 [6, None, None, 1, 9, 5, None, None, None],
    #                 [None, 9, 8, None, None, None, None, 6, None],
    #                 [8, None, None, None, 6, None, None, None, 3],
    #                 [4, None, None, 8, None, 3, None, None, 1],
    #                 [7, None, None, None, 2, None, None, None, 6],
    #                 [None, 6, None, None, None, None, 2, 8, None],
    #                 [None, None, None, 4, 1, 9, None, None, 5],
    #                 [None, None, None, None, 8, None, None, 7, 9]
    #       ]

    sudoku_grid = generate_board()
    display_board_terminal(sudoku_grid)
    print(f"Board is valid: {is_board_valid(sudoku_grid)}")
