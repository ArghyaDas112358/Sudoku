#!/usr/bin/env python3

THEMES = {
    "Classic": {
        "background": (240, 240, 245),
        "grid": (180, 180, 200, 120),
        "bold_grid": (90, 90, 130),
        "text_given": (50, 50, 70),
        "text_user": (30, 100, 150),
        "hover": (220, 230, 245),
        "selected": (70, 140, 180),
        "highlight_given": (250, 240, 200),
        "highlight_user": (210, 240, 250),
        "button_bg": (70, 130, 180),
        "button_hover": (90, 150, 200),
        "button_text": (255, 255, 255),
        "message_text": (70, 70, 100),
        "timer_bg": (250, 250, 255),
        "win_text": (0, 128, 0),
        "loss_text": (255, 0, 0),
    },
    "Golden Classic": {
        "background": (245, 245, 235),
        "grid": (160, 160, 120),
        "bold_grid": (125, 100, 75),
        "text_given": (30, 30, 50),
        "text_user": (60, 60, 90),
        "hover": (230, 210, 180),
        "selected": (70, 90, 120),
        "highlight_given": (250, 240, 190),
        "highlight_user": (210, 240, 250),
        "button_bg": (200, 200, 200),
        "button_hover": (220, 220, 220),
        "button_text": (0, 0, 0),
        "message_text": (255, 0, 0),
        "timer_bg": (255, 255, 255),
        "win_text": (34, 139, 34),
        "loss_text": (220, 20, 60),
    },
    "Dark Mode": {
        "background": (30, 30, 30),
        "grid": (50, 50, 50, 120),
        "bold_grid": (100, 100, 100),
        "text_given": (255, 255, 255),
        "text_user": (200, 200, 200),
        "hover": (70, 70, 70),
        "selected": (90, 90, 90),
        "highlight_given": (60, 60, 60),
        "highlight_user": (80, 80, 80),
        "button_bg": (100, 100, 100),
        "button_hover": (120, 120, 120),
        "button_text": (255, 255, 255),
        "message_text": (255, 69, 0),
        "timer_bg": (40, 40, 40),
        "win_text": (50, 205, 50),
        "loss_text": (255, 69, 0),
    },
    "Ocean Breeze": {
        "background": (200, 240, 255),
        "grid": (150, 200, 220),
        "bold_grid": (70, 130, 180),
        "text_given": (0, 70, 140),
        "text_user": (0, 100, 180),
        "hover": (190, 230, 250),
        "selected": (150, 200, 220),
        "highlight_given": (180, 220, 250),
        "highlight_user": (150, 200, 230),
        "button_bg": (50, 150, 200),
        "button_hover": (70, 170, 220),
        "button_text": (255, 255, 255),
        "message_text": (0, 100, 180),
        "timer_bg": (240, 255, 255),
        "win_text": (0, 128, 128),
        "loss_text": (255, 69, 0),
    },
    "Forest Whisper": {
        "background": (220, 230, 220),
        "grid": (160, 180, 160),
        "bold_grid": (100, 130, 100),
        "text_given": (30, 60, 30),
        "text_user": (50, 80, 50),
        "hover": (200, 220, 200),
        "selected": (140, 180, 140),
        "highlight_given": (190, 220, 190),
        "highlight_user": (140, 180, 140),
        "button_bg": (100, 150, 100),
        "button_hover": (120, 170, 120),
        "button_text": (255, 255, 255),
        "message_text": (34, 139, 34),
        "timer_bg": (245, 255, 245),
        "win_text": (0, 128, 0),
        "loss_text": (255, 69, 0),
    },
    "Sunset Glow": {
        "background": (255, 240, 230),
        "grid": (255, 200, 150),
        "bold_grid": (255, 160, 90),
        "text_given": (120, 60, 30),
        "text_user": (140, 70, 40),
        "hover": (255, 220, 200),
        "selected": (255, 180, 120),
        "highlight_given": (255, 230, 180),
        "highlight_user": (255, 200, 150),
        "button_bg": (240, 140, 90),
        "button_hover": (255, 160, 100),
        "button_text": (255, 255, 255),
        "message_text": (255, 99, 71),
        "timer_bg": (255, 245, 240),
        "win_text": (255, 69, 0),
        "loss_text": (255, 0, 0),
    },
    "Retro Neon": {
        "background": (20, 20, 30),
        "grid": (40, 40, 60),
        "bold_grid": (60, 0, 100),
        "text_given": (255, 0, 255),
        "text_user": (0, 255, 255),
        "hover": (70, 70, 100),
        "selected": (100, 0, 200),
        "highlight_given": (100, 0, 100),
        "highlight_user": (0, 100, 100),
        "button_bg": (50, 0, 150),
        "button_hover": (70, 0, 200),
        "button_text": (255, 255, 255),
        "message_text": (255, 0, 255),
        "timer_bg": (40, 40, 50),
        "win_text": (0, 255, 0),
        "loss_text": (255, 0, 0),
    },
    "Candy Crush": {
        "background": (255, 240, 250),
        "grid": (255, 200, 210),
        "bold_grid": (255, 140, 160),
        "text_given": (255, 80, 120),
        "text_user": (255, 50, 90),
        "hover": (255, 220, 230),
        "selected": (255, 170, 180),
        "highlight_given": (255, 190, 200),
        "highlight_user": (255, 150, 170),
        "button_bg": (255, 100, 130),
        "button_hover": (255, 130, 160),
        "button_text": (255, 255, 255),
        "message_text": (255, 69, 100),
        "timer_bg": (255, 245, 250),
        "win_text": (255, 0, 127),
        "loss_text": (220, 20, 60),
    },
    "Ice Cold": {
        "background": (230, 240, 255),
        "grid": (190, 210, 240),
        "bold_grid": (140, 180, 230),
        "text_given": (70, 90, 140),
        "text_user": (50, 70, 130),
        "hover": (200, 220, 250),
        "selected": (150, 180, 220),
        "highlight_given": (180, 200, 240),
        "highlight_user": (130, 160, 220),
        "button_bg": (100, 150, 200),
        "button_hover": (120, 170, 220),
        "button_text": (255, 255, 255),
        "message_text": (0, 120, 180),
        "timer_bg": (240, 250, 255),
        "win_text": (30, 144, 255),
        "loss_text": (255, 69, 0),
    },
    "Solar Flare": {
        "background": (255, 230, 200),
        "grid": (255, 170, 80),
        "bold_grid": (255, 120, 30),
        "text_given": (100, 50, 0),
        "text_user": (140, 70, 20),
        "hover": (255, 200, 140),
        "selected": (255, 150, 50),
        "highlight_given": (255, 180, 100),
        "highlight_user": (255, 140, 70),
        "button_bg": (200, 100, 50),
        "button_hover": (220, 120, 60),
        "button_text": (255, 255, 255),
        "message_text": (255, 69, 0),
        "timer_bg": (255, 245, 220),
        "win_text": (255, 69, 0),
        "loss_text": (139, 0, 0),
    },

    "Midnight Bliss": {
        "background": (15, 15, 45),
        "grid": (30, 30, 60),
        "bold_grid": (50, 50, 100),
        "text_given": (200, 200, 255),
        "text_user": (180, 180, 240),
        "hover": (45, 45, 75),
        "selected": (60, 60, 100),
        "highlight_given": (70, 70, 120),
        "highlight_user": (90, 90, 140),
        "button_bg": (80, 80, 160),
        "button_hover": (100, 100, 180),
        "button_text": (255, 255, 255),
        "message_text": (135, 206, 250),
        "timer_bg": (25, 25, 55),
        "win_text": (0, 191, 255),
        "loss_text": (255, 0, 0),
    },

    "Autumn Leaves": {
        "background": (255, 240, 220),
        "grid": (200, 140, 90),
        "bold_grid": (160, 100, 60),
        "text_given": (120, 60, 20),
        "text_user": (100, 50, 10),
        "hover": (230, 180, 130),
        "selected": (200, 150, 100),
        "highlight_given": (250, 200, 150),
        "highlight_user": (220, 170, 120),
        "button_bg": (180, 90, 40),
        "button_hover": (200, 110, 60),
        "button_text": (255, 255, 255),
        "message_text": (255, 69, 0),
        "timer_bg": (255, 245, 230),
        "win_text": (210, 105, 30),
        "loss_text": (139, 0, 0),
    },

    "Cyberpunk": {
        "background": (10, 10, 20),
        "grid": (50, 0, 80),
        "bold_grid": (100, 0, 160),
        "text_given": (255, 20, 147),
        "text_user": (30, 144, 255),
        "hover": (80, 0, 120),
        "selected": (120, 0, 200),
        "highlight_given": (160, 0, 240),
        "highlight_user": (20, 220, 200),
        "button_bg": (20, 20, 140),
        "button_hover": (40, 40, 200),
        "button_text": (255, 255, 255),
        "message_text": (0, 255, 127),
        "timer_bg": (20, 20, 50),
        "win_text": (50, 205, 50),
        "loss_text": (255, 0, 0),
    },

    "Peach Blossom": {
        "background": (255, 230, 240),
        "grid": (255, 190, 200),
        "bold_grid": (255, 150, 160),
        "text_given": (180, 70, 90),
        "text_user": (200, 50, 70),
        "hover": (255, 210, 220),
        "selected": (255, 170, 180),
        "highlight_given": (255, 200, 210),
        "highlight_user": (255, 160, 170),
        "button_bg": (255, 100, 120),
        "button_hover": (255, 130, 150),
        "button_text": (255, 255, 255),
        "message_text": (255, 20, 147),
        "timer_bg": (255, 245, 250),
        "win_text": (255, 105, 180),
        "loss_text": (255, 69, 0),
    },

    "Winter Frost": {
        "background": (240, 250, 255),
        "grid": (200, 230, 250),
        "bold_grid": (160, 200, 230),
        "text_given": (70, 130, 180),
        "text_user": (30, 100, 150),
        "hover": (220, 240, 255),
        "selected": (180, 210, 240),
        "highlight_given": (200, 220, 250),
        "highlight_user": (160, 190, 230),
        "button_bg": (80, 150, 200),
        "button_hover": (100, 170, 220),
        "button_text": (255, 255, 255),
        "message_text": (30, 144, 255),
        "timer_bg": (240, 250, 255),
        "win_text": (0, 191, 255),
        "loss_text": (255, 0, 0),
    }
}

