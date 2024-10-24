#TEST
def ia(board, signe):
    # Vérifier que le tableau a une taille correcte et que le signe est valide
    if len(board) != 9 or signe not in ['X', 'O']:
        return False

    # Trouver les indices des cases vides
    cases_vides = [i for i in range(len(board)) if board[i] == ' ']

    # Si aucune case n'est vide, retourner False
    if not cases_vides:
        return False

    # Choisir une case vide au hasard
    coup = cases_vides[int(len(cases_vides) * random_float())]
    return coup

def random_float():
    # Générer un nombre flottant aléatoire entre 0 et 1
    from time import time
    return time() % 1  # Utiliser le temps pour obtenir un "nombre aléatoire"

def afficher_plateau(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---|---|---")
    print("\n")

def verifier_gagnant(board):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    
    for combinaison in combinaisons_gagnantes:
        if board[combinaison[0]] == board[combinaison[1]] == board[combinaison[2]] != ' ':
            return board[combinaison[0]]  # Renvoie le gagnant ('X' ou 'O')
    return None

def tic_tac_toe():
    board = [' ' for _ in range(9)]  # Création d'un plateau vide
    joueur = 'X'  # Le joueur humain
    tours = 0

    while tours < 9:
        afficher_plateau(board)
        if joueur == 'X':  # Tour du joueur humain
            try:
                case = int(input(f"Joueur {joueur}, choisissez une case (0-8) : "))  # Demande un choix
                if board[case] != ' ':
                    print("Cette case est déjà prise. Essayez une autre case.")
                    continue
            except (ValueError, IndexError):
                print("Entrée invalide. Veuillez entrer un numéro entre 0 et 8.")
                continue
        else:  # Tour de l'IA
            print("L'IA joue...")
            case = ia(board, joueur)
        
        board[case] = joueur  # Insérer le signe du joueur
        tours += 1
        
        gagnant = verifier_gagnant(board)
        if gagnant:
            afficher_plateau(board)
            print(f"Joueur {gagnant} a gagné !")
            return
        
        # Changer de joueur
        joueur = 'O' if joueur == 'X' else 'X'

    afficher_plateau(board)
    print("C'est un match nul !")

# Lancer le jeu
if __name__ == "__main__":
    tic_tac_toe()

