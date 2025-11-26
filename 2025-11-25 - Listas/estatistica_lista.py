'''
   A partir da variável intQtValores, gere uma lista com a quantidade de valores 
   inteiros aleatórios entre 1 e 100, sem repetição. 
   
   Em seguida, o programa deve exibir:

   - A lista gerada
   - A soma dos valores na lista
   - A média dos valores na lista
   - O maior valor na lista
   - O menor valor na lista
   - A mediana dos valores na lista
   - A variância dos valores na lista
   - O desvio padrão dos valores na lista
'''
import random 

intQtValores = 20
i = 0
# ------------------------------------------------------------
# Gerando a lista de valores únicos
lstValores = list()

while i <intQtValores:
    x = random.randint (1, 100)
    if x not in lstValores:
        lstValores.append(x)
        i+= 1
print (lstValores)


intSoma = sum(lstValores)
print(f'Soma dos valores.......{intSoma}')

fltMedia = intSoma/len(lstValores)
print(f'Média dos valores.......:{fltMedia:.2f}')

intMaior = max(lstValores)
print(f'Maior valor........:{intMaior}')

intMenor = min(lstValores)
print(f'Menor valor..........: {intMenor}')