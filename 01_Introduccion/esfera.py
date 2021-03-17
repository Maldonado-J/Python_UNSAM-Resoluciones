#------------Ejercicio 1.13----------------
#Calcula e imprime volumen de una esfera de radio r introducida por el usuario

import math

r = input('Introducir radio:')

volumen = (4/3) * math.pi * float(r)**3

print('Volumen de esfera de r='+r+':', volumen)