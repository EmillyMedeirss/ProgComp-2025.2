'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista deve ser [1, 1];
   - Cada nova sub-lista deve ser formada acrescentando ao final da lista anterior 
     a soma dos dois últimos números já existentes;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário.
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 1, 2]
      [1, 1, 2, 3]
      [1, 1, 2, 3, 5]
      [1, 1, 2, 3, 5, 8]
'''
import sys

while True:
    try:
        QtSubLst = int(input('Quantas sublistas você deseja gerar (mínimo 1)?' ))
        if QtSubLst >= 1:
            break
        else:
            print('Por favor, digite um número inteiro maior ou igual a 1.')
    except ValueError:
        sys.exit('Entrada inválida. Digite apenas números inteiros.')
    except Exception as ERROR:
        sys.exit(f'ERRO INESPERADO!!! {ERROR}')


# Inicializa a lista principal
# Ela deve começar obrigatoriamente com a sublista [1, 1]
lstPrincipal = []
subLst = [1,1]

lstPrincipal.append(subLst[:])

if QtSubLst >1:
    for i in range(1, QtSubLst):
        proximoNum = subLst[-1] + subLst[-2]
        subLst.append(proximoNum)
        lstPrincipal.append(subLst[:])

for sublista in lstPrincipal:
    print(sublista)