#Le jeu consiste en un puzzle constituait de 15 carrés numerotés  de 1  à 15, dans lequel une première configuration aléatoie est donné.
#On nous demande donc de creer une interface graphique pour y jouer; on essayera egalement d'integrer des elements permettant de sauvegarder ou  bien recharger une partie.

import random
import tkinter as tk

# Initialisation du plateau de jeu
board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]

# Mélanger les tuiles
def shuffle_board(board):
    flatten_board = [tile for row in board for tile in row]
    random.shuffle(flatten_board)
    shuffled_board = [[flatten_board.pop(0) for _ in row] for row in board]
    return shuffled_board

# Vérifier si le joueur a gagné
def is_winner(board):
    return board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]

# Obtenir la position de la tuile vide
def get_blank_pos(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == None:
                return (i, j)

# Déplacer la tuile vers la position vide
def move_tile(board, tile_pos):
    blank_pos = get_blank_pos(board)
    board[tile_pos[0]][tile_pos[1]], board[blank_pos[0]][blank_pos[1]] = board[blank_pos[0]][blank_pos[1]], board[tile_pos[0]][tile_pos[1]]
    return board

# Créer la fenêtre graphique
window = tk.Tk()
window.title("Solitaire du taquin")

# Initialiser le plateau de jeu
board = shuffle_board(board)

# Créer la grille de boutons
buttons = []
for i in range(4):
    row = []
    for j in range(4):
        button = tk.Button(window, text=str(board[i][j]), font=("Arial", 20), width=4, height=3)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Fonction pour mettre à jour le texte des boutons et l'état du plateau
def update_board(board):
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(text=str(board[i][j]))

# Fonction pour gérer les clics de boutons
def on_click(i, j):
    global board
    tile_pos = (i, j)
    board = move_tile(board, tile_pos)
    update_board(board)
    if is_winner(board):
        tk.messagebox.showinfo("Félicitations", "Vous avez gagné le jeu !")

# Associer les boutons à la fonction de clic
for i in range(4):
    for j in range(4):
        buttons[i][j].config(command=lambda i=i, j=j: on_click(i, j))

# Démarrer la boucle principale des événements
window.mainloop()
