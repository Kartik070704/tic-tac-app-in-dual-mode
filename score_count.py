import tkinter as tk

class ScoreCount:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def update_score(self, winner):
        if winner == "X":
            self.player1_score += 1
        elif winner == "O":
            self.player2_score += 1

    def display_score(self, root):
        score_label = tk.Label(root, text=f"Player 1 (X): {self.player1_score} | Player 2 (O): {self.player2_score}",
                               font=("Helvetica", 16), bg="#1F2833", fg="#C5C6C7")
        score_label.pack(pady=10)
