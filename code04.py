# Structure itérative
# La boucle while

# Exemple 1 : table de mutliplication jusqu'à 10
print('=' * 60)
print('Exemple 1')
print("Table de multiplication jusqu'à 10.")
print('=' * 60)

compteur = 0
entier = int(input('Choisir un nombre entier : '))
print('=' * 60)
while compteur < 10:
    compteur = compteur + 1
    print(str(entier) + ' x ' + str(compteur) + ' = ' + str(int(entier*compteur)))

# Exemple 2
print('=' * 60)
print('Exemple 2')
print('=' * 60)
prenom = ''
while prenom != 'q' and prenom != 'Q':
    print("Taper 'q' ou 'Q' pour quitter.")
    print('Entre ton prénom :')
    prenom = input()

# Exemple 3    
# Break
print('=' * 60)
print('Exemple 3')
print('=' * 60)
while True:
    print('Ceci est une boucle infinie...')
    sortie = input('Essaie de saisir un mot pour en sortir :\n')
    if sortie == 'sortie':
        break

# Exemple 4    
# Continue
print('=' * 60)
print('Exemple 4')
print('=' * 60)
compteur = 0
while compteur < 10:
    compteur = compteur + 1
    if compteur % 2 == 0:
        continue
    else:
        print(str(compteur) + ' est un nombre impair.')
        
    
# Ressources complémentaires
# Documentation officielle : https://wiki.python.org/moin/WhileLoop
# Wiki https://wiki.python.org/moin/WhileLoop
    
    
