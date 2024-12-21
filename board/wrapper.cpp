#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "solver.h"  // Include the header file

namespace py = pybind11;

PYBIND11_MODULE(solver_lib, m) {  // Module name is "solver_lib"
    m.def("isValidPlacement", &isValidPlacement, 
          "Check if placing a number in the Sudoku grid is valid",
          py::arg("grid"), py::arg("row"), py::arg("col"), py::arg("num"));

    m.def("solveBoard", &solveBoard, 
          "Solve the Sudoku board using backtracking",
          py::arg("grid"));

    m.def("countSolutions", &countSolutions, 
          "Count all possible solutions of the Sudoku board",
          py::arg("grid"));
}
