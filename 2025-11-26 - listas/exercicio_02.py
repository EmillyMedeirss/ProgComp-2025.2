'''
   Faça um programa que solicite 5 nomes de alunos e suas respectivas notas da 
   etapa 1 e da etapa 2.

   Armazene essas informações em listas separadas.
      - Nomes dos alunos -> lstNomes
      - Notas da etapa 1 -> lstNotas1
      - Notas da etapa 2 -> lstNotas2
   
   Após a entrada dos dados, o programa deve calcular a média (IFRN) de cada aluno e 
   armazená-la em uma nova lista.
      - Médias dos alunos -> lstMedias

   A média deve ser calculada pela fórmula:
      Média = (Nota Etapa 1 * 2) + (Nota Etapa 2 * 3) / 5

   No final, imprima o nome de cada aluno junto com suas notas e suas médias.

   Exemplo:
      Nome do Aluno          Etapa 1    Etapa 2    Média
      --------------------------------------------------
      João Silva             75         80         78
      Maria Oliveira         90         85         88
      Pedro Santos           60         70         65
      Ana Costa              85         90         88
      Lucas Pereira          70         75         73
      --------------------------------------------------
'''


lstNomes = []
lstNotas1 = []
lstNotas2 = []
lstMedia = []
alunos = 5

print(f"--- Entrada de Dados para {alunos} Alunos ---")

for i in range(alunos):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    lstNomes.append(nome)  

    while True:
        try:
            nota1 = float(input(f"Digite a nota da Etapa 1 de {nome}: "))
            if 0 <= nota1 <= 100: 
                lstNotas1.append(nota1)
                break 
            else:
                print("Nota inválida. Digite um valor entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            