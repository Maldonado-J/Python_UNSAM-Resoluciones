#--------------------Ejercicio 1.18: rustico------------------------
cadena = 'Geringoso'
capadepenapa = ''
vocales = 'aeiou'

for c in cadena:
    capadepenapa += c
    if c in vocales:
        capadepenapa += 'p'+c

print(capadepenapa)