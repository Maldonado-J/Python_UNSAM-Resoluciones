#%% 4.5: Invertir una lista

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e]+invertida
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
#[5, 4, 3, 2, 1]
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
#['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
