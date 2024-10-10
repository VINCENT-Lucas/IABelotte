import tkinter as tk
from tkinter import messagebox

# Fonction pour afficher la carte sélectionnée
def afficher_carte(choix):
    nom, symbole = cartes[choix]
    messagebox.showinfo("Carte Choisie", f"Tu as choisi : {nom} {symbole}")

# Liste des cartes avec leurs symboles Unicode
cartes = [
    ("Valet de Coeur", "\U0001F0BB"),
    ("As de Coeur", "\U0001F0B1"),
    ("Roi de Coeur", "\U0001F0BD"),
    ("Dame de Coeur", "\U0001F0BE"),
    ("As de Pique", "\U0001F0A1"),
    ("Valet de Pique", "\U0001F0AB"),
    ("Joker Noir", "\U0001F0A0"),
    ("As de Trèfle", "\U0001F0C1")
]

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Choisir une carte")

# Ajouter des boutons pour chaque carte
for i, (nom, symbole) in enumerate(cartes):
    bouton = tk.Button(fenetre, text=f"{nom} {symbole}", command=lambda i=i: afficher_carte(i))
    bouton.pack(pady=10)

# Lancer la boucle principale de l'interface
fenetre.mainloop()
