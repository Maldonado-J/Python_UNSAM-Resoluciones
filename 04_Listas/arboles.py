#%%
import csv
pathArbolada = '../Data/arbolado-en-espacios-verdes.csv'

#%% 4.15: Lectura de todos los árboles <- 3.18 leer_parque
def leer_arboles2(archivo):
    with open(archivo, 'rt', encoding='UTF-8') as f:
        filas = csv.reader(f)
        header = next(filas)
        return [{columna: index for columna, index in zip(header, fila)} for fila in filas]

arboleada = leer_arboles2(pathArbolada)

#%% 4.16: Lista de altos de Jacarandá <- 3.21 alturas de una especie en lista
def obtener_alturas(especie, arboleada):
    listaAlturas = [float(arbol['altura_tot']) for arbol in arboleada if arbol['nombre_com'].lower()==especie.lower()]
    return listaAlturas

def promedio(lista):
    """Calcular promedio a partir de una lista"""
    totalElementos = len(lista)
    totalSuma = sum(lista)
    return round(totalSuma/totalElementos, 2)

alturasEspecie = obtener_alturas('Jacarandá', arboleada)

#%% 4.17: Lista de altos y diámetros de Jacarandá
def obtener_alturas_diametros(especie, arboleada):
    return [(float(a['altura_tot']),float(a['diametro'])) for a in arboleada if a['nombre_com'].lower()==especie.lower()]

altDiamEspecie = obtener_alturas_diametros('Jacarandá', arboleada)

#%% 4.18: Diccionario con medidas
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    diccionario = {especie: obtener_alturas_diametros(especie, arboleada) for especie in especies}
    return diccionario

medidasEspecies = medidas_de_especies(especies, arboleada)

print(len(medidasEspecies[especies[0]])) #4112
print(len(medidasEspecies[especies[1]])) #3150
print(len(medidasEspecies[especies[3]])) #3255
# %%
