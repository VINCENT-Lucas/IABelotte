import tkinter as tk
from PIL import Image, ImageTk
from Partie import *

carte_selectionnee = None
DIM_CARTE = (100, 150)

def charger_image_dos_carte(dos_carte):
    """Charge et redimensionne l'image du dos de carte."""
    dos_image = Image.open(dos_carte)
    dos_image = dos_image.resize(DIM_CARTE)  # Redimensionner le dos de carte
    return ImageTk.PhotoImage(dos_image)

def carte_selectionnee(root, carte):
    global carte_selectionnee
    """Fonction appelée lorsque l'utilisateur clique sur une carte."""
    carte_selectionnee = carte  # Remplacez par une action souhaitée
    root.destroy()

def afficher_main_joueur(root, frame, main):
    """Affiche les cartes de la main du joueur (Sud)."""
    label_titre = tk.Label(frame, text="Voici ta main:", font=("Helvetica", 16))
    label_titre.pack(pady=10)

    for carte in main:
        image = Image.open(carte.get_image())
        image = image.resize(DIM_CARTE)  # Redimensionner l'image
        photo = ImageTk.PhotoImage(image)

        # Créer un label avec l'image de la carte
        label_carte = tk.Label(frame, image=photo)
        label_carte.image = photo  # Conserver une référence à l'image pour éviter sa suppression
        
        # Ajouter un gestionnaire d'événements pour le clic sur la carte
        label_carte.bind("<Button-1>", lambda event, c=carte: carte_selectionnee(root, c))
        
        label_carte.pack(side="left", padx=5)

def afficher_cartes_retournees(frame, position, nb_cartes, image_dos, decalage=0, orientation="horizontal"):
    """Affiche les cartes retournées (dos) pour un joueur."""
    label_titre = tk.Label(frame, text=f"Cartes {position}", font=("Helvetica", 14))
    label_titre.pack()
    frame.update()
    for i in range(nb_cartes):
        label_dos = tk.Label(frame, image=image_dos)
        label_dos.image = image_dos  # Conserver une référence à l'image

        if orientation == "horizontal":
            label_dos.pack(side="left", padx=5)
        elif orientation == "vertical":
            label_dos.place(x=0, y=i * decalage)  # Superposition avec décalage vertical

def afficher_cartes_nord(root, dos_photo, nb_cartes):
    frame_nord = tk.Frame(root)
    frame_nord.pack(side="top")
    afficher_cartes_retournees(frame_nord, "Nord", nb_cartes, dos_photo, orientation="horizontal")

def afficher_cartes_est(root, dos_photo, nb_cartes):
    decalage = 10
    frame_est = tk.Frame(root, width=DIM_CARTE[0], height=DIM_CARTE[1]+nb_cartes*decalage)
    frame_est.pack_propagate(False)
    frame_est.pack(side="right", padx=10)
    afficher_cartes_retournees(frame_est, "Est", nb_cartes, dos_photo, decalage=decalage, orientation="vertical")

def afficher_cartes_ouest(root, dos_photo, nb_cartes):
    decalage = 10
    frame_ouest = tk.Frame(root, width=DIM_CARTE[0], height=DIM_CARTE[1]+nb_cartes*decalage)
    frame_ouest.pack_propagate(False)
    frame_ouest.pack(side="left", padx=10)
    afficher_cartes_retournees(frame_ouest, "Ouest", nb_cartes, dos_photo, decalage, orientation="vertical")
    
def afficher_main(main_joueur):
    """Affiche la disposition complète des cartes pour tous les joueurs."""
    root = tk.Tk()
    root.title("Coinche")

    # Charger l'image du dos de carte
    dos_photo = charger_image_dos_carte("images/Dos.png")

    # --------- Cartes du joueur ---------
    frame_sud = tk.Frame(root)
    frame_sud.pack(side="bottom", pady=10)
    afficher_main_joueur(root, frame_sud, main_joueur)

    nb_cartes = 6
    afficher_cartes_nord(root, dos_photo, nb_cartes)
    afficher_cartes_est(root, dos_photo, nb_cartes)
    afficher_cartes_ouest(root, dos_photo, nb_cartes)

    # Lancer l'application
    root.mainloop()
    return carte_selectionnee
    

partie = Partie()

j1 = Joueur("J1")
j2 = Joueur("J2")
j3 = Joueur("J3")
j4 = Joueur("J4")

liste_joueurs = [j1, j2, j3, j4]
partie.ajouter_joueurs(liste_joueurs)
paquet = Paquet()
paquet.melanger()
partie.distribuer_cartes(paquet)
# Exemple d'utilisation
liste_de_cartes = j1.main # Liste de cartes à afficher
c = afficher_main(liste_de_cartes)
