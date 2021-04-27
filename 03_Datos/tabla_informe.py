#%%
import csv
from collections import Counter
#2.16 
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        lines = csv.reader(f)
        header = next(lines)
        for row in lines:
            datos = {}
            for i in range(len(header)):
                try:
                    datos[header[i]] = float(row[i]) #evaluo si puedo pasarlo a float
                except ValueError:
                    datos[header[i]] = row[i] #si no es tipo numerico, no hago conversion
            camion.append(datos)
    return camion

camion = leer_camion('../Data/camion.csv')
# 2.17
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='UTF-8') as f:
        lines = csv.reader(f)
        for row in lines:
            try:
                precios[row[0]] = round(float(row[1]), 2)
            except:
                pass
    return precios

precios = leer_precios('../Data/precios.csv')

#3.13 recolectar datos
def hacer_informe(camion, precios):
    informe = []
    cant_cajon = Counter()
    for fov in camion:
        cant_cajon[fov['nombre']] += fov['cajones']
    for fov in camion:
        nombre = fov['nombre']
        diferencia = precios[nombre] - fov['precio']
        tupla = (nombre, cant_cajon[nombre], fov['precio'], diferencia )
        informe.append(tupla)
    return informe

informe = hacer_informe(camion, precios)

#%% 3.14 imprimir tabla con formato
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:<10s} {cajones:>10.0f} {precio:>10.2f} {cambio:>10.2f}')

#%% 3.15 agregar encabezados
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#print(f'{headers[0]:<10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
for i in headers:
    print(f'{i:>10s}', end=' ')
print('\n---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10.0f} {precio:>10.2f} {cambio:>10.2f}')

#%% 3.16 desafio de formato
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
for i in headers:
    print(f'{i:>10s}', end=' ')
print('\n---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    precio = '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10.0f} {precio:>10s} {cambio:>10.2f}')

#%% apto para no hardcodear los dash y dependa de #headers
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
dashline = '----------'

def encabezado(dash=False):
    for i in headers[:-1]:
        if dash:
            print(f'{dashline:>10s}', end=' ')
        else:
            print(f'{i:>10s}', end=' ')
    if dash:
        print(f'{dashline:>10s}')
    else:
        print(f'{headers[-1]:>10s}')

encabezado()
encabezado(dash=True)
for nombre, cajones, precio, cambio in informe:
    precio = '$' + str(precio)
    print(f'{nombre:>10s} {cajones:>10.0f} {precio:>10s} {cambio:>10.2f}')
# %%
