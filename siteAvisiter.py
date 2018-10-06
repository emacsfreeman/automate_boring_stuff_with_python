#! python3
# sitesAvisiter.py - Propose de visiter
#                    les sites web suivants :
# 1) Google Maps 
# 2) Amazon.fr
# 3) YouTube
# 4) Google traduction
# 5) Wikipédia

import webbrowser, sys, pyperclip

# Choisir le type de requête manuel ou presse-papier
def typeOfRequest():
    ''' 
       Cette fonction permet de choisir entre :
       1) Utiliser le presse-papier
       2) Saisir manuellement la requête
    '''
    global address
    print('Choisir le mode de saisie de votre requête :')
    menuR = ''' 
              1) Utiliser le presse-papier
              2) Saisir manuellement la requête
           '''
    print(menuR)
    choixR = input('Votre choix : ')
    if choixR == '2':
        address = input('Saisir votre requête :\n')
    else:
        address = pyperclip.paste()

# Rappeler les langues source et cible
def source_cible(nom_lang, type_lang):
    ''' 
       Affichage du nom de la langue source ou cible
    '''
    if nom_lang == 'en':
        print("La langue " + type_lang + " est l'anglais")
    elif nom_lang == 'fr':
        print("La langue " + type_lang + " est le français")
    elif nom_lang == 'de':
        print("La langue " + type_lang + " est l'allemand")
    elif nom_lang == 'es':
        print("La langue " + type_lang + " est l'espagnol")
    elif nom_lang == 'pt':
        print("La langue " + type_lang + " est le portugais")
    elif nom_lang == 'ru':
        print("La langue " + type_lang + " est le russe")
    elif nom_lang == 'ar':
        print("La langue " + type_lang + " est l'arabe")
    elif nom_lang == 'iw':
        print("La langue " + type_lang + " est l'hébreu")
    elif nom_lang == 'zh':
        print("La langue " + type_lang + " est le chinois")
    else:
        print("La langue " + type_lang + " est inconnue")

# Traitement de la traduction        
def traduction(lang_source, lang_cible):

    # On rappelle à l'utilisateur la langue source
    nom_lang = lang_source
    type_lang = 'source'
    source_cible(nom_lang, type_lang)
    
    # On rappelle à l'utilisateur la langue cible
    nom_lang = lang_cible
    type_lang = 'cible'
    source_cible(nom_lang, type_lang)
    
    global address
    typeOfRequest()
    address = address.split()
    address = '%20'.join(address)
    webbrowser.open('https://translate.google.com/?hl=fr#' + lang_source + '/' + lang_cible + '/' + address)


