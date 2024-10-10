from Carte import *
import random

class Paquet:
    def __init__(self) -> None:
        paquet = []
        for symbole in ["Coeur", "Carreau", "Pique", "Trefle"]:
            for valeur in list(range(7,11)) + ["J", "Q", "K", "A"]:
                paquet.append(Carte(valeur, symbole))
        self.paquet = paquet
    
    def melanger(self):
        random.shuffle(self.paquet)
    
    def afficher(self, nombre=52):
        if self.is_empty():
            print("Vide!")
        else:
            for carte in self.paquet:
                print(carte, end=' ')
        print("")
    
    def tirer(self):
        return self.paquet.pop()
    
    def is_empty(self):
        return self.paquet == []
        
        

