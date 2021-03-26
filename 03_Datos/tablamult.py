#%% 3.17
rango = 10 #0 a 9

def linedash():
    print('\n--------------------------------------------')

#identacion
print('    ', end='')
#cabecera
for i in range(rango):
    print(f'{i:>3d}', end=' ')

linedash()

for i in range(rango):
    print(f'{i:1d}:', end=' ')
    print('   0', end=' ')
    acumulador = 0
    for n in range(rango-1):
        print(f'{i+acumulador:>3d}', end=' ')
        acumulador += i
    print('\n')