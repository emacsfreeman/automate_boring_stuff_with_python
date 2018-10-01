# Dictionaires
# association clé, valeur

myCrypto = {'name': 'Bitcoin', 'price': 5705.64, 'change': '+0.51%'}
# clés : name, price et change
# valeurs : Bitcoin, 5705.64, +0.51%

for key in myCrypto:
    print('clé :', key)
print('-' * 60)    
# avec la méthode associée
print('Avec la bonne méthode')
for k in myCrypto.keys():
    print(k)
print('-' * 60)

for value in myCrypto:
    print('valeur :', myCrypto[value])
print('-' * 60)    
# avec la méthode associée
print('Avec la bonne méthode')
for v in myCrypto.values():
    print(v)
print('-' * 60)

for key in myCrypto:
    print('(clé, valeur) = ' + '(' + key + ', ' + str(myCrypto[key]) + ')')
print('-' * 60)    
# avec la méthode associée
print('Avec la bonne méthode')
for i in myCrypto.items():
    print(i)
print('-' * 60)

phrase = 'La crypto la plus célèbre est ' + myCrypto['name']
print(phrase)

myInvest = {1.5: 'Bitcoin', 2.5: 'Ethereum'}
print(myInvest)
for key in myInvest:
    print('(clé, valeur) = (' + str(key) + ', ' + myInvest[key] + ')')
print('clés', end=' : ')
print(list(myInvest.keys()))
print('valeurs', end=' : ')
print(list(myInvest.values()))
print('clé-valeur', end=' : ')
print(list(myInvest.items()))

for k, v in myInvest.items():
    print('(clé, valeur) = (' + str(k) + ', ' + v + ')')

    
if 3.5 in myInvest.keys():
    print(myInvest[3.5])
else:
    print('Clé introuvable')

if 'Litecoin' in myInvest.values():
    print('Litecoin fait partie de mes investissements')
else:
    print('Litecoin ne fait pas partie des valeurs')

myWallet = {'btc': 0.5, 'eth': 1.5, 'ltc': 2.5}
phrase1 = "J'ai " + str(myWallet.get('btc', 0)) + ' btc.'
phrase2 = "J'ai " + str(myWallet.get('kmd', 0)) + ' kmd.'
print(phrase1)
print(phrase2)

if 'kmd' not in myWallet:
    myWallet['kmd'] = 25

print(myWallet)

# avec la bonne méthode
myWallet.setdefault('dash', 50)
print(myWallet)


