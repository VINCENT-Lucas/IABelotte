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
    
    def pli(self, indice_joueur, atout):
        print(f"Nouveau pli ! C'est à {self.liste_joueurs[indice_joueur].nom} (atout {atout})")
        self.afficher_mains()
        # indice_joueur désigne l'indice dans la liste des joueurs du joueur qui commence
        cartes_posees = []
        id_maitre = indice_joueur
        for _ in range(4):
            carte = self.liste_joueurs[indice_joueur].jouer(cartes_posees, atout)
            cartes_posees.append(carte)
            indice_joueur = 0 if indice_joueur + 1 == len(self.liste_joueurs) else indice_joueur + 1
        return cartes_posees

    def phase_annonce(self, indice_joueur):
        # indice_joueur désigne l'indice dans la liste des joueurs du joueur qui commence

        ''' Fonction qui gère un tour d'annonce: un tour d'annonce commence après le début de la phase d'annonce ou à la suite d'une
        annonce, et prend fin lorsque personne n'a décidé d'annoncer ou si quelqu'un a annoncé '''
        def tour_annonce(indice_actuel, seuil_annonce):
            print(f"Debut tour d'annonces avec un seuil à {seuil_annonce}")
            for _ in range(4):
                annonce = self.liste_joueurs[indice_actuel].annoncer(seuil_annonce)
                indice_actuel = indice_actuel + 1 if indice_actuel + 1 != len(self.liste_joueurs) else 0
                # Si on a une nouvelle annonce
                if annonce is not None:
                    return annonce, indice_actuel
            return None, indice_actuel

        print("Début de la phase d'annonces !")
        annonce = None
        annonces_terminees = False
        indice_annonceur = None
        while not annonces_terminees:
            # On met le seuil d'annonces à 70, on doit annoncer au moins 80
            seuil_annonce = 70 if annonce is None else annonce[0]
            res_annonce, indice_joueur = tour_annonce(indice_joueur, seuil_annonce)
            
            if res_annonce is not None:
                annonce = res_annonce
            print(f"{self.liste_joueurs[indice_joueur].nom} annonce {annonce}")

            if res_annonce is None:
                annonces_terminees = True
            else:
                indice_annonceur = indice_joueur
                indice_joueur = indice_joueur + 1 if indice_joueur + 1 != len(self.liste_joueurs) else 0
        
        print(f"On joue pour {annonce}")
        return annonce, indice_annonceur

    def afficher_mains(self):
        for joueur in self.liste_joueurs:
            joueur.montrer_main()

    '''  '''
    def phase_jeu(self, annonce, indice_annonceur, indice_joueur):
        print("\nDébut de la phase de jeu !")
        valeur_annonce, atout = annonce
        for _ in range(8):
            # Il faudrait stocker les cartes jouées dans une liste de taille 4 avec l'indice correspondant au joueur
            self.pli(indice_joueur, atout)
            joueur = self.liste_joueurs[indice_joueur]
            # Maintenant qu'on a le pli, il faut l'associer à l'équipe qui le gagne
        # En suite, on compte tous les points qu'on a fait pour les 2 équipes
        pass

    def manche(self):
        # Le joueur qui joue est celui après le donneur
        indice_joueur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1

        # Phase d'annonce, si on renvoie None c'est que personne n'a annoncé
        annonce, indice_annonceur = self.phase_annonce(indice_joueur)
        if annonce is None:
            return (0, 0)

        # Phase de jeu
        points = self.phase_jeu(annonce, indice_annonceur, indice_joueur)
        return points

    def partie(self, paquet):
        # On joue jusqu'à ce qu'on atteigne 1010
        print(self.liste_joueurs)
        self.distribuer_cartes(paquet)
        self.afficher_mains()
        i_manche = 1
        while self.scores[0] < self.SCORE_VICTOIRE and self.scores[1] < self.SCORE_VICTOIRE:
            print(f"\nDebut de la manche {i_manche}\n")
            # On joue une manche
            points_manche = self.manche()
            # On passe au donneur suivant
            self.id_donneur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1
            # On update les scores
            self.scores = (self.scores[0] + points_manche[0], self.scores[1] + points_manche[1])
            print(f"Scores: {self.scores[0]} à {self.scores[1]}")
            i_manche += 1
        return
