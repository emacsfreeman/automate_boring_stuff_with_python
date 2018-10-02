# Regular expressions

print('=' * 60)
print('Sans les regex')
print('=' * 60)
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

print('=' * 60)
print('Avec les regex')
print('=' * 60)
import re

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print('=' * 60)
print('Avec les groupes')
print('=' * 60)

phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Groupe 1 :', mo.group(1))
print('Groupe 2 :', mo.group(2))
print('Groupe 0 :', mo.group(0))
print('Groupes :', mo.groups())
areaCode, mainNumber = mo.groups()
print('Code de la zone :', areaCode)

print('=' * 60)
print('Avec les parenthèses')
print('=' * 60)

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

print('=' * 60)
print('Avec les pipes')
print('=' * 60)

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print('Groupe 1 :', mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print('Groupe 2 :', mo2.group())


print('=' * 60)
print('Avec le même début')
print('=' * 60)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print('Groupe 0 :', mo.group(0))
print('Groupe 1 :', mo.group(1))

print('=' * 60)
print("Avec l'option '?'")
print('=' * 60)

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

print('=' * 60)
print("Avec l'option '*'")
print('=' * 60)

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

print('=' * 60)
print("Avec l'option '+'")
print('=' * 60)

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)


print('=' * 60)
print("Avec les accolades '{,}'")
print('=' * 60)

print('Greedy')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHa')
print(mo1.group())

mo2 = greedyHaRegex.search('Ha')
print(mo2 == None)

print('Non greedy')
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo3 = nonGreedyHaRegex.search('HaHaHaHa')
print(mo3.group())

print('=' * 60)
print("Avec la méthode 'findall()'")
print('=' * 60)

print('Sans groupe')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

print('Avec groupes')
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

print('-' * 60)

characters = {
    '\\d': 'Tout chiffre entre 0 et 9',
    '\\D': 'Tout sauf un chiffre',
    '\\w': 'Toute lettre, chiffre ou underscore',
    '\\W': 'Tout caractère qui n\'est pas une lettre, un nombre\n \tou underscore',
    '\\s': 'Tout espace, toute tabulation, ou nouvelle ligne.',
    '\\S': 'Tout caractère qui n\'est pas un espace, une\n \ttabulation ou une nouvelle ligne'
    }

for k,v in characters.items():
    print(k + ' : ' + v)
    
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('Hello world!') == None)
print(beginsWithHello.search('He said hello world!') == None)


endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)

print('=' * 60)
print("Avec l'option '.'")
print('=' * 60)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Laurent Last Name: Garnier')
print(mo.group(1))
print(mo.group(2))

print('non greedy')
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

print('greedy')
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Liberté\nEgalité\nFraternité').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Liberté\nEgalité\nFraternité').group())

print('=' * 60)
symbols = {
    '?    ': '0 ou 1 correspondance du groupe précédent',
    '*    ': '0 ou plus correspondance du groupe précédent',
    '+    ': '1 ou plusieurs correspondances du groupe précédent',
    '{n}  ': 'exactement n correspondances du groupe précédent',
    '{n,} ': 'n ou plus correspondances du groupe précédent',
    '{,m} ': 'au plus m correspondances du groupe précédent',
    '{n,m}': 'au moins n et au plus m correspondances',
    '^truc': 'la chaîne doit commencer par \'truc\'',
    'truc$': 'la chaîne doit finir par \'truc\'',
    '.    ': 'correspondance avec n\'importe quel caractère',
    '\d   ': 'digit = chiffre',
    '\w   ': 'word = mot',
    '\s   ': 'space = espace',
    'maj3 ': 'contraire des 3 précédents',
    '[abc]': 'n\'importe quel caractère parmi les 3',
    '[^abc]':'tous les caractères qui NE SONT PAS entre les crochets'
    }

for k,v in symbols.items():
    print(k + ' : ' + v)
  

robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())

namesRegex = re.compile(r'Agent \w+')

print('=' * 60)
print('Substitution')
print('=' * 60)

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # area code
    (\s|-|\.)?                   # separator
    \d{3}                        # first 3 digits
    (\s|-|\.)                    # separator
    \d{4}                        # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

print(phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
