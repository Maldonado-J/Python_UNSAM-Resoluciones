#%% 4.6: Propagación
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e]+invertida
    return invertida

def propagar(vector):
    propagado = vector.copy()
    maxlen = len(propagado)
    for ind, fosf in enumerate(propagado):
        if fosf == 0:
            if ind+1<maxlen and propagado[ind+1]==1:
                subvector = invertir_lista(propagado[:ind+2])
                propIzq = propagar(subvector)
                propagado = invertir_lista(propIzq)+propagado[ind+2:]
            if ind-1>=0 and propagado[ind-1]==1:
                propagado[ind] = 1
    return propagado

print(propagar([ 0, 0, 0, 1, 0, 0]))
              #[ 1, 1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
              #[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]

# %%
