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
