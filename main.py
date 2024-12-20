#################################################################
# main.py
#################################################################

import time
import copy

from display.gui import SudokuDisplay
from board.generator import generate_board, generate_board_with_one_solution, display_board_terminal
from board.validator import is_valid_placement, is_board_valid, is_board_complete
from board.solver import count_solutions, solve_board


def main(theme = "Classic", empty_cells_ratio = 0.7):
    # Generate board

    # sudoku_grid = generate_board(empty_cells_ratio=empty_cells_ratio)
    print("Generating board with one solution...")
    sudoku_grid = generate_board_with_one_solution(empty_cells_ratio=empty_cells_ratio)
    given_cells = [(row, col) for row in range(9) for col in range(9)
                   if sudoku_grid[row][col] is not None]
    
    sudoku_grid_copy = copy.deepcopy(sudoku_grid)
    assert count_solutions(sudoku_grid_copy) == 1
    solved_sudoku_grid = solve_board(sudoku_grid_copy)

    print("Original Board:")
    display_board_terminal(sudoku_grid)
    print("Solved Board:")
    display_board_terminal(solved_sudoku_grid)

    display = SudokuDisplay(sudoku_grid=sudoku_grid,
                            solved_sudoku_grid=solved_sudoku_grid,
                            given_cells=given_cells,
                            theme=theme,
                            renderer="screen")

    undo_stack = []
    redo_stack = []

    while display.running:
        display.run_once()

        for event_type, data in display.events_list:
            if event_type == 'QUIT':
                display.quit()

            elif event_type == 'CELL_CLICK':
                display.selected_cell = data

            elif event_type == 'NUMBER' and display.selected_cell:
                if not display.solved:
                    row, col = display.selected_cell
                    if is_valid_placement(sudoku_grid, row, col, data):
                        old_val = sudoku_grid[row][col]
                        undo_stack.append((row, col, old_val, data))
                        redo_stack.clear()
                        sudoku_grid[row][col] = data
                        display.update(sudoku_grid)

            elif event_type == 'UNDO':
                if undo_stack and not display.solved:
                    row, col, old_val, new_val = undo_stack.pop()
                    redo_stack.append((row, col, new_val, old_val))
                    sudoku_grid[row][col] = old_val
                    display.update(sudoku_grid)

            elif event_type == 'REDO':
                if redo_stack and not display.solved:
                    row, col, new_val, old_val = redo_stack.pop()
                    undo_stack.append((row, col, old_val, new_val))
                    sudoku_grid[row][col] = new_val
                    display.update(sudoku_grid)

            elif event_type == 'CHECK_BUTTON':
                # Check if board is complete and valid
                if is_board_complete(sudoku_grid) and \
                   is_board_valid(sudoku_grid):
                    # Win condition
                    display.set_message("You Win!")
                    display.set_solved()
                else:
                    display.set_message("Not Correct!")

            elif event_type == 'REFRESH_BUTTON':
                # Generate a new game
                print("Refreshing board...")
                print("Regenerating board with one solution...")
                # sudoku_grid = generate_board(empty_cells_ratio=empty_cells_ratio)
                sudoku_grid = generate_board_with_one_solution(empty_cells_ratio=empty_cells_ratio)
                given_cells = [(r, c) for r in range(9)
                               for c in range(9)
                               if sudoku_grid[r][c] is not None]
                
                sudoku_grid_copy = copy.deepcopy(sudoku_grid)
                assert count_solutions(sudoku_grid_copy) == 1
                solved_sudoku_grid = solve_board(sudoku_grid_copy)

                print("Original Board:")
                display_board_terminal(sudoku_grid)
                print("Solved Board:")
                display_board_terminal(solved_sudoku_grid)

                display.sudoku_grid = sudoku_grid
                display.given_cells = given_cells
                display.solved_sudoku_grid = solved_sudoku_grid
                display.selected_cell = None
                display.solved = False
                display.set_message("")
                undo_stack.clear()
                redo_stack.clear()
                display.reset_timer()
                display.update(sudoku_grid)
            
            elif event_type == 'HINT_BUTTON':
                # Show hint for 2 seconds by displaying the solved board
                display.show_hint()

        time.sleep(0.05)

def test_run(empty_cells_ratio= 0.3):
    print("Original Board:")
    sudoku_grid = generate_board(empty_cells_ratio=empty_cells_ratio)
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


if __name__ == "__main__":
    main(empty_cells_ratio=0.3)
    # test_run(empty_cells_ratio=0.3)

