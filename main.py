from Partie import *

partie = Partie()
paquet = Paquet()
paquet.afficher()

paquet.melanger()
paquet.afficher()

j1 = Joueur("J1")
j2 = Joueur("J2")
j3 = Joueur("J3")
j4 = Joueur("J4")

liste_joueurs = [j1, j2, j3, j4]
partie.ajouter_joueurs(liste_joueurs)

paquet.afficher()

partie.distribuer_cartes(paquet)

j1.montrer_main()
j2.montrer_main()
j3.montrer_main()
j4.montrer_main()