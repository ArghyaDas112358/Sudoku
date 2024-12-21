#include "solver.h"

// Check if placing `num` in `grid[row][col]` is valid
bool isValidPlacement(std::vector<std::vector<int>>& grid, int row, int col, int num) {
    for (int i = 0; i < 9; i++) {
        if (grid[row][i] == num || grid[i][col] == num) {
            return false;
        }
    }
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = startRow; i < startRow + 3; i++) {
        for (int j = startCol; j < startCol + 3; j++) {
            if (grid[i][j] == num) {
                return false;
            }
        }
    }
    return true;
}

bool solveBoard(std::vector<std::vector<int>>& grid) {
    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (grid[row][col] == 0) { // If cell is empty
                for (int num = 1; num <= 9; num++) { // Try numbers 1-9
                    if (isValidPlacement(grid, row, col, num)) {
                        grid[row][col] = num;
                        if (solveBoard(grid)) {
                            return true;
                        }
                        grid[row][col] = 0; // Backtrack
                    }
                }
                return false; // No valid number found
            }
        }
    }
    return true; // Board is solved
}

int countSolutions(std::vector<std::vector<int>>& grid) {
    int solutionCount = 0;

    for (int row = 0; row < 9; row++) {
        for (int col = 0; col < 9; col++) {
            if (grid[row][col] == 0) { // If cell is empty
                for (int num = 1; num <= 9; num++) { // Try numbers 1-9
                    if (isValidPlacement(grid, row, col, num)) {
                        grid[row][col] = num;
                        solutionCount += countSolutions(grid); // Recursive call
                        grid[row][col] = 0; // Backtrack
                    }
                }
                return solutionCount; // Return after exploring this branch
            }
        }
    }
    return 1; // If no empty cells, we found a solution
}