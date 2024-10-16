import tkinter as tk
from PIL import Image, ImageTk
from Partie import *

DIM_CARTE = (100, 150)
DIM_FENETRE = (900, 680)

def creer_frame_atout(fenetre, score, atout):
    # Créer une frame pour l'atout et le score
    frame_info = tk.Frame(fenetre)
    frame_info.pack(side="top", fill="x")

    # Label pour afficher l'atout
    symboles_dict = {"Trèfle": "♧", "Pique": "♤", "Coeur": "🤍", "Carreau": "♢"}
    label_atout = tk.Label(frame_info, text=f"Atout: {symboles_dict[atout]}", font=("Helvetica", 14))
    label_atout.pack(side="left", padx=10)  # Aligné à gauche

    # Label pour afficher le score
    label_score = tk.Label(frame_info, text=f"{score[0]} - {score[1]}", font=("Helvetica", 14))
    label_score.pack(side="right", padx=10)  # Aligné à droite
    return frame_info


# --- Charger l'image d'une carte jouée ---
def charger_image_carte(path):
    """Charge l'image d'une carte spécifique et la redimensionne."""
    image = Image.open(path).resize(DIM_CARTE)
    return ImageTk.PhotoImage(image)

def creer_fenetre():
    root = tk.Tk()
    root.title("Coinche")
    largeur_fenetre, hauteur_fenetre = DIM_FENETRE
    root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
    return root

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


def afficher_cartes_jouees(root, cartes_jouees):
    # --------- Frame centrale pour la carte jouée ---------
    frame_centre = tk.Frame(root, width=4*(DIM_CARTE[0]+10), height=DIM_CARTE[1])
    frame_centre.place(relx=0.5, rely=0.5, anchor="center") 
    
    for carte in cartes_jouees:
        # Appel pour afficher une carte jouée
        if carte is not None:
            afficher_carte_jouee(frame_centre, carte)  # Par exemple, affiche la première carte jouée

def charger_image_dos_carte(dos_carte):
    """Charge et redimensionne l'image du dos de carte."""
    dos_image = Image.open(dos_carte)
    dos_image = dos_image.resize(DIM_CARTE)  # Redimensionner le dos de carte
    return ImageTk.PhotoImage(dos_image)

def carte_selectionnee(root, carte):
    global carte_posee
    """Fonction appelée lorsque l'utilisateur clique sur une carte."""
    carte_posee = carte  # Remplacez par une action souhaitée
    root.destroy()

def afficher_main_joueur(root, frame, main, cartes_posables):
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
        if carte in cartes_posables:
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

def afficher_cartes_sud(root, dos_photo, nb_cartes):
    frame_sud = tk.Frame(root)
    frame_sud.pack(side="bottom")
    afficher_cartes_retournees(frame_sud, "Sud", nb_cartes, dos_photo, orientation="horizontal")

def origine_jeu(cartes_jouees):
    nb_cartes_jouees = sum(1 for item in cartes_jouees if item is not None)
    return nb_cartes_jouees

''' origine est l'endroit d'ou part la carte: 1: nord, 2:est, 3:sud 4:ouest '''
def afficher_poser_carte(main_joueur, cartes_jouees, atout, score, carte_posee, origine=3):
    root = creer_fenetre()

    # Créer une frame d'informations (score, atout)
    frame_info = creer_frame_atout(root, score, atout)

    # Charger l'image du dos de carte et l'image de la carte à jouer
    dos_photo = charger_image_dos_carte("images/Dos.png")
    carte_photo = Image.open(carte_posee.get_image())  # Chemin de l'image de la carte jouée
    carte_photo = carte_photo.resize(DIM_CARTE)
    carte_photo = ImageTk.PhotoImage(carte_photo)


    # Afficher les cartes déjà jouées
    afficher_cartes_jouees(root, cartes_jouees)

    nb_cartes_sud = len(main_joueur)
    afficher_cartes_sud(root, dos_photo, nb_cartes_sud)

    # Calculer le nombre de cartes restantes pour chaque joueur
    nb_cartes_jouees = sum(1 for item in cartes_jouees if item is not None)
    nb_cartes_nord = len(main_joueur) - int(nb_cartes_jouees >= 2)
    afficher_cartes_nord(root, dos_photo, nb_cartes_nord)

    nb_cartes_est = len(main_joueur) - int(nb_cartes_jouees >= 1)
    afficher_cartes_est(root, dos_photo, nb_cartes_est)

    nb_cartes_ouest = len(main_joueur) - int(nb_cartes_jouees >= 3)
    afficher_cartes_ouest(root, dos_photo, nb_cartes_ouest)

    # --------- Animation de la carte jouée ---------
    def animer_carte(origine):
        
        # Position initiale de la carte en fonction de l'origine (Est, Nord, Ouest)
        if origine == 2:  # Est
            x_initial, y_initial = DIM_FENETRE[0] - 20 - DIM_CARTE[0], DIM_FENETRE[1] // 2 - DIM_CARTE[1] // 2
        elif origine == 1:  # Nord
            x_initial, y_initial = DIM_FENETRE[0] // 2 - DIM_CARTE[0] // 2, 20
        elif origine == 4:  # Ouest
            x_initial, y_initial = 20, DIM_FENETRE[1] // 2 - DIM_CARTE[1] // 2
        else:  # Default fallback
            x_initial, y_initial = DIM_FENETRE[0] // 2 - DIM_CARTE[0] // 2 , DIM_FENETRE[1] - DIM_CARTE[1]

        # Position finale (centre de l'écran, où les cartes sont jouées)
        x_final, y_final = DIM_FENETRE[0] // 2 - DIM_CARTE[0] // 2, DIM_FENETRE[1] // 2 - DIM_CARTE[1] // 2

        # Créer un label pour afficher l'image de la carte
        carte_label = tk.Label(root, image=carte_photo)
        carte_label.place(x=x_initial, y=y_initial)

        # Variables pour contrôler le déplacement
        steps = 20  # Nombre de pas dans l'animation
        delay = 10  # Délai en millisecondes entre chaque déplacement (total = 20*50 = 1000ms = 1 seconde)
        dx = (x_final - x_initial) / steps
        dy = (y_final - y_initial) / steps

        def deplacer_carte(step):
            if step + 1 <= steps:
                carte_label.place(x=x_initial + step * dx, y=y_initial + step * dy)
                root.after(delay, deplacer_carte, step + 1)
            else:
                # Attendre 500 ms avant de fermer la fenêtre
                root.after(500, root.destroy)

        deplacer_carte(0)

    # Lancer l'animation après un petit délai (optionnel, pour rendre la transition plus naturelle)
    root.after(500, lambda: animer_carte(origine)) 

    # Lancer l'application
    root.mainloop()
    return carte_posee


liste_joueurs = [Robot("J1"),Robot("J2"),Robot("J3"),Robot("J4")]
partie = Partie(liste_joueurs)

paquet = Paquet()
partie.distribuer_cartes(paquet)


afficher_poser_carte(liste_joueurs[0].main, [liste_joueurs[0].main[1], liste_joueurs[2].main[0], liste_joueurs[2].main[2]], "Pique", (0, 0), liste_joueurs[0].main[0])
