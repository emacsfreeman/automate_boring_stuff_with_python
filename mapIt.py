#! python3
# mapIt.py - Launches a map in the browser
#            using an address from the
#            command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

while True:    
    print('Which website would you like to access to?')
    menu = ''' 
              1) Google Maps
              2) Amazon.fr
              3) YouTube
              4) Google traduction (EN -> FR)
              5) Google traduction (FR -> EN)
              q) Quit
           '''
    print(menu)
    choice = input('Your choice: ')
    if choice == '1':
        webbrowser.open('https://www.google.com/maps/place/' + address)
    elif choice == '2':
        webbrowser.open('https://www.amazon.fr/s/ref=nb_sb_noss_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=' + address)
    elif choice == '3':
        webbrowser.open('https://www.youtube.com/results?search_query=' + address)
    elif choice == '4':
        address = address.split()
        address = '%20'.join(address)
        webbrowser.open('https://translate.google.com/?hl=fr#en/fr/' + address)
    elif choice == '5':
        address = address.split()
        address = '%20'.join(address)
        webbrowser.open('https://translate.google.com/?hl=fr#fr/en/' + address)
    elif choice == 'q':
        break
    else:
        print('Incorrect entry')
