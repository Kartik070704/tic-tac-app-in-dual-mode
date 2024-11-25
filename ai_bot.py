import tkinter as tk
import random
from game_utils import Game

def start_ai_game(grid_size):
    game = Game(grid_size=grid_size, ai_mode=True)
    game.setup_grid()

def ai_move(game):
    best_score = -float('inf')
    best_move = None

    for move in game.get_empty_indices():
        game.make_move(move)
        score = minimax(game, 0, False)
        game.undo_move()

        if score > best_score:
            best_score = score
            best_move = move

    game.make_move(best_move)

def minimax(game, depth, is_maximizing):
    if game.is_game_over():
        return game.evaluate()

    if is_maximizing:
        best_score = -float('inf')
        for move in game.get_empty_indices():
            game.make_move(move)
            score = minimax(game, depth + 1, False)
            game.undo_move()
            best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for move in game.get_empty_indices():
            game.make_move(move)
            score = minimax(game, depth + 1, True)
            game.undo_move()
            best_score = min(score, best_score)
        return best_score