# Traitement du choix de la langue    
def choix2langue():
    ''' 
        Cette fonction permet :
        1) De choisir le type de langue
        2) De choisir le couplage de langues à traduire
    '''

    global address

    while True:
        print('Choisir le type de langue à traduire :')
        menuT = ''' 
                  1) Langues germaniques
                  2) Langues latines
                  3) Langues slaves
                  4) Langues sémitiques
                  5) Langues asiatiques
                  q) Quitter
               '''
        print(menuT)
        choixT = input('Votre choix : ')
        
        # Groupe des langues germaniques
        if choixT == '1':
            print('Vous avez choisi le groupe des langues germaniques')
            menuG = ''' 
                       1) English -> Français
                       2) Français -> English
                       3) English -> Deutsch
                       4) Deutsch -> English 
                       q) Quitter
                    '''
            print(menuG)
            choixG = input('Votre choix : ')

            # Anglais vers Français
            if choixG == '1':
                lang_source = 'en'
                lang_cible = 'fr'
                traduction(lang_source, lang_cible)
            # Français vers Anglais
            elif choixG == '2':
                lang_source = 'fr'
                lang_cible = 'en'
            # Anglais vers Allemand
            elif choixG == '3':
                lang_source = 'en'
                lang_cible = 'de'
                traduction(lang_source, lang_cible)
            # Allemand vers Anglais
            elif choixG == '4':
                lang_source = 'de'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            elif choixG == 'q':
                break

        # Groupe des langues latines
        if choixT == '2':
            print('Vous avez choisi le groupe des langues latines')
            menuL = ''' 
                       1) English -> Español
                       2) Español -> English
                       3) English -> Português
                       4) Português -> English
                       q) Quitter
                    '''
            print(menuL)
            choixL = input('Votre choix : ')
            # Anglais vers Espagnol
            if choixL == '1':
                lang_source = 'en'
                lang_cible = 'es'
                traduction(lang_source, lang_cible)
            # Espagnol vers Anglais
            elif choixL == '2':
                lang_source = 'es'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            # Anglais vers Portugais
            if choixL == '3':
                lang_source = 'en'
                lang_cible = 'pt'
                traduction(lang_source, lang_cible)
            # Portugais vers Anglais
            elif choixL == '4':
                lang_source = 'pt'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            elif choixL == 'q':
                break

        # Groupe des langues slaves
        if choixT == '3':
            print('Vous avez choisi le groupe des langues slaves')
            menuSl = ''' 
                       1) English -> русский
                       2) русский -> English
                       q) Quitter
                    '''
            print(menuSl)
            choixSl = input('Votre choix : ')
            # Anglais vers Russe
            if choixSl == '1':
                lang_source = 'en'
                lang_cible = 'ru'
                traduction(lang_source, lang_cible)
            # Russe vers Anglais
            elif choixSl == '2':
                lang_source = 'ru'
                lang_cible = 'en'
            elif choixSl == 'q':
                break

        # Groupe des langues sémitiques
        if choixT == '4':
            print('Vous avez choisi le groupe des langues sémitiques')
            menuSem = ''' 
                       1) English -> عربى
                       2) عربى -> English 
                       3) English -> עִברִית
                       4) עִברִית -> English
                       q) Quitter
                    '''
            print(menuSem)
            choixSem = input('Votre choix : ')
            # Anglais vers Arabe
            if choixSem == '1':
                lang_source = 'en'
                lang_cible = 'ar'
                traduction(lang_source, lang_cible)
            # Arabe vers Anglais
            elif choixSem == '2':
                lang_source = 'ar'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            # Anglais vers Hébreu
            elif choixSem == '3':
                lang_source = 'en'
                lang_cible = 'iw'
                traduction(lang_source, lang_cible)
            # Hébreu vers Anglais
            elif choixSem == '4':
                lang_source = 'iw'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            elif choixSem == 'q':
                break

        # Groupe des langues asiatiques
        if choixT == '5':
            print('Vous avez choisi le groupe des langues asiatiques')
            menuAs = ''' 
                       1) English -> 中文
                       2) 中文 -> English
                       q) Quitter
                    '''
            print(menuAs)
            choixAs = input('Votre choix : ')
            # Anglais vers Chinois
            if choixAs == '1':
                lang_source = 'en'
                lang_cible = 'zh-CN'
                traduction(lang_source, lang_cible)
            # Chinois vers Anglais
            elif choixAs == '2':
                lang_source = 'zh-CN'
                lang_cible = 'en'
                traduction(lang_source, lang_cible)
            elif choixAs == 'q':
                break

        elif choixT == 'q':
            break        
    
    
        
while True:    
    print('Which website would you like to access to?')
    menu = ''' 
              1) Google Maps
              2) Amazon.fr
              3) YouTube
              4) Google traduction 
              5) Wikipédia
              q) Quit
           '''
    print(menu)
    choice = input('Your choice: ')
    if choice == '1':
        typeOfRequest()
        webbrowser.open('https://www.google.com/maps/place/' + address)
    elif choice == '2':
        typeOfRequest()
        webbrowser.open('https://www.amazon.fr/s/ref=nb_sb_noss_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords=' + address)
    elif choice == '3':
        typeOfRequest()
        webbrowser.open('https://www.youtube.com/results?search_query=' + address)
    elif choice == '4':
        choix2langue()
    elif choice == '5':
        typeOfRequest()
        webbrowser.open('https://fr.wikipedia.org/wiki/' + address)
    elif choice == 'q':
        break
    else:
        print('Incorrect entry')
