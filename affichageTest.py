import tkinter as tk
from PIL import Image, ImageTk
from Partie import *

DIM_CARTE = (100, 150)
DIM_FENETRE = (900, 680)

# Variables globales pour stocker l'annonce et le symbole sélectionné
annonce_selectionnee = None
symbole_selectionne = None

# --- FONCTIONS DE SÉLECTION ---

def selectionner_annonce(value):
    """Met à jour la variable globale pour l'annonce sélectionnée."""
    global annonce_selectionnee
    annonce_selectionnee = int(value)

def selectionner_symbole(symbole):
    """Met à jour la variable globale pour le symbole sélectionné."""
    global symbole_selectionne
    symbole_selectionne = symbole

# --- FONCTIONS POUR LES BOUTONS ---

def creer_boutons_symboles(frame, callback_update_label):
    """Crée les boutons pour choisir les symboles dans un frame."""
    boutons_symboles = [("Pique", "♠"), ("Cœur", "♥"), ("Carreau", "♦"), ("Trèfle", "♣")]
    for _, symbole in boutons_symboles:
        bouton = tk.Button(frame, text=symbole, font=("Helvetica", 14),
                           command=lambda s=symbole: [selectionner_symbole(s), callback_update_label()])
        bouton.pack(side="left", padx=10)

def creer_boutons_validation(frame, root):
    """Crée les boutons 'Passer' et 'Valider' côte à côte."""
    bouton_passer = tk.Button(frame, text="Passer", command=lambda: passer_annonce(root), bg="red", fg="white", font=("Helvetica", 12))
    bouton_valider = tk.Button(frame, text="Valider", command=lambda: valider_annonce(root), bg="green", fg="white", font=("Helvetica", 12))
    bouton_passer.pack(side="left", padx=10)
    bouton_valider.pack(side="left", padx=10)

# --- FONCTIONS POUR L'AFFICHAGE ---

def mettre_a_jour_label(label, scale):
    """Met à jour le label avec l'annonce et le symbole sélectionnés."""
    def update():
        annonce = scale.get()
        selectionner_annonce(annonce)
        atout = symbole_selectionne if symbole_selectionne else ""
        label.config(text=f"Annonce actuelle : {annonce}{atout}")
    return update

# --- FONCTIONS DE GESTION DE L'ANNONCE ---

def passer_annonce(root):
    """Annule l'annonce en réinitialisant les variables et ferme la fenêtre."""
    global annonce_selectionnee, symbole_selectionne
    annonce_selectionnee, symbole_selectionne = None, None
    root.destroy()

def valider_annonce(root):
    """Valide l'annonce et ferme la fenêtre."""
    root.destroy()

# --- FONCTION D'AFFICHAGE DE LA FENÊTRE D'ANNONCE ---

def afficher_selection_annonce(root):
    """Affiche la fenêtre de sélection d'annonces avec mise à jour en temps réel."""
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
    scale_annonce.set(80)  # Valeur initiale

    # Mettre à jour le label en fonction de la sélection sur le scale
    update_label = mettre_a_jour_label(label_affichage, scale_annonce)
    scale_annonce.bind("<Motion>", lambda event: update_label())

    # Frame pour les boutons des symboles
    frame_boutons = tk.Frame(frame_annonce)
    frame_boutons.pack(pady=10)
    creer_boutons_symboles(frame_boutons, update_label)  # Création des boutons de symbole

    # Frame pour les boutons de validation
    frame_boutons_validation = tk.Frame(frame_annonce)
    frame_boutons_validation.pack(pady=10)
    creer_boutons_validation(frame_boutons_validation, root)

# --- FONCTION DE CRÉATION DE FENÊTRE ---

def creer_fenetre():
    """Crée la fenêtre principale avec les dimensions définies."""
    root = tk.Tk()
    root.title("Coinche")
    largeur_fenetre, hauteur_fenetre = DIM_FENETRE
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
    return root

def creer_fenetre_annonce():
    """Crée la fenêtre pour la sélection des annonces et symboles."""
    root = creer_fenetre()
    afficher_selection_annonce(root)
    root.mainloop()
    return annonce_selectionnee, symbole_selectionne

# Exemple d'utilisation
annonce, symbole = creer_fenetre_annonce()

if annonce is None:
    print("Le joueur a passé.")
else:
    print(f"Annonce sélectionnée: {annonce} points avec l'atout {symbole}")
