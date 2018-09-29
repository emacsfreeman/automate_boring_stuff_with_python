# Importation de module



# Exemple 1 : le module random
print('=' * 60)
print('Exemple 1')
print("Le module random.")
print('=' * 60)

import random
for i in range(10):
    print(random.randint(1, 10))
print('-' * 60)
# Ressources complémentaires
# Documentation officielle :
# https://docs.python.org/3/library/random.html?highlight=random#module-random

# Exemple 2 : le module math
print('=' * 60)
print('Exemple 2')
print("Le module math.")
print('=' * 60)

import math
print('Racine carrée de 2 vaut environ :', math.sqrt(2))
print('Sa partie entière inférieure vaut :', math.floor(math.sqrt(2)))
print('Sa partie entière supérieure vaut :', math.ceil(math.sqrt(2)))
print('Le nombre Pi vaut environ :', round(math.pi, 5))
print('Le nombre Tau vaut environ :', round(math.tau, 5))
print("Le nombre e d'Euler vaut environ :", round(math.e, 5))
print('10! =', math.factorial(10))
print('Le reste de la division de 522 par 126 vaut :', int(math.remainder(522, 126)))
print('PGCD(126, 522) =', math.gcd(126, 522))
print('-' * 60)
# Ressources complémentaires
# Documentation officielle :
# https://docs.python.org/3/library/math.html?highlight=math#module-math

# Exemple 3 : le module sys
print('=' * 60)
print('Exemple 3')
print("Le module sys.")
print('=' * 60)

import sys
print('Bonjour')
sys.exit()
print('Au revoir')
print('-' * 60)
# Ressources complémentaires
# Documentation officielle :
# https://docs.python.org/3/library/sys.html?highlight=sys#module-sys

# pip install pyperclip



