#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "solver.h"  // Include the header file

namespace py = pybind11;

// Expose the isValidPlacement function
PYBIND11_MODULE(solver_lib, m) {  // Change the module name to "solver_lib"
    m.def("isValidPlacement", &isValidPlacement, 
          "Check if placing a number in the Sudoku grid is valid",
          py::arg("grid"), py::arg("row"), py::arg("col"), py::arg("num"));
}
