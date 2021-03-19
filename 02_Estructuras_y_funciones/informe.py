#%% 2.15 partiendo de 2.6
"""
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for row in lines:
            precio = round(float(row[2]),2)
            datos = (row[0], int(row[1]), precio)
            camion.append(datos)
        return camion

camion = leer_camion('../Data/camion.csv')
"""
#%% 2.16 diccionario
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        header = next(lines)
        for row in lines:
            datos = {}
            for i in range(len(header)):
                datos[header[i]] = row[i]
            camion.append(datos)
        return camion

camion = leer_camion('../Data/camion.csv')
# %%
