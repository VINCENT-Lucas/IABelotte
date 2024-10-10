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
        # None pour pas d'annonce, sinon, on renvoie l'annonce qu'on veut faire
        return (80, "Pique")
    
    def poser(self, indice):
        return self.main.pop(indice)
    
    def jouer(self, cartes_posees, atout, maitre=False):
        if cartes_posees is None:

