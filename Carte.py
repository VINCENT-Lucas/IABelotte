class Carte:
    def __init__(self, valeur, symbole) -> None:
        self.valeur = str(valeur)
        self.symbole = str(symbole)
    
    def __str__(self) -> str:
        symboles_dict = {"Trefle": "♧", "Pique": "♤", "Coeur": "🤍", "Carreau": "♢"}
        
        symbole = symboles_dict[self.symbole] if self.symbole in symboles_dict else self.symbole
        return f"{self.valeur}{symbole}"
    
    def gt(self, other, atout):
        if self.symbole == atout and other.symbole != atout:
            return True
        if self.symbole != atout and other.symbole == atout:
            return False
        if self.symbole == atout == other.symbole:
            values_dic = {"7": 7, "8": 8, "Q": 9, "K": 10, "10": 11, "A": 12, "9": 13, "J": 14}
        else:
            values_dic = {"7": 7, "8": 8, "9": 9, "J": 10, "Q": 11, "K": 12, "10": 13, "A": 14}
        return values_dic[self.valeur] > values_dic[other.valeur]

    def afficher_liste(liste_cartes):
        for carte in liste_cartes:
            print(carte, end=" ")
        print("")
    
    def points(self, atout):
        if self.symbole == atout:
            values_dic = {"7": 0, "8": 0, "Q": 3, "K": 4, "10": 10, "A": 11, "9": 14, "J": 20}
        else:
            values_dic = {"7": 0, "8": 0, "9": 0, "J": 2, "Q": 3, "K": 4, "10": 10, "A": 11}
        return values_dic[self.valeur]
 