import random
from affichage import *

class Joueur:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.main = []
    
    def donner_carte(self, carte):
        self.main.append(carte) 
    
    def vider_main(self):
        self.main = []

    def montrer_main(self):
        print(f"Main de {self.nom}:", end=' ')
        for carte in self.main:
            print(carte, end=' ')
        print("")
    
    def annoncer(self, seuil_annonce):
        if random.random() > 0.2:
            return None
        # None pour pas d'annonce, sinon, on renvoie l'annonce qu'on veut faire
        atout = ["Pique", "Trèfle", "Coeur", "Carreau"][random.randrange(4)]
        return (seuil_annonce + 10, atout)
    
    def choisir_carte_a_poser(self, cartes_posables, cartes_posees, atout, score):
        carte = afficher_jeu(self.main, cartes_posees, atout, score, cartes_posables)
        for i in range(len(self.main)):
            if self.main[i] == carte:
                return self.poser(i)

    def poser(self, indice):
        print(f"{self.nom} pose {self.main[indice]}")
        return self.main.pop(indice)
    
    def cartes_jouables(self, jouer_a, atout, maitre):
        if jouer_a == atout:
            pass
    
    ''' Renvoie la carte qui gagne le pli pour l'instant '''
    def hauteur(self, cartes_posees, atout):
        if cartes_posees == []:
            return None
        hauteur = cartes_posees[0].valeur

        carte_hauteur = cartes_posees[0]
        for carte in cartes_posees:
            if carte.gt(carte_hauteur, atout):
                hauteur = carte
        return hauteur

    def est_maitre(self, cartes_posees, atout):
        nb_cartes_posees = sum(1 for item in cartes_posees if item is not None)
        if nb_cartes_posees > 1:
            carte1 = next(item for item in cartes_posees if item is not None)
            carte2 = next(item for i, item in enumerate(cartes_posees) if item is not None and sum(1 for x in cartes_posees[:i+1] if x is not None) == 2)
            if nb_cartes_posees == 3:
                carte3 = next(item for i, item in enumerate(cartes_posees) if item is not None and sum(1 for x in cartes_posees[:i+1] if x is not None) == 3)
                return carte2.gt(carte1, atout) and carte2.gt(carte3, atout)
            return carte1.gt(carte2, atout)
        return False

    def jouer(self, cartes_posees, atout, score):
        print(f"{self.nom} joue, voici sa main:", end = ' ')
        self.montrer_main()
        if cartes_posees == [None]*4:
            return self.choisir_carte_a_poser(self.main, cartes_posees, atout, score)
        else:
            symbole_demande = next(item for item in cartes_posees if item is not None).symbole # Symbole qui a été demandé
            # Si on a des cartes demandées, on doit jouer une de ces cartes
            cartes_symbole_demande = []
            for i_carte in range(len(self.main)):
                carte = self.main[i_carte]
                if carte.symbole == symbole_demande:
                    cartes_symbole_demande.append(carte)
            if cartes_symbole_demande != []:
                return self.choisir_carte_a_poser(cartes_symbole_demande, cartes_posees, atout, score)
            # Sinon, si on n'est pas maître, si on peut couper on doit couper
            if not self.est_maitre(cartes_posees, atout):
                cartes_jouables = []
                for i_carte in range(len(self.main)):
                    carte = self.main[i_carte]
                    if carte.symbole == atout:
                        cartes_jouables.append(carte)
                if cartes_jouables != []:
                    return self.choisir_carte_a_poser(cartes_jouables, cartes_posees, atout, score)
            # Sinon, on joue ce qu'on veut
            cartes_jouables = []
            for i_carte in range(len(self.main)):
                carte = self.main[i_carte]
                cartes_jouables.append(carte)
            return self.choisir_carte_a_poser(cartes_jouables, cartes_posees, atout, score)
