#################################################################
# validator.py
#################################################################

import os
import sys

# Dynamically add the `build` directory to the system path
BUILD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../build"))
if BUILD_DIR not in sys.path:
    sys.path.append(BUILD_DIR)

from solver_lib import isValidPlacement

def is_unique(numbers):
    """Check if the list contains unique numbers (ignoring None)."""
    nums = [num for num in numbers if num is not None]
    return len(nums) == len(set(nums))

def get_subgrid(sudoku_grid, row, col):
    """
    Get all numbers in the 3x3 subgrid containing the cell at (row, col).
    Returns a list of 9 numbers.
    """

    subgrid = []
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            subgrid.append(sudoku_grid[r][c])
    return subgrid

def is_board_with_valid_rows(sudoku_grid):
    for row in sudoku_grid:
        if not is_unique(row):
            return False
    return True

def is_board_with_valid_cols(sudoku_grid):
    for col in range(9):
        col_values = [sudoku_grid[row][col] for row in range(9)]
        if not is_unique(col_values):
            return False
    return True

def is_board_with_valid_subgrids(sudoku_grid):
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = get_subgrid(sudoku_grid, row, col)
            if not is_unique(subgrid):
                return False
    return True

def is_board_valid(sudoku_grid):
    return is_board_with_valid_rows(sudoku_grid) and \
           is_board_with_valid_cols(sudoku_grid) and \
           is_board_with_valid_subgrids(sudoku_grid)


def is_board_complete(sudoku_grid): # No None present
    return all(cell is not None for row in sudoku_grid for cell in row)


def is_valid_placement(sudoku_grid, row, col, num):
    """
    Use the C++ implementation of isValidPlacement to validate placements.
    """
    converted_grid = [[cell if cell is not None else 0 for cell in row] for row in sudoku_grid]
    return isValidPlacement(converted_grid, row, col, num)

