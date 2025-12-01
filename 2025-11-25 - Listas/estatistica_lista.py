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

#intQtValores = 20
lstValores = [2, 9, 8, 5]

#MEDIA
media = sum(lstValores)/len(lstValores)

#MEDIANA 

lstOrdenada = sorted(lstValores)
if len (lstValores) % 2 != 0:
    mediana = lstValores[len(lstValores//2)]
else:
    mediana = (lstValores[len(lstValores)//2-1] + lstValores [len(lstValores)//2])/2

print(mediana)

#Variância

fltVariancia = 0
for valor in lstValores:
    fltVariancia += (valor-media)**2
fltVariancia /= len(lstValores)

print(fltVariancia)

#DesvioPadrao

