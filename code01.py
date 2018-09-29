# Source : https://youtu.be/XWkLyn0Fct4?t=1h4m15s
# Ce programme dit bonjour et demande le prénom de l'utilisateur

print('Bonjour le monde !')
print('Quel est votre prénom ?') # demande le prénom
monPrenom = input()
print('Ravi de faire ta connaissance ' + monPrenom)
print('La longueur de ton prénom est : ')
print(len(monPrenom))
print('Quel est ton âge ?') # demande l'âge
monAge = input()
print('Tu auras ' + str(int(monAge) + 1) + ' ans dans 1 an.')
