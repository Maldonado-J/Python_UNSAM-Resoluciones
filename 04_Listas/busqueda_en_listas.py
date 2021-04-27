#%% 4.3: Búsquedas de un elemento

def buscar_u_elemento(lista, elemento):
    indice = -1
    for i, item in enumerate(lista):
        if elemento == item:
            indice = i
    return indice

print(buscar_u_elemento([1,2,3,2,3,4],1))   #0
print(buscar_u_elemento([1,2,3,2,3,4],2))   #3
print(buscar_u_elemento([1,2,3,2,3,4],3))   #4
print(buscar_u_elemento([1,2,3,2,3,4],5))   #-1

def buscar_n_elemento(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador+=1
    return contador

#%% 4.4: Búsqueda de máximo y mínimo

def maximo_positivos(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

print(maximo_positivos([1,2,7,2,3,4]))    #7
print(maximo_positivos([1,2,3,4]))        #4
print(maximo_positivos([-5,4]))           #4
print(maximo_positivos([-5,-4]))          #0

#El ultimo caso falla porque no contempla valores en negativo porque inicia en 0. En el caso anterior
#estaba el 4 (positivo) y de hecho es lo que retorna como valor maximo

#%% version mejorada del 4.4. contempla negativos

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] #inicializo m como el primer valor
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e #valga la redundancia
    return m

print(maximo([-5,4,-3]))           #4
print(maximo([-5,-4,-6]))          #-4