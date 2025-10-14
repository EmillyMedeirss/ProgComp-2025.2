'''
   Crie um programa que calcula o salário semanal de um funcionário.
   
   O programa deve solicitar o número de horas trabalhadas na semana e o 
   valor que ele recebe por hora. A jornada de trabalho padrão é de 40 horas 
   semanais. Horas trabalhadas acima de 40 devem ser pagas com um adicional 
   de 50% (o valor da hora extra é 1.5 vezes o valor da hora normal). 
   
   O programa deve exibir o salário total. 
   
   Garanta que o programa trate o caso de o usuário digitar valores não 
   numéricos.
'''

import sys
# Entrada de dados com tratamento de erro

try: 
    hrs   = int(input('Informe a carga horária semanal:'))
    valor = float(input('Informe o valor recebido por hora trabalhada:'))
# Tratamento de erro para valores não numéricos
except ValueError:
    sys.exit(f'ERRO: digite apenas valores númericos.')
# Tratamento de erro para outros tipos de erro
except Exception as strErro:
    sys.exit (f'ERRO: {strErro}')
# Cálculo do salário caso tenha passado pelas validações
else:
   # Verifica se a quantidade de horas trabalhadas é negativa 
    if hrs <0:
        sys.exit ('ERRO: O número de horas trabalhadas não pode ser negativo.')
        # Verifica se o valor da hora é negativo
    if valor <0:
        sys.exit ('ERRO: O valor da hora não pode ser negativo.')

# Cálculo do salário
intHorasExtras = 0
if hrs > 40:
      intHorasExtras = hrs - 40
      hrs = 40

 # Cálculo do salário
fltSalario = (hrs * valor) + (intHorasExtras * valor * 1.5)

 # Exibição do resultado
print(f'Você trabalhou {hrs + intHorasExtras} horas nesta semana.')
print(f'O valor da sua hora é R$ {valor:.2f}.')
print(f'Seu salário semanal é de R$ {fltSalario:.2f}')

