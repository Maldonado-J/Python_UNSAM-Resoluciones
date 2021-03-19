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

#%% 2.3 precio de la naranja
with open('../Data/precios.csv', 'rt') as f:
    headers = next(f) #nombre,cajones,precio
    for line in f:
        row = line.strip('\n').split(',')
        if row[0].lower() == 'naranja':
            precio_u = float(row[1])
            print(f'[{row[0]:^12s}]: {precio_u:.2f}')
# %%
