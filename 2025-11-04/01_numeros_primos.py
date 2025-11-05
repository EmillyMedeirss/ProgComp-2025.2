'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é primo ou não.
'''

'''primeiro numero primo é 2

numero primo só é divisil por 1 por ele mesmo
'''

import sys

try:
 intN = int(input('Digite um número inteiro: '))
except ValueError:
    sys.exit('ERRO: Por favor, digite um número inteiro...')
except Exception as ERROR:
    sys.exit(f'ERRO INESPERADO: {ERROR}')
else:
    if intN < 2:
        sys.exit('Digite um valor inteiro maior do que 2.')
    if (intN % 2 == 0) and (intN % intN == 0):
      print(f'{intN} é um número primo!')
    else:
      print(f'{intN} não é um número primo.')

