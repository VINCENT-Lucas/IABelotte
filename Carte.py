class Carte:
    def __init__(self, valeur, symbole) -> None:
        self.valeur = valeur
        self.symbole = symbole

    def __str__(self) -> str:
        symboles_dict = {"Trefle": "♧", "Pique": "♤", "Coeur": "🤍", "Carreau": "♢"}
        
        symbole = symboles_dict[self.symbole] if self.symbole in symboles_dict else self.symbole
        return f"{self.valeur}{symbole}"