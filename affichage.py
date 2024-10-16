import tkinter as tk
from PIL import Image, ImageTk
from Partie import *

carte_posee = None
DIM_CARTE = (100, 150)

def charger_image_dos_carte(dos_carte):
    """Charge et redimensionne l'image du dos de carte."""
    dos_image = Image.open(dos_carte)
    dos_image = dos_image.resize(DIM_CARTE)  # Redimensionner le dos de carte
    return ImageTk.PhotoImage(dos_image)

def effacer_cartes_jouees(frame_centre):
    # Nettoyer l'ancienne carte (s'il y en a une)
    for widget in frame_centre.winfo_children():
        widget.destroy()

def afficher_carte_jouee(frame_centre, carte):
    """Affiche une carte jouée au centre de l'écran."""
    
    # Charger l'image de la carte
    image = Image.open(carte.get_image())
    image = image.resize(DIM_CARTE)  # Redimensionner l'image de la carte
    photo = ImageTk.PhotoImage(image)

    # Afficher la carte au centre
    label_carte = tk.Label(frame_centre, image=photo)
    label_carte.image = photo  # Conserver une référence pour éviter la suppression de l'image
    label_carte.pack(side='left')

def carte_selectionnee(root, carte):
    global carte_posee
    """Fonction appelée lorsque l'utilisateur clique sur une carte."""
    carte_posee = carte  # Remplacez par une action souhaitée
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
    label_titre = tk.Label(frame, text=f"Cartes du collègue", font=("Helvetica", 14))
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
    
def afficher_jeu(main_joueur, cartes_jouees, atout, score):
    """Affiche la disposition complète des cartes pour tous les joueurs."""
    root = tk.Tk()
    root.title("Coinche")
    largeur_fenetre = 800
    hauteur_fenetre = 680
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")

    # Créer une frame pour l'atout et le score
    frame_info = tk.Frame(root)
    frame_info.pack(side="top", fill="x")

    # Label pour afficher l'atout
    symboles_dict = {"Trèfle": "♧", "Pique": "♤", "Coeur": "🤍", "Carreau": "♢"}
    label_atout = tk.Label(frame_info, text=f"Atout: {symboles_dict[atout]}", font=("Helvetica", 14))
    label_atout.pack(side="left", padx=10)  # Aligné à gauche

    # Label pour afficher le score
    label_score = tk.Label(frame_info, text=f"{score[0]} - {score[1]}", font=("Helvetica", 14))
    label_score.pack(side="right", padx=10)  # Aligné à droite


    # Charger l'image du dos de carte
    dos_photo = charger_image_dos_carte("images/Dos.png")

    # --------- Cartes du joueur ---------
    frame_sud = tk.Frame(root)
    frame_sud.pack(side="bottom", pady=10)
    afficher_main_joueur(root, frame_sud, main_joueur)

    # --------- Frame centrale pour la carte jouée ---------
    frame_centre = tk.Frame(root, width=4*(DIM_CARTE[0]+10), height=DIM_CARTE[1])
    frame_centre.place(relx=0.5, rely=0.5, anchor="center") 
    
    for carte in cartes_jouees:
        # Appel pour afficher une carte jouée (tu peux appeler cette fonction au moment où la carte est jouée)
        if carte is not None:
            afficher_carte_jouee(frame_centre, carte)  # Par exemple, affiche la première carte jouée


    nb_cartes = len(main_joueur)
    afficher_cartes_nord(root, dos_photo, nb_cartes)
    afficher_cartes_est(root, dos_photo, nb_cartes)
    afficher_cartes_ouest(root, dos_photo, nb_cartes)

    # Lancer l'application
    root.mainloop()
    return carte_posee