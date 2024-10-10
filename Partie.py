from Carte import *
from Paquet import *
from Joueur import *


paquet = Paquet()
paquet.afficher()

paquet.melanger()
paquet.afficher()

j1 = Joueur("J1")
j2 = Joueur("J2")
j3 = Joueur("J3")
j4 = Joueur("J4")

while not paquet.is_empty():
    j1.donner_carte(paquet.tirer())
    j2.donner_carte(paquet.tirer())
    j3.donner_carte(paquet.tirer())
    j4.donner_carte(paquet.tirer())

paquet.afficher()
j1.montrer_main()
j2.montrer_main()
j3.montrer_main()
j4.montrer_main()
