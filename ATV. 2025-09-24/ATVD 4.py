#Peça ao usuário a distância percorrida (em km) e o tempo gasto (em horas).
#Calcule a velocidade média e exiba o resultado.

distancia  = float(input('Qual a distância percorrida em KM?'))
horas      = float(input('Quanto tempo foi gasto em horas?'))

velocidade = distancia / horas 

print(f'A velocidade média foi de {velocidade:.2f}km/h.')
