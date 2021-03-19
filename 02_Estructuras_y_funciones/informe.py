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
# %% 2.17 partiendo de 2.7
import csv

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='UTF-8') as f:
        lines = csv.reader(f)
        next(lines)
        for row in lines:
            try:
                precios[row[0]] = round(float(row[1]), 2)
            except:
                pass
    return precios

precios = leer_precios('../Data/precios.csv')
#%% 2.18 balance
"""
#2.16 camion = leer_camion(camion.csv)
#precios pagados al productor de frutas
precio_productor = 0
for fov in camion:
    precio_productor += int(fov['cajones']) * float(fov['precio'])

#2.17 precios = leer_precios(precios.csv)
#precios de venta
precio_venta = 0
for fov in precios.keys():
    precio_venta += precios[fov]

print(f'Total pagado al productor de frutas: ${precio_productor:.2f}\nTotal ganado en ventas: ${precio_venta:.2f}')
balance = precio_venta-precio_productor
if balance < 0:
    print(f'Hubo una perdida de: {balance:.2f}')
else:
    print(f'Hubo una ganacia de: ${balance:.2f}')
"""
# %%
def balance(camion, precios):
    precio_productor = 0
    precio_venta = 0
    for fov in camion:
        precio_productor += int(fov['cajones']) * float(fov['precio'])
    for fov in precios.keys():
        precio_venta += precios[fov]
    balance = precio_venta - precio_productor
    return precio_productor, precio_venta, balance

produccion, venta, balance = balance(camion, precios)
print(f'Total pagado al productor de frutas: ${produccion:.2f}\nTotal ganado en ventas: ${venta:.2f}')
if balance < 0:
    print(f'Hubo una perdida de: {balance:.2f}')
else:
    print(f'Hubo una ganacia de: ${balance:.2f}')

#Total pagado al productor de frutas: $47671.15
#Total ganado en ventas: $1318.02
#Hubo una perdida de: -46353.13

# %%
