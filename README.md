# Sudoku

A comprehensive Sudoku project that includes:
 - **Board Generation**
 - **Board Validation**
 - **Board Solver** (C++ bindings via pybind11)
 - **GUI** (PyGame)


## Screenshots

### Classic Theme

![Classic Theme](https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Classic.png?raw=true)   

### Solar Flare Theme

![Golden Classic Theme](https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Solar_Flare.png?raw=true)

## Ice Cold Theme

![Ice Cold Theme](https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Ice_Cold.png?raw=true)

### Dark Theme

![Dark Theme](https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Dark_Mode.png?raw=true)




## Project Structure

```bash
.
├── board
│   ├── generator.py       # Functions to generate sudoku boards
│   ├── __init__.py        # Python package initializer
│   ├── Makefile           # Builds the C++ shared library
│   ├── solver.cpp         # C++ solver implementation
│   ├── solver.h           # C++ solver header
│   ├── solver.py          # Python solver (falls back to Python logic if needed)
│   ├── validator.py       # Validation logic for rows, columns, subgrids
│   └── wrapper.cpp        # C++ to Python binding using Pybind11
├── build.py               # Python script to automate building the shared library
├── display
│   ├── gui.py             # GUI logic using Pygame
│   ├── __init__.py        # Python package initializer
│   └── theme.py           # Theming for the GUI
├── main.py                # Main script to run the Sudoku application
└── README.md              # Project documentation
```


## Installation

1. Clone the GitHub repository:
 ```bash     
   git clone https://github.com/ArghyaDas112358/Sudoku.git
   cd Sudoku
 ```

2. Install Python dependencies:
 ```bash
   pip install -r requirements.txt
 ```
3. Build the C++ shared library:
   - Option A: Use the provided `build.py` script:
 ```bash
     python build.py
 ```
   - Option B: Manually use the Makefile:
 ```bash
     cd board
     make
     cd ..
 ```

 This will generate the shared library `board/solver_lib.so` in the `board` directory.


## Usage
Simply run:

```bash
python main.py
```
This launches the Sudoku board in both the terminal and the Pygame GUI.

### GUI Controls
 - **Navigation**: Use the arrow keys or mouse to select cells.
 - **Checking**: The Check button verifies the current entries.
 - **Refresh**: The Refresh button resets the board.
 - **Hint**: The Hint button, when pressed for 2 seconds, reveals a solution for the selected cell.


### Theming
The GUI’s appearance is governed by the `theme.py` file, which contains a dictionary of possible themes. You can modify or add themes in `THEMES` within `theme.py`. By default, the `"Classic"` theme is used.

To preview themes:

```bash
python -m display.gui
```
Screenshots of the current board will be saved to the `images/themes` directory.

## Contributing

Pull requests are welcome! 
For significant changes, please open an issue first to discuss your ideas and proposed modifications.

## License

This project is licensed under the MIT License.

---

**Enjoy Sudoku!** :smile:


