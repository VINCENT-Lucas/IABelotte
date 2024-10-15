# TODO GERER LES INDICES ---> OK
# Penser a mélanger le paquet fin partie ------> OK
# TODO Gérer les coupes au lieu de mélanger au pif 

# TODO gérer lorsque personne n'annonce direct -> A moitié bon
# TODO gérer les 10 de der
# TODO regarder si on a réussi le contrat


ma_liste = [None, 1]
resultat = next(item for i, item in enumerate(ma_liste) if item is not None and sum(1 for x in ma_liste[:i+1] if x is not None) == 2)
print(resultat)