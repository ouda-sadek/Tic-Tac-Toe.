import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in range(len(board)):
        print(" | ".join(board[row]))
        if row != len(board) - 1:
            print("_" * 10)

def check_winner(board):
    for row_index in range(3):
        if board[row_index][0] == board[row_index][1] == board[row_index][2] != " ":
            return board[row_index][0]
        if board[0][row_index] == board[1][row_index] == board[2][row_index] != " ":
            return board[0][row_index]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def ia(board, sign):
    # Check for winning moves
    for index in range(9):
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = sign
            if check_winner(board) == sign:
                return index
            board[row_index][col_index] = " "  # Undo the move
    
    # Check for blocking moves
    opponent_sign = "O" if sign == "X" else "X"
    for index in range(9):
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = opponent_sign
            if check_winner(board) == opponent_sign:
                board[row_index][col_index] = " "  # Undo the move
                return index
            board[row_index][col_index] = " "  # Undo the move

    # Take the first available cell if no win/blocking moves
    for index in range(9):
        if board[index // 3][index % 3] == " ":
            return index

    return False  # No valid moves

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.mode = None
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.create_mode_selection()
        self.create_board()

    def create_mode_selection(self):
        self.label = tk.Label(self.master, text="Select Game Mode:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.human_vs_human_button = tk.Button(self.master, text="Human vs Human", command=self.start_human_vs_human)
        self.human_vs_human_button.grid(row=1, column=0, padx=10, pady=5)

        self.human_vs_ai_button = tk.Button(self.master, text="Human vs AI", command=self.start_human_vs_ai)
        self.human_vs_ai_button.grid(row=2, column=0, padx=10, pady=5)

    def create_board(self):
        self.buttons = [[tk.Button(self.master, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=r, c=c: self.player_move(r, c)) 
                        for c in range(3)] for r in range(3)]
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c + 1)  # Shift to the right of mode selection

    def start_human_vs_human(self):
        self.mode = "human_vs_human"
        self.reset_game()

    def start_human_vs_ai(self):
        self.mode = "human_vs_ai"
        self.reset_game()

    def player_move(self, r, c):
        if self.board[r][c] == " ":
            self.board[r][c] = self.current_player
            self.buttons[r][c].config(text=self.current_player)
            winner = check_winner(self.board)

            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.mode == "human_vs_ai" and self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        move = ia(self.board, "O")
        if move is not False:
            row, col = divmod(move, 3)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")
            winner = check_winner(self.board)
            if winner:
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "X"

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
