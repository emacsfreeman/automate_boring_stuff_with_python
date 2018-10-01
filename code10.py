# Chaînes de caractères

print("Caractères d'échappements :")
escapeChar = {"\\' ": 'apostrophe',
              '\\" ': 'guillemmet',
              '\\t ': 'tabulation',
              '\\n ': 'nouvelle ligne',
              '\\  ': 'contre-oblique'}
for k, v in escapeChar.items():
    print(k + ' : ' +  v)

phrase1 = 'Bonjour je m\'appelle Laurent.'
phrase2 = "\"Bonjour\", dit-il."
phrase3 = '\tCeci est une indentation.'
ligne = '-' * 60
phrase4 = ligne + '\nAllons à la ligne.\nNous y voilà.\n' + ligne
phrase5 = 'Sous windaube les répertoires sont précédés de \\'
phrase_list = [phrase1, phrase2, phrase3, phrase4, phrase5]

print('Application avec formattage')
for p in phrase_list:
    print(p)
print('Application brute sans formattage')
print(r'Bonjour je m\'appelle Laurent.')
print(r"\"Bonjour\", dit-il.")
print(r'\tCeci est une indentation.')
print(ligne)
print(r'\nAllons à la ligne.\nNous y voilà.\n')
print(ligne)
print(r'Sous windaube les répertoires sont précédés de \\')
print('''
         Avec les triples apostrophes 
         
                       ou
     
         triples guillemmets

         On peut écrire autant de lignes qu'on veut

         avec un seul print ou dans une seule variable.
     ''')
for char in 'Hello world!':
    print(char)

print('Hello world!'[0:5])

if 'Hello' in 'Hello world':
    print('Of course!')

if 'HELLO' in 'Hello world':
    print('Case does not matter!')
else:
    print('Case does matter!')

crypto = 'Welcome to crypto world!'
print(crypto.upper())
print(crypto)
print(crypto.lower())

print(', '.join(['btc', 'eth', 'kmd']))
print(' '.join(['My', 'name', 'is', 'Bond']))
print('£'.join(['My', 'name', 'is', 'Bond']))
print('My name is Bond'.split())
print('My name is Bond, James Bond'.split())
print('My£name£is£Bond'.split('£'))
print('My name is Bond'.split('n'))
multi_lignes = '''
         Avec les triples apostrophes 
         
                       ou
     
         triples guillemmets

         On peut écrire autant de lignes qu'on veut

         avec un seul print ou dans une seule variable.
     '''
print(multi_lignes.split('\n'))
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))

def printWallet(itemsDict, leftWidth, rightWidth):
    print('WALLET ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
walletItems = {'btc': 1, 'eth': 5, 'kmd': 45, 'ltc': 8}
printWallet(walletItems, 12, 5)
printWallet(walletItems, 20, 6)

space = '      Hello Crypto    '
print('Avant le strip tease')
print(space)
print('Après le strip tease')
print(space.strip())
print('A gauche seulement')
print(space.lstrip())
print('A droite seulement')
print(space.rstrip())
repetTruc = 'TrucMucheTrucTrucBiduleTrucTrucMachinTruc'
print('Avant :\n', repetTruc)
print('Après :\n', repetTruc.strip('Truc'))

# import pyperclip
# pyperclip.copy('Hello Crypto')
# print(pyperclip.paste())
# bug avec pyperclip
