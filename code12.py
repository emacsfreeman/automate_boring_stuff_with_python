# Fichiers

import os


def headline(title):
    print('\n')
    print('=' * 80)
    print(title)
    print('-' * len(title))
    print('\n')
    
title = "The 'os.path.join()' command"    
headline(title)

print(os.path.join('usr', 'bin', 'spam'))
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join(os.getcwd(), filename))

title = "The 'os.getcwd()' command"    
headline(title)
print('current working directory:', os.getcwd())

title = "The 'os.chdir()' command"    
headline(title)
print('change directory')
os.chdir('/home/whitehathacker/Bureau')
print('new current working directory:', os.getcwd())
print('change directory')
os.chdir('/home/whitehathacker/automate-the-boring-stuff')
print('new current working directory:', os.getcwd())

# print('create a new folder')
# os.makedirs(os.getcwd() + '/new-folder')

title = "The 'os.path.abspath()' command"    
headline(title)
print('Absolute path:', os.path.abspath('.'))
print('Absolute path:', os.path.abspath('./new-folder'))

title = "The 'os.path.isabs()' command"    
headline(title)
print('Is "./new-folder" an absolute path?', os.path.isabs('.'))
print('Is "." an absolute path?', os.path.isabs(os.path.abspath('.')))

title = "The 'os.path.relpath()' command"    
headline(title)
print('relation between "/home" and "/":\n', os.path.relpath('/home', '/'))
print('relation between "/home" and "/dev/net":\n', os.path.relpath('/home', '/dev/net'))
print('current working directory:\n', os.getcwd())

title = "The dir name and the base name"
headline(title)
path = os.getcwd() + '/code11.py'
print('Path name:\n', path)
print('Base name:\n', os.path.basename(path))
print('Dir name:\n', os.path.dirname(path))
print('With split() method:\n', os.path.split(path))
print('Using split() with sep:\n', path.split(os.sep))

title = 'The "os.path.getsize()" command'
headline(title)
print('size of code11.py =', os.path.getsize(os.getcwd() + '/code-avant-fichiers/code11.py'))

title = 'The "os.listdir()" command'
headline(title)
print('current files and folders:', os.listdir(os.getcwd()))

totalSize = 0
for filename in os.listdir(os.getcwd() + '/code-avant-fichiers'):
    totalSize += os.path.getsize(os.path.join(os.getcwd() + '/code-avant-fichiers', filename))
print('taille du dossier "code-avant-fichiers" :', totalSize)

title = 'The "os.path.exists()" command'
headline(title)
print(os.path.exists(os.getcwd()))
print(os.path.exists('/home/testons'))

title = 'The "os.path.isdir/file" commands'
headline(title)
print('Is ' + os.getcwd() + ' a directory?', os.path.isdir(os.getcwd()))
print('Is ' + os.getcwd() + '/code12.py a directory?', os.path.isdir(os.getcwd() + '/code12.py'))
print('Is ' + os.getcwd() + ' a file?', os.path.isfile(os.getcwd()))
print('Is ' + os.getcwd() + '/code12.py a file?', os.path.isfile(os.getcwd() + '/code12.py'))

title = 'The "open()" command'
headline(title)
helloFile = open(os.getcwd() + '/hello.txt', 'r')
helloContent = helloFile.read()
print('"hello.txt" content:', helloContent)
helloFile.close()

brassensFile = open('brassens-idees.txt', 'r')
print(brassensFile.readlines())
brassensFile.close()

def lire(var_name, file_name):
    var_name = open(file_name, 'r')
    result = var_name.read()
    var_name.close()
    print('Contenu de votre fichier :\n', result)

print('Premier appel de la fonction "lire"')    
lire(helloFile, 'hello.txt')

def ecrire(var_name, file_name):
    print('Voulez-vous écraser ou ajouter à la suite ?')
    erase = input('Taper "w" pour écraser\nTaper "a" pour ajouter\n')
    var_name = open(file_name, erase)
    text = input('Sasir votre texte :\n')
    
    print('Faut-il aller à la ligne après le texte ?')
    retour = input('Taper "Y" pour oui (yes)\nTaper "N" pour non\n')
    if retour == 'Y':
        var_name.write(text + '\n')
    else:
        var_name.write(text)
        
    var_name.close()

# print('Premier appel de la fonction "écrire"')        
# ecrire(helloFile, 'hello.txt')
# print('Deuxième appel de la fonction "lire"')    
# lire(helloFile, 'hello.txt')

# print('Deuxième appel de la fonction "écrire"')    
# ecrire(helloFile, 'hello.txt')
# print('Troisième appel de la fonction "lire"')    
# lire(helloFile, 'hello.txt')

title = 'The "shelve" module'
headline(title)
import shelve
shelfFile = shelve.open('mydata')
cryptos = ['Bitcoin', 'Ethereum', 'Komodo']
shelfFile['cryptos'] = cryptos
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cryptos'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print('keys:', list(shelfFile.keys()))
print('values:', list(shelfFile.values()))
shelfFile.close()


title = 'The "pprint" module'
headline(title)
import pprint
cryptos = [{'name': 'Bitcoin', 'abbv': 'BTC'},
           {'name': 'Ethereum', 'abbv': 'ETH'},
           {'name': 'Komodo', 'abbv': 'KMD'}]
print(pprint.pformat(cryptos))
fileObj = open('myCryptos.py', 'w')
fileObj.write('cryptos = ' + pprint.pformat(cryptos) + '\n')
fileObj.close()

import myCryptos
print(myCryptos.cryptos)
print(myCryptos.cryptos[0])
print(myCryptos.cryptos[0]['name'])
