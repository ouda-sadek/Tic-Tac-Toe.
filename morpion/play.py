#
def print_board(board):
    for row in range (len(board)):
        print(" | ".join(board [row]))
        if row != len(board)- 1:
            print("_" * 10)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def ai_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return (i, j)
    return None


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    mode = input("Choose mode: (1) Human vs Human (2) Human vs AI: ")

    while True:
        print_board(board)

        if current_player == "X" or mode == "1":  # Player X or in Human vs Human mode
            row = int(input(f"Player {current_player}, enter your row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter your column (0, 1, 2): "))
        else:  # AI's turn
            print("AI is making a move...")
            row, col = ai_move(board)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken! Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
