#Peça ao usuário um valor em reais (R$) e a cotação do dólar.
#Calcule e exiba quantos dólares ele teria com esse valor.

reais = float(input('Quanto custa um iPhone 16 em reais?'))
dólar = float(input('Qual a cotação atual do dólar?'))

resultado =  reais / dólar 

print(f'O preço de um iPhone 16 em dólar custa cerca de US$ {resultado:.2f}.')