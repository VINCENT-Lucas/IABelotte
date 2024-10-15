from Carte import *
from Paquet import *
from Joueur import *
from Robot import *

class Partie:
    def __init__(self, liste_joueurs=[]) -> None:
        self.liste_joueurs = liste_joueurs # Les équipes sont pas ultra faciles à définir, faut mettre E1, E2, E1, E2 pour les joueurs
        self.id_donneur = 0
        self.scores = [0, 0] # Passer à un dictionnaire ?
        self.SCORE_VICTOIRE = 1010
        self.cartes_gagnees = [[],[]]

    ''' Penser à n'accepter que 4 joueurs '''
    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def vider_mains(self):
        for joueur in self.liste_joueurs:
            joueur.vider_main()

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
        cartes_posees = [None]*4
        for _ in range(4):
            carte = self.liste_joueurs[indice_joueur].jouer(cartes_posees, atout)
            cartes_posees[indice_joueur] = carte
            indice_joueur = 0 if indice_joueur + 1 == len(self.liste_joueurs) else indice_joueur + 1
        Carte.afficher_liste(cartes_posees)
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
                if annonce != None:
                    return annonce, indice_actuel
            return None, indice_actuel

        print("Début de la phase d'annonces !")
        annonces_terminees = False
        indice_preneur = None
        annonce = None
        seuil_annonce = 70
        while not annonces_terminees:
            # On met le seuil d'annonces à 70, on doit annoncer au moins 80
            annonce_provisoire, indice_joueur = tour_annonce(indice_joueur, seuil_annonce)
            
            if annonce_provisoire is not None:
                annonce = annonce_provisoire
                seuil_annonce = annonce[0]
                print(f"{self.liste_joueurs[indice_joueur].nom} annonce {annonce}")

            if annonce_provisoire is None:
                annonces_terminees = True
            else:
                indice_preneur = indice_joueur
                indice_joueur = indice_joueur + 1 if indice_joueur + 1 != len(self.liste_joueurs) else 0
        if annonce:
            print(f"On joue pour {annonce[0]} à {annonce[1]}")
        return annonce, indice_preneur

    def afficher_mains(self):
        for joueur in self.liste_joueurs:
            joueur.montrer_main()

    def determiner_gagnant_pli(self, pli, atout):
        best = 0
        for i in range(1, 4):
            if not pli[best].gt(pli[i], atout):
                best = i
        return best

    def compter_points(self, pli, atout):
        somme = 0
        for carte in pli:
            somme += carte.points(atout)
        return somme
 
    '''  '''
    def phase_jeu(self, annonce, indice_joueur):
        print("\nDébut de la phase de jeu !")
        valeur_annonce, atout = annonce
        scores_manche = [0, 0]
        for _ in range(8):
            # Il faudrait stocker les cartes jouées dans une liste de taille 4 avec l'indice correspondant au joueur
            cartes_posees = self.pli(indice_joueur, atout)
            joueur_gagnant = self.determiner_gagnant_pli(cartes_posees, atout)
            # Maintenant qu'on a le pli, il faut l'associer à l'équipe qui le gagne
            score_pli = self.compter_points(cartes_posees, atout)
            scores_manche[joueur_gagnant%2] += score_pli
            indice_joueur = joueur_gagnant
            print(f"Fin du pli ! Scores du pli: {score_pli} pour l'équipe {joueur_gagnant%2}.")
        # En suite, on compte tous les points qu'on a fait pour les 2 équipes
        return scores_manche

    def manche(self):
        # Le joueur qui joue est celui après le donneur
        indice_joueur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1

        # Phase d'annonce, si on renvoie None c'est que personne n'a annoncé
        annonce, indice_annonceur = self.phase_annonce(indice_joueur)
        if annonce is None:
            return (0, 0)

        # Phase de jeu
        points = self.phase_jeu(annonce, indice_joueur)
        return points

    def partie(self):
        # On joue jusqu'à ce qu'on atteigne 1010
        i_manche = 1
        while self.scores[0] < self.SCORE_VICTOIRE and self.scores[1] < self.SCORE_VICTOIRE:
            paquet = Paquet()
            paquet.melanger()
            self.vider_mains()
            self.distribuer_cartes(paquet)
            self.afficher_mains()
            print(f"\nDebut de la manche {i_manche}\n")
            # On joue une manche
            points_manche = self.manche()
            # On passe au donneur suivant
            self.id_donneur = 0 if self.id_donneur + 1 == len(self.liste_joueurs) else self.id_donneur + 1
            # On update les scores
            self.scores = [self.scores[0] + points_manche[0], self.scores[1] + points_manche[1]]
            print(f"----Points sur cette manche: {points_manche}")
            print(f"Scores: {self.scores[0]} à {self.scores[1]}")
            i_manche += 1
        return
