#%% 2.14
#Funcion que a partir de una lista de palabras, devuelva un diccionario geringoso
def geringar(palabra):
    vocales = 'aeiou'
    papalapabrapa = ''
    for c in palabra.lower():
        papalapabrapa += c
        if c in vocales:
            papalapabrapa += 'p'+c
    return papalapabrapa

def dipiccipioponaparipiopo(lista):
    diccionario = {}
    for p in lista:
        diccionario[p] = geringar(p)
    return diccionario

lipistapa = dipiccipioponaparipiopo(['banana', 'manzana', 'mandarina'])
