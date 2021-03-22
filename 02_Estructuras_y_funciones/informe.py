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
                try:
                    datos[header[i]] = float(row[i]) #evaluo si puedo pasarlo a float
                except ValueError:
                    datos[header[i]] = row[i] #si no es tipo numerico, no hago conversion
            camion.append(datos)
    return camion

camion = leer_camion('../Data/camion.csv')
# %% 2.17 partiendo de 2.7
import csv

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
#%% 2.18 balance
def balance(camion, precios):
    precio_productor = 0
    precio_venta = 0
    cant_cajon = {}
    for fov in camion: #por cada item en camion [{fov1}, {fov2},...]
        precio_productor += fov['cajones'] * fov['precio']
        cant_cajon[fov['nombre']] = cant_cajon.get(fov['nombre'],0) + int(fov['cajones'])
        #inicializo cant_cajon[key] en 0 si no existe la key, y sino las voy sumando (int)
    for fov in cant_cajon.keys(): 
        precio_venta += precios[fov] * cant_cajon[fov]
    balance = precio_venta - precio_productor
    return precio_productor, precio_venta, balance

produccion, venta, balance = balance(camion, precios)
print(f'Total pagado al productor de frutas: ${produccion:.2f}\nTotal ganado en ventas: ${venta:.2f}')
if balance < 0:
    print(f'Hubo una perdida de: {balance:.2f}')
else:
    print(f'Hubo una ganacia de: ${balance:.2f}')

#Total pagado al productor de frutas: $47671.15
#Total ganado en ventas: $62986.10
#Hubo una ganacia de: $15314.95
# %%
