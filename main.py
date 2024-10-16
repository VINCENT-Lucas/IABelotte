from Partie import *

partie = Partie()

j1 = Joueur("J1")

robotJ1 = Robot("J1")
robotJ2 = Robot("J2")
robotJ3 = Robot("J3")
robotJ4 = Robot("J4")

liste_joueurs = [j1, robotJ2, robotJ3, robotJ4]
partie.ajouter_joueurs(liste_joueurs)

partie.partie()