#%% 2.10 commandline costo_camion(nombre_archivo)
import csv
import sys

def costo_camion(nombre_archivo):
    sin_precio = []
    con_precio = []
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        headers = next(lines)
        for row in lines:
            try:
                costo = float(row[1]) * float(row [2])
                costo_total += costo
                con_precio.append(row[0]) #agrego nombre a la lista que tiene precios
            except ValueError:
                sin_precio.append(row[0]) #agrego nombre a la lista que no tiene precios
        return costo_total, con_precio, sin_precio

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo, con_precio, sin_precio = costo_camion(nombre_archivo)
print(f'Costo total de {con_precio}: {costo:.2f}')
if sin_precio: #si no esta vacio
    print(f'Faltan los precios de {sin_precio}')