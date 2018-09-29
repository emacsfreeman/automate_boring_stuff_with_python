# Structure itérative
# La boucle for

# Exemple 1 : méthode Couet
print('=' * 60)
print('Exemple 1')
print("Méthode Couet.")
print('=' * 60)

print('Auto-motivation')
for i in range(5):
    print('Je suis le meilleur ' + str(i) + ' fois sur 5')
print('Source : https://fr.wikipedia.org/wiki/M%C3%A9thode_Cou%C3%A9')

# Exemple 2 : calculs pour sales gosses
print('=' * 60)
print('Exemple 2')
print("Il y a les sales gosses et il y a Gauss")
print('=' * 60)

# pour les sales gosses
print('Pour les sales gosses')
total = 0
for num in range(101):
    print('Itération n°' + str(num))
    total = total + num
print(total)
print('-' * 60)

# pour Gauss
print("Pour Gauss pas d'itération")
total = 100 * 101 / 2
print(int(total))

# Exemple 3 : arguments de range()
print('=' * 60)
print('Exemple 3')
print("Arguments de range()")
print('=' * 60)

print('De deux en deux')
for i in range(0, 10, 2):
    print('i = ', i)
print("On n'a pas atteint la borne finale, i =", i)
print('-' * 60)

print('Tout le monde descend')
for i in range(10, 0, -1):
    print('i = ', i)
print("On n'a pas atteint la borne finale, i =", i)


# Ressources complémentaires
# Documentation officielle : https://docs.python.org/3/reference/compound_stmts.html#for
# Wiki : https://wiki.python.org/moin/ForLoop

