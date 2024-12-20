#################################################################
# gui.py
#################################################################

import time
from datetime import datetime, timedelta
import pygame
import os
import re
import json

from display.theme import THEMES

KEY_TO_NUMBER = {
    pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3,
    pygame.K_4: 4, pygame.K_5: 5, pygame.K_6: 6,
    pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9,
    pygame.K_KP1: 1, pygame.K_KP2: 2, pygame.K_KP3: 3,
    pygame.K_KP4: 4, pygame.K_KP5: 5, pygame.K_KP6: 6,
    pygame.K_KP7: 7, pygame.K_KP8: 8, pygame.K_KP9: 9,
}

WIDTH = 600
HEIGHT = 720

dx = WIDTH // 9
dy = HEIGHT // 9

DEFAULT_POSITIONS = {
    "check_button":   [1.0 * dx,    610,    1.5 * dx,     50],
    "time_display":   [3.27 * dx,   610,    2.5 * dx,     50],
    "refresh_button": [6.5 * dx,    610,    1.66 * dx,    50],
    "hint_button":    [6.5 * dx,    665,    1.66 * dx,    50],
}

def theme_to_colors(theme):
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    return THEMES[theme]

class SudokuDisplay:
    def __init__(self, width=WIDTH, height=HEIGHT, sudoku_grid=None, solved_sudoku_grid=None,
                 given_cells=None, theme="Classic", renderer="screen", config_file="button_positions.json"):

        # Initialize pygame
        if renderer == "screenless":
            os.environ["SDL_VIDEODRIVER"] = "dummy"  # Dummy driver for headless mode
        pygame.init()

        self.width = width
        self.height = height
        self.cell_size = self.width // 9
        self.renderer = renderer
        self.config_file = config_file

        # Determine the rendering target
        if renderer == "screen":
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Sudoku")
        elif renderer == "screenless":
            self.screen = pygame.Surface((self.width, self.height))
        else:
            raise ValueError(f"Unknown renderer type: {renderer}")

        # Font settings
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 40)

        # Game state
        self.running = True
        self.sudoku_grid = sudoku_grid if sudoku_grid else \
            [[None for _ in range(9)] for _ in range(9)]
        self.given_cells = given_cells if given_cells else \
            [(row, col) for row in range(9) for col in range(9) 
             if self.sudoku_grid[row][col] is not None]
        
        # Varables for Hinting
        self.solved_sudoku_grid = solved_sudoku_grid
        self.showing_hint = False
        self.hint_start_time = None

        # Variables for user interaction
        self.selected_cell = None
        self.hovered_cell = None
        self.events_list = []

        # Colors and theme
        self.theme = theme
        self.colors = theme_to_colors(self.theme)

        # Timer and game state
        self.start_time = time.time()
        self.solved = False
        self.message = ""

        # Button positions
        self.load_positions()

        # Drag-and-drop variables
        self.editing_mode = False 
        self.message = "" if not self.editing_mode else "Editing"
        self.dragged_button = None
        self.drag_offset = (0, 0)

    def load_positions(self):
        try:
            with open(self.config_file, "r") as f:
                positions = DEFAULT_POSITIONS #json.load(f)
        except FileNotFoundError:
            positions = DEFAULT_POSITIONS

        self.check_button_rect = pygame.Rect(*positions["check_button"])
        self.refresh_button_rect = pygame.Rect(*positions["refresh_button"])
        self.hint_button_rect = pygame.Rect(*positions["hint_button"])
        self.time_rect = pygame.Rect(*positions["time_display"])

    def save_positions(self):
        positions = {
            "check_button": [*self.check_button_rect],
            "time_display": [*self.time_rect],
            "refresh_button": [*self.refresh_button_rect],
            "hint_button": [*self.hint_button_rect],
        }
        with open(self.config_file, "w") as f:
            json.dump(positions, f)

    def draw_grid(self):
        for i in range(10):
            line_width = 4 if i % 3 == 0 else 1
            color = self.colors["bold_grid"] if i % 3 == 0 else \
                self.colors["grid"]
            pygame.draw.line(
                self.screen,
                color,
                (0, i * self.cell_size),
                (self.width, i * self.cell_size),
                line_width,
            )
            pygame.draw.line(
                self.screen,
                color,
                (i * self.cell_size, 0),
                (i * self.cell_size, self.width),
                line_width,
            )


    def is_hint_active(self):
        # Ensure this function always returns a boolean
        if self.showing_hint and self.hint_start_time is not None:
            if time.time() - self.hint_start_time < 2:
                return True
            else:
                # Reset hint state after 2 seconds
                self.showing_hint = False
                self.hint_start_time = None
        return False


    def draw_numbers(self):
        # Show the solved numbers when hint is active else show user numbers
        current_grid = self.solved_sudoku_grid if self.is_hint_active() else self.sudoku_grid


        for row in range(9):
            for col in range(9):
                val = current_grid[row][col]
                if val is None:
                    continue
                color = self.colors["text_given"] if (row, col) in \
                    self.given_cells else self.colors["text_user"]
                text_surf = self.font.render(str(val), True, color)
                
                # Get the rectangle of the text surface
                text_rect = text_surf.get_rect()
                
                # Center the text rectangle within the cell
                text_rect.center = (
                    col * self.cell_size + self.cell_size // 2,
                    row * self.cell_size + self.cell_size // 2
                )
                
                # Draw the text
                self.screen.blit(text_surf, text_rect)

    def draw_highlights(self):
        for row in range(9):
            for col in range(9):
                rect = pygame.Rect(col * self.cell_size,
                                   row * self.cell_size,
                                   self.cell_size,
                                   self.cell_size)
                if (row, col) in self.given_cells:
                    pygame.draw.rect(self.screen,
                                     self.colors["highlight_given"],
                                     rect)
                elif self.sudoku_grid[row][col] is not None:
                    pygame.draw.rect(self.screen,
                                     self.colors["highlight_user"],
                                     rect)
        if self.hovered_cell:
            row, col = self.hovered_cell
            rect = pygame.Rect(col * self.cell_size,
                               row * self.cell_size,
                               self.cell_size,
                               self.cell_size)
            pygame.draw.rect(self.screen, self.colors["hover"], rect,
                             border_radius=8)

        if self.selected_cell:
            row, col = self.selected_cell
            rect = pygame.Rect(col * self.cell_size,
                               row * self.cell_size,
                               self.cell_size,
                               self.cell_size)
            pygame.draw.rect(self.screen, self.colors["selected"], rect,
                             border_radius=8)

    def draw_buttons(self):
        # Draw Check Button
        pygame.draw.rect(self.screen, self.colors["button_bg"],
                        self.check_button_rect, border_radius=10)
        check_text = self.button_font.render("Check", True,
                                            self.colors["button_text"])
        cx = self.check_button_rect.x + \
            (self.check_button_rect.width - check_text.get_width()) // 2
        cy = self.check_button_rect.y + \
            (self.check_button_rect.height - check_text.get_height()) // 2
        self.screen.blit(check_text, (cx, cy))

        # Draw Refresh Button with Unicode Symbol
        pygame.draw.rect(self.screen, self.colors["button_bg"],
                        self.refresh_button_rect, border_radius=10)
        refresh_text = self.button_font.render("Refresh", True, self.colors["button_text"])  # Refresh symbol
        rx = self.refresh_button_rect.x + \
            (self.refresh_button_rect.width - refresh_text.get_width()) // 2
        ry = self.refresh_button_rect.y + \
            (self.refresh_button_rect.height - refresh_text.get_height()) // 2
        self.screen.blit(refresh_text, (rx, ry))

        # Draw Hint Button with Unicode Symbol
        pygame.draw.rect(self.screen, self.colors["button_bg"],
                        self.hint_button_rect, border_radius=10)
        hint_text = self.button_font.render("Hint!", True, self.colors["button_text"])  # Light bulb symbol
        hx = self.hint_button_rect.x + \
            (self.hint_button_rect.width - hint_text.get_width()) // 2
        hy = self.hint_button_rect.y + \
            (self.hint_button_rect.height - hint_text.get_height()) // 2
        self.screen.blit(hint_text, (hx, hy))

        # Highlight draggable areas in editing mode
        if self.editing_mode:
            for rect in [self.check_button_rect, self.refresh_button_rect,
                        self.hint_button_rect, self.time_rect]:
                pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)

    def draw_timer(self):
        elapsed = max(0, time.time() - self.start_time)
        if self.solved:
            elapsed = self.end_time - self.start_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        timer_text = f"Time: {mins:02d}:{secs:02d}"
        
        timer_surf = self.button_font.render(timer_text, True,
                                         self.colors["message_text"])
        self.screen.blit(timer_surf, (self.time_rect.x + 10,
                                  self.time_rect.y + 10))

    def draw_message(self, win_loss_text=True, test_theme_mode = False):
        if self.message and not test_theme_mode:
            msg_color = self.colors["message_text"] if not win_loss_text else self.colors["win_text"] if self.solved else self.colors["loss_text"]
            msg_surf = self.button_font.render(self.message, True, msg_color)
            mx = (self.width - msg_surf.get_width()) // 2
            my = 670
            self.screen.blit(msg_surf, (mx, my))
        
        elif test_theme_mode:
            label_surf = self.button_font.render('Theme: ', True, self.colors["win_text"])
            name_surf = self.button_font.render(self.theme, True, self.colors["loss_text"])

            # Calculate positions for combined text
            combined_width = label_surf.get_width() + name_surf.get_width()
            label_x = (self.width - combined_width) // 2
            label_y = 670
            name_x = label_x + label_surf.get_width()
            
            self.screen.blit(label_surf, (label_x, label_y))
            self.screen.blit(name_surf, (name_x, label_y))

    def draw_screen(self, test_theme_mode=False):
        self.screen.fill(self.colors["background"])
        self.draw_highlights()
        self.draw_grid()
        self.draw_numbers()
        self.draw_buttons()
        self.draw_timer()
        self.draw_message(test_theme_mode=test_theme_mode)

        if self.renderer == "screen":
            pygame.display.flip()

    def handle_events(self):
        self.events_list = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.events_list.append(('QUIT', None))

            if self.is_hint_active():
                # Still update things like selected cell with mouse clicks if desired,
                # but let's block button clicks:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # Only let user select cells, do not trigger CHECK/REFRESH/HINT events
                    if y < self.width: 
                        col = x // self.cell_size
                        row = y // self.cell_size
                        self.selected_cell = (row, col)
                        self.events_list.append(('CELL_CLICK', (row, col)))
                continue

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if self.editing_mode:
                    # Drag-and-drop functionality in editing mode
                    if self.check_button_rect.collidepoint(x, y):
                        self.dragged_button = "check"
                        self.drag_offset = (x - self.check_button_rect.x, y - self.check_button_rect.y)
                    elif self.refresh_button_rect.collidepoint(x, y):
                        self.dragged_button = "refresh"
                        self.drag_offset = (x - self.refresh_button_rect.x, y - self.refresh_button_rect.y)
                    elif self.hint_button_rect.collidepoint(x, y):
                        self.dragged_button = "hint"
                        self.drag_offset = (x - self.hint_button_rect.x, y - self.hint_button_rect.y)
                    elif self.time_rect.collidepoint(x, y):
                        self.dragged_button = "time"
                        self.drag_offset = (x - self.time_rect.x, y - self.time_rect.y)
                else:
                    # Handle button clicks in normal mode
                    if self.check_button_rect.collidepoint(x, y):
                        self.events_list.append(('CHECK_BUTTON', None))
                    elif self.refresh_button_rect.collidepoint(x, y):
                        self.events_list.append(('REFRESH_BUTTON', None))
                    elif self.hint_button_rect.collidepoint(x, y):
                        self.events_list.append(('HINT_BUTTON', None))

                # Handle clicks on the Sudoku grid
                if y < self.width:  # Only register clicks within the grid area
                    col = x // self.cell_size
                    row = y // self.cell_size
                    self.selected_cell = (row, col)
                    self.events_list.append(('CELL_CLICK', (row, col)))

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.editing_mode and self.dragged_button:
                    # Save button positions after dragging
                    self.dragged_button = None
                    self.save_positions()

            elif event.type == pygame.MOUSEMOTION and self.editing_mode:
                # Update button positions during drag
                x, y = event.pos
                if self.dragged_button == "check":
                    self.check_button_rect.x = x - self.drag_offset[0]
                    self.check_button_rect.y = y - self.drag_offset[1]
                elif self.dragged_button == "refresh":
                    self.refresh_button_rect.x = x - self.drag_offset[0]
                    self.refresh_button_rect.y = y - self.drag_offset[1]
                elif self.dragged_button == "hint":
                    self.hint_button_rect.x = x - self.drag_offset[0]
                    self.hint_button_rect.y = y - self.drag_offset[1]
                elif self.dragged_button == "time":
                    self.time_rect.x = x - self.drag_offset[0]
                    self.time_rect.y = y - self.drag_offset[1]

            elif event.type == pygame.KEYDOWN and not self.solved:
                # Handle keyboard events
                if event.key in KEY_TO_NUMBER:
                    number = KEY_TO_NUMBER[event.key]
                    self.events_list.append(('NUMBER', number))
                elif event.key == pygame.K_u:
                    self.events_list.append(('UNDO', None))
                elif event.key == pygame.K_r:
                    self.events_list.append(('REDO', None))

                # Handle arrow key navigation for the grid
                if self.selected_cell:
                    row, col = self.selected_cell
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        col = max(0, col - 1)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        col = min(8, col + 1)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        row = max(0, row - 1)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        row = min(8, row + 1)
                    self.selected_cell = (row, col)
                    self.events_list.append(('GRID_MOVE', (row, col)))

    def show_hint(self):
        # Called when the hint button is pressed
        self.showing_hint = True
        self.hint_start_time = time.time()

    def run_once(self):
        if not self.running:
            return
        self.handle_events()
        self.draw_screen()

    def update(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        self.draw_screen()

    def set_message(self, text):
        self.message = text

    def set_solved(self):
        self.solved = True
        self.end_time = time.time()

    def reset_timer(self):
        self.start_time = time.time()

    def quit(self):
        self.running = False
        pygame.quit()

    def save_to_png(self, output_path):
        directory = os.path.dirname(output_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the image
        pygame.image.save(self.screen, output_path)
        print(f"Board saved as PNG at {output_path}")

if __name__ == "__main__":
    sudoku_grid = [
        [5, None, None, None, 7, None, None, None, None],
        [None, 5, None, 1, 9, 5, None, None, None],
        [None, None, None, None, None, None, None, 6, None],
        [8, None, None, None, 6, None, None, None, 3],
        [4, None, None, 8, None, 3, None, None, 1],
        [7, None, None, None, 2, None, None, None, 6],
        [None, 6, None, None, None, None, 2, 8, None],
        [None, None, None, 4, 1, 9, None, None, 5],
        [None, None, None, None, 8, None, None, 7, 9],
    ]
    given_cells = [(row, col) for row in range(9) for col in range(9)
                   if sudoku_grid[row][col] is not None]


    for theme in THEMES:
        sanitized_theme = re.sub(r"[^\w]", "_", theme)
        display = SudokuDisplay(sudoku_grid=sudoku_grid, 
                                given_cells = given_cells,
                                theme=theme,
                                renderer="screenless")
        
        display.hovered_cell =(0,0)
        display.selected_cell= (1,1)
        display.sudoku_grid[2][2] = 9

        custom_start_time = datetime.now() - timedelta(minutes=5, seconds=30)  # Start 5m30s ago
        display.start_time = custom_start_time.timestamp()

        display.draw_screen(test_theme_mode=True)
        display.save_to_png(f"./images/themes/{sanitized_theme}.png")