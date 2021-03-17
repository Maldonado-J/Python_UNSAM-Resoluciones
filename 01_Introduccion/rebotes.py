#------------Ejercicio 1.5: rebotes.py v1 - --------------

#Una pelota de goma es arrojada desde una altura de 100 metros,
#cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
#Imprimi una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

fraccion = 3/5
pelota_y = altura_inicial = 100
for i in range(1, 11):
    pelota_y = pelota_y * fraccion
    print(i, pelota_y)