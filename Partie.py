from Carte import *
from Paquet import *
from Joueur import *

class Partie:
    def __init__(self, liste_joueurs=[]) -> None:
        self.liste_joueurs = liste_joueurs # Les équipes sont pas ultra faciles à définir, faut mettre E1, E2, E1, E2 pour les joueurs
        self.id_donneur = 0
        self.scores = [0, 0] # Passer à un dictionnaire ?
        self.SCORE_VICTOIRE = 1010

    ''' Penser à n'accepter que 4 joueurs '''
    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    ''' Penser à n'accepter que 4 joueurs '''
    def ajouter_joueurs(self, liste_joueurs):
        for joueur in liste_joueurs:
            self.liste_joueurs.append(joueur)
    
    def distribuer_cartes(self, paquet):
        indice_joueur = 0
        while not paquet.is_empty():
            self.liste_joueurs[indice_joueur].donner_carte(paquet.tirer())
            indice_joueur += 1
            if indice_joueur == len(self.liste_joueurs):
                indice_joueur = 0
    
    def pli(self, indice_joueur):
        # indice_joueur désigne l'indice dans la liste des joueurs du joueur qui commence
        pass

    def phase_annonce(self, indice_joueur):
        # indice_joueur désigne l'indice dans la liste des joueurs du joueur qui commence

        ''' Fonction qui gère un tour d'annonce: un tour d'annonce commence après le début de la phase d'annonce ou à la suite d'une
        annonce, et prend fin lorsque personne n'a décidé d'annoncer ou si quelqu'un a annoncé '''
        def tour_annonce(indice_actuel, seuil_annonce):
            for _ in range(4):
                annonce = self.liste_joueurs[indice_actuel].annoncer(seuil_annonce)
                if annonce is not None:
                    return annonce, indice_actuel
                indice_actuel = indice_actuel + 1 if indice_actuel + 1 != len(self.liste_joueurs) else 0
            return None, indice_actuel

        annonce = None
        annonces_terminees = False
        indice_annonceur = None
        while not annonces_terminees:
            seuil_annonce = 70 if annonce is None else annonce[0]
            annonce, indice_joueur = tour_annonce(indice_joueur, seuil_annonce)

            if annonce is None:
                annonces_terminees = True
            else:
                indice_annonceur = indice_joueur
                indice_joueur = indice_joueur + 1 if indice_joueur + 1 != len(self.liste_joueurs) else 0
        
        return annonce, indice_annonceur

    '''  '''
    def phase_jeu(self, annonce, indice_annonceur, indice_joueur):
        valeur_annonce, atout = annonce
        for _ in range(8):
            self.pli(indice_joueur)
            joueur = self.liste_joueurs[indice_joueur]
        pass

    def manche(self):
        # Le joueur qui joue est celui après le donneur
        indice_joueur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1

        # Phase d'annonce, si on renvoie None c'est que personne n'a annoncé
        annonce, indice_annonceur = self.phase_annonce(indice_joueur)
        if annonce is None:
            return None

        # Phase de jeu
        points = self.phase_jeu(annonce, indice_annonceur, indice_joueur)


    def partie(self):
        # On joue jusqu'à ce qu'on atteigne 1010
        while self.scores[0] < self.SCORE_VICTOIRE and self.scores[1] < self.SCORE_VICTOIRE:
            # On joue une manche
            points_manche = self.manche()
            # On passe au donneur suivant
            self.id_donneur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1
            # On update les scores
            self.scores = (self.scores[0] + points_manche[0], self.scores[1] + points_manche[1])
        return     