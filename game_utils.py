import tkinter as tk
from tkinter import messagebox
from score_count import ScoreCount

class Game:
    def __init__(self, grid_size, ai_mode=False):
        self.grid_size = grid_size
        self.ai_mode = ai_mode
        self.current_player = "X"
        self.board = [""] * (grid_size * grid_size)
        self.buttons = []
        self.score_counter = ScoreCount()

    def setup_grid(self):
        root = tk.Tk()
        root.title("Tic Tac Toe")
        root.geometry("500x700")
        root.configure(bg="#1F2833")

        turn_label = tk.Label(root, text=f"Player 1 (X)'s Turn", font=("Helvetica", 16, "italic"), bg="#1F2833", fg="#C5C6C7")
        turn_label.pack(pady=10)
        self.score_counter.display_score(root)

        grid_frame = tk.Frame(root, bg="#1F2833")
        grid_frame.pack(pady=20)

        for i in range(self.grid_size * self.grid_size):
            button = tk.Button(grid_frame, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i), bg="#0B0C10", fg="#C5C6C7", relief="solid", borderwidth=2)
            button.grid(row=i // self.grid_size, column=i % self.grid_size, padx=5, pady=5)
            self.buttons.append(button)

        reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 16, "bold"), command=self.reset_game, bg="#1F2833", fg="#66FCF1", width=15, relief="ridge")
        reset_button.pack(pady=10)

        root.mainloop()

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="#45A29E" if self.current_player == "X" else "#C5C6C7", bg="#4B4B4B")
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = []
        for i in range(self.grid_size):
            winning_combinations.append([i * self.grid_size + j for j in range(self.grid_size)])
            winning_combinations.append([j * self.grid_size + i for j in range(self.grid_size)])
        winning_combinations.append([i * self.grid_size + i for i in range(self.grid_size)])
        winning_combinations.append([i * self.grid_size + (self.grid_size - i - 1) for i in range(self.grid_size)])

        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return self.current_player
        return "Draw" if "" not in self.board else None

    def end_game(self, winner):
        if winner == "Draw":
            messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
        else:
            self.score_counter.update_score(winner)
            winning_player = "Player 1" if winner == "X" else "Player 2"
            messagebox.showinfo("Tic Tac Toe", f"Congratulations {winning_player}! You win!")

