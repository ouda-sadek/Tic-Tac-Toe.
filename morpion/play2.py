def print_board(board):
    for row in range (len(board)):
        print(" | ".join(board [row]))
        if row != len(board)- 1:
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
    """for index in range(9):
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = sign
            if check_winner(board) == sign:
                return index  # AI wins
            board[row_index][col_index] = " "     """    # Undo the move
    check_winner(board)
    if check_winner(board) == sign:
        board[row_index][col_index] = " " 
    # Check for blocking moves
    opponent_sign = "O" if sign == "X" else "X"
    for index in range(9):
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = opponent_sign
            if check_winner(board) == opponent_sign:
                board[row_index][col_index] = " "  # Undo the move
                return index  # Block the opponent
            board[row_index][col_index] = " "  # Undo the move

    # Take the first available cell if no win/blocking moves
    for index in range(9):
        if board[index // 3][index % 3] == " ":
            return index

    return False  # No valid moves

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    mode = input("Choose mode: (1) Human vs Human (2) Human vs AI: ")
    symbol = input("Choose your symbol (X or O): ").upper()

    if symbol not in ["X", "O"]:
        print("Invalid symbol. Defaulting to X.")
        symbol = "X"
    ai_symbol = "O" if symbol == "X" else "X"

    current_player = symbol

    while True:
        print_board(board)

        if current_player == symbol or mode == "1":  # Human's turn
            try:
                move = int(input(f"Player {current_player}, enter your move (0-8): "))
                if move < 0 or move > 8:
                    print("Invalid move! Choose a number between 0 and 8.")
                    continue
                row, col = divmod(move, 3)
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
        else:  # AI's turn
            print("AI is making a move...")
            move = ia(board, ai_symbol)
            if move is False:
                print("No available moves.")
                break
            row, col = divmod(move, 3)

        # Place the player's symbol on the board
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken! Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == ai_symbol:
                print("AI is the winner!")
            else:
                print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = ai_symbol if current_player == symbol else symbol

if __name__ == "__main__":
    tic_tac_toe()
