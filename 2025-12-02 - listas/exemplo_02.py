'''
   Escreva um programa que construa uma lista de sub-listas de números inteiros.

   - O usuário deverá informar quantas sub-listas deseja gerar;
   - A primeira sub-lista será obrigatoriamente [1, 1];
   - Cada nova sub-lista deve começar e terminar com o número 1;
   - Os valores internos de cada sub-lista devem ser obtidos somando pares de números 
     vizinhos da sub-lista imediatamente anterior;
   - O processo deve continuar até que seja atingida a quantidade de sub-listas 
     definida pelo usuário;
   - Ao final, o programa deve imprimir todas as sub-listas geradas.

   Exemplo de saída para 5 sub-listas:

      [1, 1]
      [1, 2, 1]
      [1, 3, 3, 1]
      [1, 4, 6, 4, 1]
      [1, 5, 10, 10, 5, 1]
'''

while True:
    try:
        QtSubLst = int(input('Quantas sublistas você deseja gerar (mínimo 1)? '))
        if QtSubLst >=1:
            break
        else:
            print('Por favor, digite um número inteiro maior ou igual a 1.')
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

lstLista = [[1,1]]
intSubLista = []
for _ in range(1, QtSubLst):
  lstSubLista = [1]
  for j in range(len(lstLista[-1] -1)):
    intSoma = lstLista [-1][j]+lstLista[-1][j+1]
    lstSubLista.append(intSoma)

intSubLista.append(1)
lstLista.append(lstSubLista)
