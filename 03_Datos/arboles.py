#%%
import csv
pathArbolada = '../Data/arbolado-en-espacios-verdes.csv'

#%% 3.18 leer_parque
def leer_parque(archivo, nombreParque):
    arbParque = []
    with open(archivo, 'rt', encoding='UTF-8') as f:
        filas = csv.reader(f)
        header = next(filas)
        for fila in filas:
            arbol = dict(zip(header, fila))
            if arbol['espacio_ve'].lower() == nombreParque.lower():
                altura = arbol['altura_tot']
                inclinacion = arbol['inclinacio']
                arbol['altura_tot'] = float(altura)
                arbol['inclinacio'] = float(inclinacion)
                arbParque.append(arbol)
    return arbParque

arbGeneralPaz = leer_parque(pathArbolada, 'General Paz')

len(arbGeneralPaz)  #690
# %% 3.19 Determinar las especies en un parque

def especies(listaArboles):
    """Determina las especies en un parque a partir de una lista"""
    listaEspecies = []
    for arbol in listaArboles:
        especie = arbol['nombre_com']
        listaEspecies.append(especie)
    return set(listaEspecies)

especiesGeneralPaz = especies(arbGeneralPaz)

# %% 3.20 Contar ejemplares por especie
from collections import Counter

def contar_ejemplares(listaArboles):
    contadorEspecie = Counter()
    for arbol in listaArboles:
        especie = arbol['nombre_com']
        contadorEspecie[especie] += 1
    return contadorEspecie

totEspecieGeneralPaz = contar_ejemplares(arbGeneralPaz)
arbLosAndes = leer_parque(pathArbolada, 'ANDES, LOS')
arbCentenario = leer_parque(pathArbolada, 'CENTENARIO')
totEspecieLosAndes = contar_ejemplares(arbLosAndes)
totEspecieCentenario = contar_ejemplares(arbCentenario)

#most_common coinciden con la tabla

# %% 3.21 alturas de una especie en una lista
def obtener_alturas(listaArboles, especie):
    listaAlturas = []
    for arbol in listaArboles:
        especieLista = arbol['nombre_com'].lower()
        if  especieLista == especie.lower():
            altura = arbol['altura_tot']
            listaAlturas.append(altura)
    return listaAlturas

def promedio(lista):
    """Calcular promedio a partir de una lista"""
    totalElementos = len(lista)
    totalSuma = sum(lista)
    return round(totalSuma/totalElementos, 2)

altGeneralPaz = obtener_alturas(arbGeneralPaz, 'Jacarandá')
altCentenario = obtener_alturas(arbCentenario, 'Jacarandá')
altLosAndes = obtener_alturas(arbLosAndes, 'Jacarandá')

print(promedio(altGeneralPaz)) #10.2
print(promedio(altLosAndes)) #10.54
print(promedio(altCentenario)) #8.96

#%% 3.22: Inclinaciones por especie de una lista
def obtener_inclinaciones(listaArboles, especie):
    """Inclinaciones por especie de una lista"""
    listaInclinacion = []
    for arbol in listaArboles:
        especieArbol = arbol['nombre_com'].lower()
        if especieArbol == especie.lower():
            inclinacion = arbol['inclinacio']
            listaInclinacion.append(inclinacion)
    return listaInclinacion

#%% 3.23: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(listaArboles):
    """Especie con el ejemplar mas inclinado en un parque determinado"""
    inclinaciones = {}
    listaEspecie = especies(listaArboles)
    for especie in listaEspecie:
        inclinacionEspecie = obtener_inclinaciones(listaArboles, especie)
        inclinaciones[especie] = max(inclinacionEspecie)
    maxInclinacionKey = max(inclinaciones, key=inclinaciones.get)
    return (maxInclinacionKey, inclinaciones[maxInclinacionKey])

masInclinadoGeneralPaz = especimen_mas_inclinado(arbGeneralPaz)
masInclinadoLosAndes = especimen_mas_inclinado(arbLosAndes)
masInclinadoCentenario = especimen_mas_inclinado(arbCentenario)

#%% 3.24: Especie más inclinada en promedio

def especie_promedio_mas_inclinada(listaArboles):
    inclinaciones = {}
    listaEspecie = especies(listaArboles)
    for especie in listaEspecie:
        inclinacionEspecie = obtener_inclinaciones(listaArboles, especie)
        inclinaciones[especie] = promedio(inclinacionEspecie)
    maxInclinacionKey = max(inclinaciones, key=inclinaciones.get)
    return (maxInclinacionKey, inclinaciones[maxInclinacionKey])

maxPromGeneralPaz = especie_promedio_mas_inclinada(arbGeneralPaz)
maxPromLosAndes = especie_promedio_mas_inclinada(arbLosAndes)
maxPromCentenario = especie_promedio_mas_inclinada(arbCentenario)
# %%
