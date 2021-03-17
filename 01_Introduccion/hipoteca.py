#------------Ejercicio 1.7: hipoteca.py v1 - --------------

#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
#Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

# print('Total pagado', round(total_pagado, 2))


#------------Ejercicio 1.8: hipoteca.py v2 - --------------
#Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
adelanto = 1000
mes = 0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado += pago_mensual
    if mes < 12 :
        saldo -=adelanto
        total_pagado += adelanto
    mes += 1

print('Total pagado en', mes, 'meses:', round(total_pagado, 2))