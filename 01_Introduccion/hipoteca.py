#------------Ejercicio 1.7: hipoteca.py v1 - --------------

#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
#Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))