#Peça ao usuário a distância percorrida (em km) e o tempo gasto (em horas).
#Calcule a velocidade média e exiba o resultado.

distancia  = float(input('Qual a distância percorrida de Natal/RN à João Pessoa/PB?'))
horas      = float(input('Levou quantas horas para essa distância ser percorrida?'))

velocidade = distancia / horas 

print(f'A velocidade média foi de {velocidade:.2f}km/h.')
