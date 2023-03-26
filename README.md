# projet_taquin
#le jeu consiste en un puzzle constituait de 15 carrés numerotés  de 1  à 15, dans lequel une première configuration aléatoie est donné.
#on nous demande donc de creer une interface graphique pour y jouer; on essayera egalement d'integrer des elements permettant de sauvegarder ou  bien recharger une partie, mais aussi un element permettant deremelangerla configuaration de base en cas ou non solutio

import random
import tkinter as tk

#Initialisation du plateau de jeu
tableau = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]

#fonction pour mélanger les tuiles
def shuffle_tableau(tableau):
    flatten_tableau = [tile for row in tableau for  tile in row]
    random.shuffle(flatten_tableau)
    shuffled_tableau = [[flatten_tableau.pop(0)for _ in row] for row in tableau]
    return shuffled_tableau

#Le joueur a gagné
def a_gagne(tableau):
    return tableau == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]

# Obtenir la position de la tuile vide
def case_vide(tableau):
    for i in range(4):
        for j in range(4):
            if board[i][j] == None:
                return (i, j)

# Déplacer la tuile vers la position vide
def  deplace_tuile(tableau, tuile_position):
    vide_c = case_vide(tableau)
    tableau[tuile_position[0]][tuile_position[1]], tableau[vide_c[0]][vide_c[1]] = tableau[vide_c[0]][vide_c[1]], tableau[tuile_position[0]][tuile_position[1]]
    return tableau

# Créer la fenêtre graphique
fenetre = tk.Tk()
fenetre.title("Solitaire du taquin")

# Initialiser le plateau de jeu
tableau = shuffle_tableau(tableau)

fenetre.mainloop()
