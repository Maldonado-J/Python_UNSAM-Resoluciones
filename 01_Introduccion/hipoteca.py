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


#------------Ejercicio 1.8: hipoteca.py v2 - --------------
#Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
adelanto = 1000
mes = 1

# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado += pago_mensual
#     if mes < 12 :
#         saldo -=adelanto
#         total_pagado += adelanto
#     mes += 1

#----------------Ejercicio 1.9: hipoteca.py ------------------
#¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado += pago_mensual

#----------------Ejercicio 1.11: bonus ------------------
# el pago del último mes se ajusta a lo adeudado
    if saldo < 0:
        a_favor = saldo #valor en negativo
        saldo = 0
        total_pagado += a_favor #resto lo que pago de mas

#----------------Ejercicio 1.10: tabla ------------------
    #print(mes, round(total_pagado, 2), round(saldo, 2))
#----------------Ejercicio 1.20: f-strings ------------------
    print(f'\t{str(mes):>4s} |\t${total_pagado:0.2f}\t|\t${saldo:0.2f}')
    
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin :
        saldo -=adelanto
        total_pagado += adelanto
    mes += 1

#print('Total pagado en', mes, 'meses:', round(total_pagado, 2))