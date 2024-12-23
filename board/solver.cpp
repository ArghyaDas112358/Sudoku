// board/solver.cpp

#include <vector>
#include <iostream>
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
                for (int num = 1; num <= 9; num++) {
                    if (isValidPlacement(grid, row, col, num)) {
                        grid[row][col] = num; // Place the number
                        if (solveBoard(grid)) {
                            return true; // Solved
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

// Returns the solved board (in-place by reference solving is having problem)
std::vector<std::vector<int>> solveBoardReturn(std::vector<std::vector<int>> grid) {
    solveBoard(grid);
    return grid;
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


void printGrid(const std::vector<std::vector<int>>& grid) {
    for (const auto& row : grid) {
        for (int cell : row) {
            if (cell == 0) {
                std::cout << ". ";
            } else {
                std::cout << cell << " ";
            }
        }
        std::cout << std::endl;
    }
}

int main() {
    // Example Sudoku grid
    std::vector<std::vector<int>> grid = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9},
    };

    std::cout << "Original grid:" << std::endl;
    printGrid(grid);

    // Test the solver
    if (solveBoard(grid)) {
        std::cout << "Solved grid:" << std::endl;
        printGrid(grid);
    } else {
        std::cout << "No solution found." << std::endl;
    }

    // Test the solution counter
    std::vector<std::vector<int>> gridForCount = grid; // Reset grid for counting
    int solutions = countSolutions(gridForCount);
    std::cout << "Number of solutions: " << solutions << std::endl;

    return 0;
}