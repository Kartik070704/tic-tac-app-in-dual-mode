import tkinter as tk
from game_utils import Game

def start_3x3_game():
    game = Game(grid_size=3)
    game.setup_grid()

def start_4x4_game():
    game = Game(grid_size=4)
    game.setup_grid()