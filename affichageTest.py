import tkinter as tk
from PIL import Image, ImageTk
from Partie import *

DIM_CARTE = (100, 150)
DIM_FENETRE = (900, 680)

annonce_selectionnee = None
symbole_selectionne = None

# --- Fonctions de sélection ---

def selectionner_annonce(value):
    global annonce_selectionnee
    annonce_selectionnee = int(value)

def selectionner_symbole(symbole):
    global symbole_selectionne
    symbole_selectionne = symbole

def passer_annonce(root):
    global annonce_selectionnee, symbole_selectionne
    annonce_selectionnee, symbole_selectionne = None, None
    root.destroy()

def valider_annonce(root):
    root.destroy()

# --- Affichage des cartes ---

def charger_image_dos_carte(path):
    """Charge l'image du dos de carte et la redimensionne."""
    image = Image.open(path).resize(DIM_CARTE)
    return ImageTk.PhotoImage(image)

def afficher_main_joueur(root, frame, main_joueur, cartes_posables):
    """Affiche les cartes du joueur (Sud)."""
    for carte in main_joueur:
        bouton = tk.Button(frame, text=carte, font=("Helvetica", 14))  # Placeholder, vous pouvez ajouter des images de cartes
        bouton.pack(side="left", padx=10)

def afficher_cartes_nord(root, dos_photo, nb_cartes):
    """Affiche les cartes de l'adversaire au Nord."""
    frame_nord = tk.Frame(root)
    frame_nord.pack(side="top", pady=10)
    for _ in range(nb_cartes):
        label = tk.Label(frame_nord, image=dos_photo)
        label.pack(side="left", padx=5)

def afficher_cartes_est(root, dos_photo, nb_cartes):
    """Affiche les cartes de l'adversaire à l'Est."""
    frame_est = tk.Frame(root)
    frame_est.pack(side="right", padx=10)
    for _ in range(nb_cartes):
        label = tk.Label(frame_est, image=dos_photo)
        label.pack(pady=5)

def afficher_cartes_ouest(root, dos_photo, nb_cartes):
    """Affiche les cartes de l'adversaire à l'Ouest."""
    frame_ouest = tk.Frame(root)
    frame_ouest.pack(side="left", padx=10)
    for _ in range(nb_cartes):
        label = tk.Label(frame_ouest, image=dos_photo)
        label.pack(pady=5)

    # --- Fonction d'affichage de la sélection d'annonces ---

def afficher_selection_annonce(root):
    global annonce_selectionnee, symbole_selectionne

    # Créer une frame pour l'annonce
    frame_annonce = tk.Frame(root)
    frame_annonce.place(relx=0.5, rely=0.5, anchor="center") 

    # Label principal
    label_annonce = tk.Label(frame_annonce, text="Choisissez votre annonce :", font=("Helvetica", 14))
    label_annonce.pack()

    # Label dynamique qui montre l'annonce actuelle
    label_affichage = tk.Label(frame_annonce, text="", font=("Helvetica", 12))
    label_affichage.pack()

    # Échelle pour choisir l'annonce (80 à 160)
    scale_annonce = tk.Scale(frame_annonce, from_=80, to=160, orient="horizontal", resolution=10, length=200)
    scale_annonce.pack(pady=10)
    scale_annonce.set(80)

    def mettre_a_jour_label():
        annonce = scale_annonce.get()
        selectionner_annonce(annonce)
        atout = symbole_selectionne if symbole_selectionne else ""
        label_affichage.config(text=f"Annonce actuelle : {annonce}{atout}")

    scale_annonce.bind("<Motion>", lambda event: mettre_a_jour_label())

    # Frame pour les boutons des symboles
    frame_boutons = tk.Frame(frame_annonce)
    frame_boutons.pack(pady=10)
    creer_boutons_symboles(frame_boutons, mettre_a_jour_label)

    # Frame pour les boutons de validation
    frame_boutons_validation = tk.Frame(frame_annonce)
    frame_boutons_validation.pack(pady=10)
    creer_boutons_validation(frame_boutons_validation, root)

def creer_boutons_symboles(frame, callback_update_label):
    boutons_symboles = [("Pique", "♠"), ("Cœur", "♥"), ("Carreau", "♦"), ("Trèfle", "♣")]
    for _, symbole in boutons_symboles:
        bouton = tk.Button(frame, text=symbole, font=("Helvetica", 14),
                           command=lambda s=symbole: [selectionner_symbole(s), callback_update_label()])
        bouton.pack(side="left", padx=10)

def creer_boutons_validation(frame, root):
    bouton_passer = tk.Button(frame, text="Passer", command=lambda: passer_annonce(root), bg="red", fg="white", font=("Helvetica", 12))
    bouton_valider = tk.Button(frame, text="Valider", command=lambda: valider_annonce(root), bg="green", fg="white", font=("Helvetica", 12))
    bouton_passer.pack(side="left", padx=10)
    bouton_valider.pack(side="left", padx=10)

# --- Création de la fenêtre ---

def creer_fenetre():
    root = tk.Tk()
    root.title("Coinche")
    largeur_fenetre, hauteur_fenetre = DIM_FENETRE
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
    return root

# --- Fonction principale d'affichage du jeu ---

def afficher_annonces(main_joueur, cartes_jouees, atout, score, cartes_posables):
    """Affiche la disposition complète des cartes pour tous les joueurs."""
    root = creer_fenetre()

    # Créer une frame d'informations (ex : score, atout) - à définir selon vos besoins
    frame_info = tk.Frame(root)
    frame_info.pack(side="top", pady=10)

    # Charger l'image du dos de carte
    dos_photo = charger_image_dos_carte("images/Dos.png")

    # --------- Afficher l'interface d'annonce ---------
    afficher_selection_annonce(root)

    # --------- Cartes du joueur (Sud) ---------
    frame_sud = tk.Frame(root)
    frame_sud.pack(side="bottom", pady=10)
    afficher_main_joueur(root, frame_sud, main_joueur, cartes_posables)

    # Calculer le nombre de cartes des adversaires selon les cartes jouées
    nb_cartes_jouees = sum(1 for item in cartes_jouees if item is not None)
    
    nb_cartes_nord = len(main_joueur) - int(nb_cartes_jouees >= 2)
    afficher_cartes_nord(root, dos_photo, nb_cartes_nord)

    nb_cartes_est = len(main_joueur) - int(nb_cartes_jouees >= 1)
    afficher_cartes_est(root, dos_photo, nb_cartes_est)
    
    nb_cartes_ouest = len(main_joueur) - int(nb_cartes_jouees >= 3)
    afficher_cartes_ouest(root, dos_photo, nb_cartes_ouest)

    # Lancer l'application
    root.mainloop()
    return annonce_selectionnee, symbole_selectionne

# Exemple d'utilisation
annonce, symbole = creer_fenetre_annonce()

if annonce is None:
    print("Le joueur a passé.")
else:
    print(f"Annonce sélectionnée: {annonce} points avec l'atout {symbole}")
