#%% 2.3 precio de la naranja
with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.strip('\n').split(',')
        if row[0].lower() == 'naranja':
            precio_u = float(row[1])
            print(f'[{row[0]:^12s}]: {precio_u:.2f}')

#%% 2.7 buscar_precio(fruta)
def buscar_precio(fov):
    precio_u = False
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.strip('\n').split(',')
            if row[0].lower() == fov.lower():
                precio_u = float(row[1])
                print(f'[{fov:^12s}]: {precio_u}')  
        if precio_u is False:
            print(f'{fov} no figura en el listado de precios')
    
fov = input('Ingresar fruta o verdura:')
buscar_precio(fov)
# %%
