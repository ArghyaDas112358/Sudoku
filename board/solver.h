#ifndef SOLVER_H
#define SOLVER_H

#include <vector>

bool isValidPlacement(std::vector<std::vector<int>>& grid, int row, int col, int num);
bool solveBoard(std::vector<std::vector<int>>& grid);
int countSolutions(std::vector<std::vector<int>>& grid);

#endif
