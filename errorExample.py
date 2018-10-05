def spam():
    bacon()
def bacon():
    raise Exception('Ceci est un message d\'erreur.')

spam()
