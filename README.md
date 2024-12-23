# 🧩 Sudoku

A comprehensive Sudoku project that includes:
 - **Board Generation**
 - **Board Validation**
 - **Board Solver** (C++ bindings via pybind11)
 - **GUI** (PyGame)


## 📸 Screenshots

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Classic.png?raw=true" alt="Classic Theme" width="150"/>
        <br>
        <strong>Classic Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Solar_Flare.png?raw=true" alt="Solar Flare Theme" width="150"/>
        <br>
        <strong>Solar Flare Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Ice_Cold.png?raw=true" alt="Ice Cold Theme" width="150"/>
        <br>
        <strong>Ice Cold Theme</strong>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Dark_Mode.png?raw=true" alt="Dark Mode Theme" width="150"/>
        <br>
        <strong>Dark Mode Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Forest_Whisper.png?raw=true" alt="Forest Whisper Theme" width="150"/>
        <br>
        <strong>Forest Whisper Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Retro_Neon.png?raw=true" alt="Retro Neon Theme" width="150"/>
        <br>
        <strong>Retro Neon Theme</strong>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Golden_Classic.png?raw=true" alt="Golden Classic Theme" width="150"/>
        <br>
        <strong>Golden Classic Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Midnight_Bliss.png?raw=true" alt="Midnight Bliss Theme" width="150"/>
        <br>
        <strong>Midnight Bliss Theme</strong>
      </td>
      <td align="center">
        <img src="https://github.com/ArghyaDas112358/Sudoku/blob/main/images/themes/Autumn_Leaves.png?raw=true" alt="Autumn Leaves Theme" width="150"/>
        <br>
        <strong>Autumn Leaves Theme</strong>
      </td>
    </tr>
  </table>
</div>


There are various other themes available namely: Cyberpunk, Ocean Breeze, Peach Blossom, Sunset Glow, Candy Crush, Winter Frost etc.


## 📁 Project Structure

```bash
.
├── build.py                # Script to build the shared library
├── LICENSE                 # Licensing information
├── main.py                 # Entry point or testing script
├── README.md               # Project description
├── requirements.txt        # Project dependencies
├── setup.py                # For packaging and distribution
└── src
    ├── board               # Core logic and integration
    │   ├── generator.py    # Generates Sudoku puzzles
    │   ├── __init__.py     # Marks the module
    │   ├── solver.py       # Solver logic, uses `solver_lib.so`
    │   └── validator.py    # Validation logic
    ├── cpp                 # C++ source files for `solver_lib.so`
    │   ├── include
    │   │   └── solver.h    # Header file for C++ logic
    │   ├── Makefile        # Makefile to build `solver_lib.so`
    │   └── src
    │       ├── solver.cpp  # Solver implementation
    │       └── wrapper.cpp # Pybind11 wrapper
    ├── display             # GUI and visual elements
    │   ├── gui.py          # Pygame-based GUI
    │   ├── __init__.py     # Marks the module
    │   └── theme.py        # Handles visual theming
    └── __init__.py         # Marks `src` as a package
```


## 🛠️ Installation

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


## 🚀 Usage
Simply run:

```bash
python main.py
```
This launches the Sudoku board in both the terminal and the Pygame GUI.

### 🎮 GUI Controls
 - **Navigation**: Use the arrow keys or mouse to select cells.
 - **Checking**: The Check button verifies the current entries.
 - **Refresh**: The Refresh button resets the board.
 - **Hint**: The Hint button, when pressed for 2 seconds, reveals a solution for the selected cell.


### 🎨 Theming
The GUI’s appearance is governed by the `theme.py` file, which contains a dictionary of possible themes. You can modify or add themes in `THEMES` within `theme.py`. By default, the `"Classic"` theme is used.

To preview themes:

```bash
python -m display.gui
```
Screenshots of the current board will be saved to the `images/themes` directory.

## 🤝 Contributing

Pull requests are welcomed! 
For significant changes, please open an issue first to discuss your ideas and proposed modifications.

## 📜 License

This project is licensed under the MIT License.

---

**Enjoy Sudoku!** :smile:


