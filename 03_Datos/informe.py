# 3.9 partiendo de 2.18 balance
#%% parto de 2.16 -> agrego zip y enumerate
import csv
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        header = next(filas)
        for i, fila in enumerate(filas, start=1):
            record = dict(zip(header, fila))
            try:
                record['nombre'] = record['nombre']
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
            except ValueError:
                print(f'Fila {i}: No pude interpretar: {fila}')
            camion.append(record)
    return camion
camion = leer_camion('../Data/fecha_camion.csv')
#%% parto de 2.17 -> sin cambio
import csv
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='UTF-8') as f:
        filas = csv.reader(f)
        for fila in filas:
            try:
                precios[fila[0]] = round(float(fila[1]), 2)
            except:
                pass
    return precios
precios = leer_precios('../Data/precios.csv')
#%% partiendo de 2.18 balance -> sin cambio
# no encontre donde "mejorar" esta funcion con enumerate o zip
# funciona con fecha_camion

def balance(camion, precios):
    precio_productor = 0
    precio_venta = 0
    cant_cajones = {}
    for fov in camion: #por cada dict de fruta o verdura en camion [{fov1}, {fov2},...]
        precio_productor += fov['cajones'] * fov['precio']
        cant_cajones[fov['nombre']] = cant_cajones.get(fov['nombre'],0) + int(fov['cajones'])
        #inicializo cant_cajon[key] en 0 si no existe la key, y sino las voy sumando (int)
    for fov in cant_cajones.keys(): 
        precio_venta += precios[fov] * cant_cajones[fov]
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
