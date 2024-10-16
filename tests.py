# TODO GERER LES INDICES ---> OK
# Penser a mélanger le paquet fin partie ------> OK
# TODO Gérer les coupes au lieu de mélanger au pif 

# ------------ Partie jeu -----------------------

# TODO gérer lorsque personne n'annonce direct -> A moitié bon
# TODO gérer les 10 de der ------------------> FAIT
# TODO regarder si on a réussi le contrat --------------> FAIT

# TODO ajouter le fait de coincher 

# TODO SURTOUT jouer seulement les cartes qu'on peut
# --- Soit on rejoue si la carte est incorrecte mais le mieux c'est de créer des boutons que pour les cartes correctes
# TODO régler le problème du joueur qui joue tout seul des fois

# ------------ Partie affichage -----------------------

# TODO Afficher les cartes du pli au milieu ----------> OK
# --- Mais réussir à les faire se distinguer les unes des autres, en définissant 4 frames ? 

# TODO faire des "animations" pour faire jouer les autres joueurs
# --- Donc il faut qu'à chaque 

# ------------- Partie IA ------------------------

'''
2 modèles à entrainer:
- 1 modèle qui annonce
- 1 modèle qui choisit les cartes à jouer

Update les 2 modèles en fonction du résultat de la manche ? Ou bien en update juste 1 puis l'autre ?


Quelles entrées ? 

Modèle qui annonce
- Cartes en main
- Annonces précédentes (si un joueur annonce à coeur ça augmente ses chances d'avoir du jeu à coeur donc moins de jeu ailleurs)
- Score actuel (si on est proche de gagner on peut annoncer - aggressif)

ANNONCES possibles: 80, 90, 100, 110, 120, 130, 140, 150, 160: 9 valeurs à 4 atouts donc 36

Modèle qui joue
- Cartes de la main
- Cartes déjà tombées
- Position du 1er à jouer (important dans certains cas)
- Annonce et points actuels (si on est proche de mettre dedans l'équipe adverse, on peut donner beaucoup de points)


TODO:
- Stocker toutes les annonces dans une liste au fur et à mesure
'''
