from Partie import *

partie = Partie()

j1 = Joueur("J1")
j2 = Joueur("J2")
j3 = Joueur("J3")
j4 = Joueur("J4")

liste_joueurs = [j1, j2, j3, j4]
partie.ajouter_joueurs(liste_joueurs)

partie.partie()