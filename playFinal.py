"""def intro():
    print("Hello! welcome to Tic-Tac-Toe game :) ")
    inp=input("do you have a partener ? If your answer is No your gonna to play with IA (yes/no):  ")
    if inp == "yes":
        print("it's gonna to be a great party! happy for you")
    elif inp=="no":
        print("can you win our IA? let's try ")
    else:
        print("please inter the right answer")
    
intro()"""

"""def reset_game():
    Réinitialise le jeu après chaque partie.
    while True:
        reset = input("Do you want to play again? (yes/no): ").strip().lower()
        if reset == "yes":
            return True
        elif reset == "no":
            print("Thank you for playing! Goodbye!")
            return False
        else:
            print("Please enter a valid answer (yes/no).")"""


"""Displays the game board."""
def print_board(board):
    for row in range (len(board)):
        print(" | ".join(board [row]))
        if row != len(board)- 1:
            print("_" * 10)

"""Check if there is a winner."""
def check_winner(board):
    # Checks rows and columns
    for row_index in range(3):
        if board[row_index][0] == board[row_index][1] == board[row_index][2] != " ":
            return board[row_index][0]
        if board[0][row_index] == board[1][row_index] == board[2][row_index] != " ":
            return board[0][row_index]
     # Check the diagonals   
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    # No winner
    return None

"""Check if the game board is full."""
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

"""AI must choose the best move"""
def ia(board, sign):
    # Check for winning moves
    for index in range(9):
        row_index = index // 3
        col_index = index % 3
        if board[row_index][col_index] == " ":
            board[row_index][col_index] = sign #try the move
            if check_winner(board) == sign:
                return index #return the move winner
            board[row_index][col_index] = " " #cancel the movement

   
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
    # No valid moves
    return False  


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

        """if not reset_game():
            break"""
if __name__ == "__main__":
    tic_tac_toe()
