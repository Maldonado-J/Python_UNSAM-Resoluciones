#%% 3.1 Semántica

#Error:                              #Solucion: 
# no recorre toda la expresion  ->      saco return false (caso else) y aumento el contador
#                                       pongo el return false fuera del while
# no contempla 'A'              ->      agrego un lower() para validar 'A'
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False
        
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
"""
#%% 3.2 Sintaxis

#Error:                              #Solucion: 
# mal definicion funcion    ->          agrego ':'
# error en while            ->          idem
# error en if               ->          idem
# asignacion en vez de equidad  ->      cambio '=' por '=='
# no contempla 'A'          ->          agrego lower()
# error tipeo               ->          cambio 'Falso' por 'False'

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
#%% 3.3 Tipos

#Error:                                        #Solucion:
# no puedo aplicar un len() a un int    ->       si es int, tranformarlo a str
""" codigo con error
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene
"""
def tiene_uno(expresion):
    if type(expresion) == int:
        expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%% 3.4 Alcances

#Error:                                     #Solucion:
# falta devolver la funcion a main     ->     agrego return c

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%% 3.5 Pisando memoria

#Error:                                 
    # guardo el mismo reg en camion porque nunca se sobreescribe 
#Solucion:
    # cambio de lugar registro asi se actualiza

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
# %%
