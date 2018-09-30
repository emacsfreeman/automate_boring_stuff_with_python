# Listes

top_crypto = ['BTC', 'ETH', 'XRP', 'BCH', 'EOS']
print("L'indétronable n°1 :", top_crypto[0])
print('Top 5')
print(top_crypto)
for crypto in top_crypto:
    print(crypto)

websites = [
    'https://bitcoin.org/fr/',
    'https://www.ethereum.org/',
    'https://ripple.com/xrp/',
    'https://www.bitcoincash.org/',
    'https://eos.io/'
]

crypto = [top_crypto, websites]
print(crypto)
print('-' * 60)
for i in range(0, 5):
    print('Devise :', crypto[0][i])
    print('Site web :', crypto[1][i])
    print('-' * 60)

print(range(10))
print(range(1, 10))
print(range(10, 20, 2))

if range(3) == [0, 1, 2]:
    print("range(3) == [0, 1, 2]")
else:
    print("range(3) != [0, 1, 2]")
    print("range(3) : ")
    for i in range(3):
        print(i)
    print('-' * 60)
    print("[0, 1, 2] :")
    for i in [0, 1, 2]:
        print(i)
        
    
import copy

test = [1, 2, 3, 4]
test_copie = copy.deepcopy(test)
test_copie[1] = 42
print(test_copie)
print(test)
