import tkinter as tk
from tkinter import messagebox

# Game settings
colors = {
    "X": "#45A29E",
    "O": "#C5C6C7",
    "bg": "#0B0C10",
    "hover": "#66FCF1",
    "reset": "#1F2833",
    "text": "#C5C6C7"
}
current_player = "X"
board = [""] * 9
buttons = []
ai_mode = False
game_started = False
player1_score = 0
player2_score = 0
rounds_played = 0


def start_game(mode):
    global game_started, current_player, board, ai_mode
    game_started = True
    current_player = "X"
    ai_mode = (mode == "AI")
    turn_label.config(text="Player 1 (X)'s Turn")
    board = [""] * 9  # Reset the board

    # Reset and configure buttons
    for button in buttons:
        button.destroy()
    buttons.clear()

    for i in range(9):
        button = tk.Button(grid_frame, text="", font=("Helvetica", 20, "bold"), width=5, height=2,
                           command=lambda i=i: on_button_click(i), bg=colors["bg"], fg=colors["text"], relief="solid",
                           borderwidth=2)
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        buttons.append(button)

    reset_game()
    show_reset_button()  # Show reset button when the game starts


def reset_game():
    global board, current_player
    board = [""] * 9
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg=colors["bg"])
    current_player = "X"
    turn_label.config(text="Player 1 (X)'s Turn")


def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == current_player and board[i] != "" for i in combo):
            return current_player
    return "Draw" if "" not in board else None


def on_button_click(index):
    global current_player
    if game_started and board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, fg=colors[current_player], bg="#4B4B4B")
        winner = check_winner()

        if winner:
            end_game(winner)
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"{'Player 1' if current_player == 'X' else 'AI' if ai_mode else 'Player 2'}'s Turn")

            if ai_mode and current_player == "O":
                ai_move()


def ai_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    on_button_click(best_move)


def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score


def end_game(winner):
    global player1_score, player2_score, rounds_played

    for button in buttons:
        button.config(state=tk.DISABLED)
    if winner == "Draw":
        messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
    else:
        if winner == "X":
            player1_score += 1
        else:
            player2_score += 1

        rounds_played += 1
        update_scoreboard()

        if player1_score == 2:
            messagebox.showinfo("Tic Tac Toe", "Player 1 is the overall winner!")
            reset_match()
        elif player2_score == 2:
            messagebox.showinfo("Tic Tac Toe", f"{'AI' if ai_mode else 'Player 2'} is the overall winner!")
            reset_match()
        elif rounds_played < 3:
            reset_game()
        else:
            messagebox.showinfo("Tic Tac Toe", "No overall winner after 3 rounds.")
            reset_match()


def reset_match():
    global player1_score, player2_score, rounds_played
    player1_score = 0
    player2_score = 0
    rounds_played = 0
    update_scoreboard()
    reset_game()


def update_scoreboard():
    scoreboard_label.config(
        text=f"Scoreboard - Player 1: {player1_score} | {'AI' if ai_mode else 'Player 2'}: {player2_score}")


def on_enter(event):
    if event.widget["text"] == "":
        event.widget.config(bg=colors["hover"])


def on_leave(event):
    if event.widget["text"] == "":
        event.widget.config(bg=colors["bg"])


def show_main_menu():
    welcome_frame.pack_forget()  # Hide the welcome screen
    main_menu_frame.pack(pady=20)  # Show the main menu


# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x700")
root.configure(bg="#1F2833")

# Welcome Page
welcome_frame = tk.Frame(root, bg="#1F2833")
welcome_frame.pack(pady=50)

welcome_label = tk.Label(welcome_frame, text="Welcome to Tic Tac Toe!", font=("Helvetica", 24, "bold"), bg="#1F2833",
                         fg=colors["text"])
welcome_label.pack(pady=10)

start_button = tk.Button(welcome_frame, text="Start Game", font=("Helvetica", 18, "bold"), command=show_main_menu,
                         bg="#45A29E", fg="white", width=15)
start_button.pack(pady=20)

# Main Menu (Game Mode Selection)
main_menu_frame = tk.Frame(root, bg="#1F2833")

turn_label = tk.Label(main_menu_frame, text="Choose game mode to start", font=("Helvetica", 16, "italic"), bg="#1F2833",
                      fg=colors["text"])
turn_label.pack(pady=10)

buttons_frame = tk.Frame(main_menu_frame, bg="#1F2833")
buttons_frame.pack(pady=5)

btn_pvp_3x3 = tk.Button(buttons_frame, text="3x3 Grid - PvP", font=("Helvetica", 14, "bold"),
                        command=lambda: start_game("PvP"), bg="#1ABC9C", fg="white", width=15)
btn_pvp_3x3.grid(row=0, column=0, padx=10, pady=5)

btn_ai_3x3 = tk.Button(buttons_frame, text="3x3 Grid - Vs AI", font=("Helvetica", 14, "bold"),
                       command=lambda: start_game("AI"), bg="#FF6347", fg="white", width=15)
btn_ai_3x3.grid(row=1, column=0, padx=10, pady=5)

# Game Grid Frame
grid_frame = tk.Frame(root, bg="#1F2833")
grid_frame.pack(pady=20)

# Reset Button (only appears after game has started)
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 16, "bold"), command=reset_game,
                         bg=colors["reset"], fg=colors["hover"], width=15, relief="ridge", activebackground="#4B4B4B",
                         activeforeground=colors["hover"])

# Scoreboard
scoreboard_label = tk.Label(root, text="Scoreboard - Player 1: 0 | Player 2: 0", font=("Helvetica", 16, "bold"),
                            bg="#1F2833", fg=colors["text"])
scoreboard_label.pack(pady=10)


# Function to show reset button after game starts
def show_reset_button():
    reset_button.pack(pady=10)


root.mainloop()
