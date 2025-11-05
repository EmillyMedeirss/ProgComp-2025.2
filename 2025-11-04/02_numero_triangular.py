'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é um número triangular ou não.

   Um número triangular é um número que pode ser representado na forma 
   de um triângulo equilátero.

   Os primeiros números triangulares são: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
'''
import sys

try:
 intN = int(input('Digite um número inteiro: '))
except ValueError:
    sys.exit('ERRO: Por favor, digite um número inteiro...')
except Exception as ERROR:
    sys.exit(f'ERRO INESPERADO: {ERROR}')

