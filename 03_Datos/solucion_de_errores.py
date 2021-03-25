#%% 3.1 Semántica

#Error:                              #Solucion: 
# no recorre toda la expresion  ->      saco return false (caso else) y aumento el contador
#                                       pongo el return false fuera del while
# no contempla 'A'              ->      agrego un lower() para validar 'A'
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False
        
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
"""
#%% 3.2 Sintaxis

#Error:                              #Solucion: 
# mal definicion funcion    ->          agrego ':'
# error en while            ->          idem
# error en if               ->          idem
# asignacion en vez de equidad  ->      cambio '=' por '=='
# no contempla 'A'          ->          agrego lower()
# error tipeo               ->          cambio 'Falso' por 'False'

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
#%% 3.3 Tipos
""" codigo con error
"""

#Solucion
#%% 3.4 Alcances
""" codigo con error
"""

#Solucion
#%% 3.5 Pisando memoria
""" codigo con error
"""

#Solucion