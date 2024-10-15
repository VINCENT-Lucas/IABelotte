import random
class Joueur:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.main = []
    
    def donner_carte(self, carte):
        self.main.append(carte)
    
    def montrer_main(self):
        print(f"Main de {self.nom}:", end=' ')
        for carte in self.main:
            print(carte, end=' ')
        print("")
    
    def annoncer(self, seuil_annonce):
        if seuil_annonce > 70 and random.random() > 0.2:
            return None     
        # None pour pas d'annonce, sinon, on renvoie l'annonce qu'on veut faire
        return (80, "Pique")
    
    def choisir_carte_a_poser(self, cartes_posables):
        # TODO heuristique ou train IA sur la carte à poser
        return self.poser(cartes_posables[random.randrange(len(cartes_posables))])

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
        if len(cartes_posees) > 1:
            print(f"Cartes posées: ", end="")
            for carte in cartes_posees:
                print(carte, end=" ")
            print("")
            if len(cartes_posees) == 3:
                return cartes_posees[-2].gt(cartes_posees[-1], atout) and cartes_posees[-2].gt(cartes_posees[-3], atout)
            return cartes_posees[-2].gt(cartes_posees[-1], atout)
        return False

    def jouer(self, cartes_posees, atout):
        print(f"{self.nom} joue, voici sa main:", end = ' ')
        self.montrer_main()
        if cartes_posees == []:
            return self.poser(0) # ICI CHANGER 0 PAR LID DE LA MEILLEURE CARTE A JOUER
        else:
            symbole_demande = cartes_posees[0].symbole # Symbole qui a été demandé
            # Si on a des cartes demandées, on doit jouer une de ces cartes
            cartes_symbole_demande = []
            for i_carte in range(len(self.main)):
                carte = self.main[i_carte]
                if carte.symbole == symbole_demande:
                    cartes_symbole_demande.append(i_carte)
            if cartes_symbole_demande != []:
                return self.choisir_carte_a_poser(cartes_symbole_demande)
            # Sinon, si on n'est pas maître, si on peut couper on doit couper
            if not self.est_maitre(cartes_posees, atout):
                cartes_jouables = []
                for i_carte in range(len(self.main)):
                    carte = self.main[i_carte]
                    if carte.symbole == atout:
                        cartes_jouables.append(i_carte)
                if cartes_jouables != []:
                    return self.choisir_carte_a_poser(cartes_jouables)
            # Sinon, on joue ce qu'on veut
            cartes_jouables = []
            for i_carte in range(len(self.main)):
                carte = self.main[i_carte]
                cartes_jouables.append(i_carte)
            return self.choisir_carte_a_poser(cartes_jouables)
             
            
                


