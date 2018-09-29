# Structure de branchement
# if, elif, else

mot_de_passe = input('Choisis ton mot de passe :\n')
if len(mot_de_passe) < 8:
    print("Ton mot de passe contient moins de 8 caractères c'est risqué")
elif mot_de_passe == 'azertyuiop' or mot_de_passe == 'AZERTYUIOP':
    print("Ton mot de passe est trop simple c'est risqué.")
elif mot_de_passe == '123azerty':
    print("Ton mot de passe est trop simple c'est risqué.")
else:
    print("Ton mot de passe contient au moins 8 caractères c'est un bon début.")
    
# Ressources complémentaires
# Documentation officielle : https://wiki.python.org/moin/WhileLoop
# Wiki : https://wiki.python.org/moin/IfStatementWithValue
