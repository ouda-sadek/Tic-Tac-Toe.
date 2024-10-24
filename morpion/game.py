def print_board(board):
    for row in range (len(board)):
        print(" | ".join(board [row]))
        if row != len(board)- 1:
            print("_" * 10)
        
def check_winner(board):
    # Vérification des lignes, colonnes et diagonales
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(2):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row) 

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Joueur {current_player}, entrez la colonne (0-2): "))
            col = int(input(f"Joueur {current_player}, entrez la ligne (0-2): "))
            #coord = ([row], [col])
            #int = input(f"Joueur {current_player}, entrez la colonne (0-2): ", entrez la ligne (0-2): "))
        except ValueError:
            print("Entrée invalide, veuillez entrer un numéro entre 0 et 2.")
            continue

        if board[row][col] != " ":
            print("Cette case est déjà prise, choisissez-en une autre.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Le joueur {winner} a gagné !")
            break

        if is_board_full(board):
            print_board(board)
            print("Match nul !")
            break

        current_player = "O" if current_player == "X" else "X" 

if __name__ == "__main__":
    tic_tac_toe()


"""def ia(board, signe):
    if len(board) != 9 or signe not in ['X', 'O']:
        return False
    print(ia(board, signe))"""