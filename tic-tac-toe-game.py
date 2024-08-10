import tkinter as tk
from tkinter import messagebox
import math

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the game board
buttons = [[None for _ in range(3)] for _ in range(3)]
state = [[None for _ in range(3)] for _ in range(3)]
current_player = 'O'

def create_board():
    for row in range(3):
        for col in range(3):
            btn = tk.Button(root, text="", width=10, height=3, command=lambda r=row, c=col: on_click(r, c))
            btn.grid(row=row, column=col)
            buttons[row][col] = btn

def on_click(row, col):
    global current_player
    if state[row][col] is None and current_player == 'O':
        state[row][col] = 'O'
        buttons[row][col].config(text='O')
        if check_win('O'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
            return
        if check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
            return
        current_player = 'X'
        ai_move()
        current_player = 'O'
        if check_win('X'):
            messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            root.quit()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()

def ai_move():
    _, row, col = minimax(state, 0, True)
    state[row][col] = 'X'
    buttons[row][col].config(text='X')

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth, -1, -1
    if score == -10:
        return score + depth, -1, -1
    if not any(cell is None for row in board for cell in row):
        return 0, -1, -1

    if is_max:
        best = -math.inf
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    move_val, _, _ = minimax(board, depth + 1, False)
                    board[i][j] = None
                    if move_val > best:
                        best = move_val
                        best_move = (i, j)
        return best, best_move[0], best_move[1]
    else:
        best = math.inf
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    move_val, _, _ = minimax(board, depth + 1, True)
                    board[i][j] = None
                    if move_val < best:
                        best = move_val
                        best_move = (i, j)
        return best, best_move[0], best_move[1]

def evaluate(board):
    win_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for pattern in win_patterns:
        if all(board[r][c] == 'X' for r, c in pattern):
            return 10
        if all(board[r][c] == 'O' for r, c in pattern):
            return -10
    return 0

def check_win(player):
    return any(
        all(state[r][c] == player for r, c in pattern)
        for pattern in [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
    )

def check_draw():
    return all(cell is not None for row in state for cell in row)

create_board()
root.mainloop()
