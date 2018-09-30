# Création de fonctions

def bonjour():
    print('Bonjour')

bonjour()
bonjour()
bonjour()

def bonjour(name):
    print('Bonjour', name)

bonjour('Alice')
bonjour('Bob')

def plusUn(num):
    return num +1

print(plusUn(5))

import random
def getAnswer(answerNum):
    if answerNum == 1:
        return "C'est certain"
    elif answerNum == 2:
        return "C'est décidé"
    elif answerNum == 3:
        return 'Oui'

r = random.randint(1, 3)
fortune = getAnswer(r)
print(fortune)

print('Je')
print('suis')
print('Je pense', end=' "fin de ligne" ')
print('donc je suis')
print('Je', 'pense', 'donc', 'je', 'suis')
print('Je', 'pense', 'donc', 'je', 'suis', sep=' BTC ')

variable_globale = 'Bitcoin' # variable globale
print("Avant la déclaration de la fonction crypto :", variable_globale)
def crypto():
    variable_globale = 'Komodo' # variable locale
    print("Dans la fonction crypto :", variable_globale)

print("Avant l'appel de crypto :", variable_globale)
crypto()
print("Après l'appel de crypto :", variable_globale)

def best_crypto():
    crypto = 'Bitcoin'
    market_cap()
    print("Dans la fonction 'best_crypto()' crypto =", crypto)

def market_cap():
    kmd = 'Komodo'
    crypto = 'Ethereum'

best_crypto()
print("Après l'appel de 'best_crypto()' crypto =", crypto)
    
def localisons():
    global test
    test = 'Inside'
    print(test)

test = 'Outside'
localisons()
print(test)

# Exceptions

# def div42by(divideBy):
#     return 42 / divideBy

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))

def div42byE(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
        
print(div42byE(2))
print(div42byE(12))
print(div42byE(0))

print('Bonjour. Quel est ton prénom ?')
prenom = input()

print("Bien, " + prenom + ", je pense à un nombre entre 1 et 20")
mystere = random.randint(1, 20)

for essaiFaits in range(1, 7):
    print("Essai n°" + str(essaiFaits))
    essai = int(input())

    if essai < mystere:
        print('Ton nombre est trop petit')
    elif essai > mystere:
        print('Ton nombre est trop grand')
    else:
        break

if essai == mystere:
    print("Bravo, " + prenom + " ! Tu as deviné mon nombre en " + str(essaiFaits) + " essais !")
else:
    print("Non. Le nombre mystère était " + str(mystere))
