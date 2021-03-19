# %% 2.2 costo_camion.py
#Calcular el precio pagado por los cajones cargados en el camión
f = open('../Data/camion.csv', 'rt')
headers = next(f) #nombre,cajones,precio
costo_total = 0
for line in f:
    row = line.strip('\n').split(',')
    costo = float(row[1]) * float(row [2])
    print(f'[{row[0]:^12s}]: {costo:.2f}')
    costo_total += costo
print('Costo total:', round(costo_total,2))
f.close()

#%% 2.6 costo_camion.py > costo_camion(nombre_archivo)
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        costo_total = 0
        for line in f:
            row = line.strip('\n').split(',')
            costo = float(row[1]) * float(row [2])
            costo_total += costo
        return costo_total

costo = costo_camion('../Data/camion.csv') #47671.15
print(f'Costo total: {costo:.2f}')