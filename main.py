from Partie import *

partie = Partie()

j1 = Joueur("J1")
j2 = Joueur("J2")
j3 = Joueur("J3")
j4 = Joueur("J4")


robotJ1 = Robot("J1")
robotJ2 = Robot("J2")
robotJ3 = Robot("J3")
robotJ4 = Robot("J4")

liste_joueurs = [j1, j2, j3, j4]
liste_joueurs_robots = [j1, robotJ2, robotJ3, robotJ4]
partie.ajouter_joueurs(liste_joueurs_robots)

partie.partie()