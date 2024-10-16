from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore

model_annonces = Sequential([
    Dense(64, input_dim=36, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(36, activation='softmax')  # Probabilité d'annoncer une couleur ou passer
])
model_annonces.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model_jeu = Sequential([
Dense(64, input_dim=32, activation='relu'),
Dense(128, activation='relu'),
Dense(64, activation='relu'),
Dense(32, activation='softmax')  # Probabilité de jouer chaque carte
])
model_jeu.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Partie annonce IA
cartes_main = joueur.cartes_main_vectorisees()  # Vectorise les cartes en main
annonces_precedentes = self.vectoriser_annonces_precedentes()
score = self.scores[0] - self.scores[1]  # Différence de score

# Appel du modèle
input_data = np.concatenate([cartes_main, annonces_precedentes, [score]])
annonce_prob = model_annonces.predict(input_data.reshape(1, -1))
annonce = np.argmax(annonce_prob)  # L'annonce choisie par l'IA

# Appel modèle
cartes_main = joueur.cartes_main_vectorisees()
position_joueur = indice_joueur
annonce = self.vectoriser_annonce()
cartes_jouees = self.vectoriser_cartes_jouees(cartes_posees)

# Appel du modèle
input_data = np.concatenate([cartes_main, [position_joueur], annonce, cartes_jouees])
carte_prob = model_jeu.predict(input_data.reshape(1, -1))
carte_choisie = np.argmax(carte_prob)

# Convertir l'indice de carte choisie en une vraie carte
carte = joueur.convertir_indice_en_carte(carte_choisie)
