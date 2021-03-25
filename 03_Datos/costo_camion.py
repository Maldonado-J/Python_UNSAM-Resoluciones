#%% 2.9 csv costo_camion(nombre_archivo)
"""
import csv

def costo_camion(nombre_archivo):
    sin_precio = []
    con_precio = []
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for row in lines:
            try:
                costo = float(row[1]) * float(row [2])
                costo_total += costo
                con_precio.append(row[0])
            except ValueError:
                sin_precio.append(row[0])
        return costo_total, con_precio, sin_precio

costo, con_precio, sin_precio = costo_camion('../Data/missing.csv')
print(f'Costo total de {con_precio}: {costo:.2f}\nFaltan los precios de {sin_precio}')
#Costo total de ['Lima', 'Naranja', 'Caqui', 'Durazno', 'Mandarina']: 30381.15
#Faltan los precios de ['Mandarina', 'Naranja']
"""
#%% 3.8 missing costo_camion(nombre_archivo)
import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for nrow, row in enumerate(lines, start=1):
            try:
                costo = float(row[1]) * float(row [2])
                costo_total += costo
            except ValueError:
                print(f'Fila {nrow}: No pude interpretar: {row}')
        return costo_total

costo = costo_camion('../Data/missing.csv')
print(f'Costo total: {costo:.2f}')
#Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
#Fila 7: No pude interpretar: ['Naranja', '', '70.44']
#Costo total: 30381.15
# %%
