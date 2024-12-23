#ifndef SOLVER_H
#define SOLVER_H

#include <array>

typedef std::array<std::array<int, 9>, 9> SudokuGrid;

bool isValidPlacement(SudokuGrid& grid, int row, int col, int num);
bool solveBoard(SudokuGrid& grid);
int countSolutions(SudokuGrid& grid);
SudokuGrid solveBoardReturn(SudokuGrid grid);

#endif
