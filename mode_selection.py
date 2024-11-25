import tkinter as tk
from grid import start_3x3_game
from grid import start_4x4_game
from ai_bot import start_ai_game

def open_mode_selection(root, grid_size):
    root.withdraw()
    mode_window = tk.Toplevel()
    mode_window.title("Select Mode")
    mode_window.geometry("400x200")
    mode_window.configure(bg="#1F2833")

    mode_label = tk.Label(mode_window, text="Select Game Mode", font=("Helvetica", 16), bg="#1F2833", fg="#C5C6C7")
    mode_label.pack(pady=20)

    btn_pvp = tk.Button(mode_window, text="PvP Mode", font=("Helvetica", 14, "bold"),
                        command=lambda: start_game(mode_window, grid_size, "PvP"), bg="#1ABC9C", fg="white", width=10)
    btn_pvp.pack(pady=5)

    btn_ai = tk.Button(mode_window, text="AI Bot Mode", font=("Helvetica", 14, "bold"),
                       command=lambda: start_game(mode_window, grid_size, "AI"), bg="#1ABC9C", fg="white", width=10)
    btn_ai.pack(pady=5)

def start_game(mode_window, grid_size, mode):
    mode_window.withdraw()
    if mode == "PvP":
        if grid_size == 3:
            start_3x3_game()
        else:
            start_4x4_game()
    elif mode == "AI":
        start_ai_game(grid_size)

