'''
   Desenvolva um código em Python que solicite ao usuário que informe os 
   comprimentos dos três lados de um triângulo. 
   
   Em seguida, verifique se esses comprimentos podem formar um triângulo. 
   Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e 
   classifique-o quanto aos lados e aos ângulos.

   Instruções:
      - Peça ao usuário para inserir os comprimentos dos três lados do triângulo;
      - Verifique se os comprimentos fornecidos podem formar um triângulo. 
        Caso contrário, informe que não é possível formar um triângulo com esses lados;
      - Se for possível formar um triângulo, calcule os três ângulos do triângulo;
      - Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) 
        e aos ângulos (agudo, obtuso ou retângulo);
      - Exiba a classificação do triângulo quanto aos lados e aos ângulos.

   Observações:
      - Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, 
        é necessário verificar a seguinte condição: A soma de quaisquer dois lados de 
        um triângulo deve ser sempre maior que o terceiro lado;
      - Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo;
      - Para classificar quanto aos lados, verifique se os três lados são iguais 
        (equilátero), se dois lados são iguais (isósceles) ou se todos os lados são 
        diferentes (escaleno);
      - Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 
        90 graus (obtuso), se um dos ângulos é igual a 90 graus (retângulo) 
        ou se todos os ângulos são menores que 90 graus (agudo);
      - Considere que os ângulos são expressos em graus.

   Dica: Utilize a biblioteca math.
'''
import sys
import math 

try:
   fltLadoA = float(input('Informe o comprimento do lado A do triângulo:'))
   fltLadoB = float(input('Informe o comprimento do lado B do triângulo:'))
   fltLadoC = float(input('Informe o comprimento do lado C do triângulo:'))
except ValueError:
    sys.exit('ERRO: você deve informar apenas valores númericos.')
except Exception as strERRO:
    sys.exit(f'ERRO INESPERADO: {strERRO}')
else:
   if fltLadoA <= 0 or fltLadoB <= 0 or fltLadoC <= 0:
    sys.exit('ERRO: Os lados do triângulo devem ser números positivos.')
    
   if (fltLadoA + fltLadoB <=fltLadoC) or (fltLadoA + fltLadoC <= fltLadoB) or (fltLadoB + fltLadoC <= fltLadoA):
     sys.exit(f'INVÁLIDO! Não é possível formar um triângulo com esses comprimentos.')

RAD_a = math.acos((fltLadoB**2  + fltLadoC**2 - fltLadoA**2) / (2 * fltLadoB * fltLadoC))
RAD_b = math.acos((fltLadoA**2  + fltLadoC**2 - fltLadoB **2) / (2 * fltLadoA * fltLadoC))

fltAngA = round (math.degrees(RAD_a),5)
fltAngB = round (math.degrees(RAD_b),5)

# Calculando o ângulo C
fltAngC = round( 180 - fltAngA - fltAngB, 3)

print(f'Valores dos ângulos do triângulo: {fltAngA:.2f}, {fltAngB:.2f}, {fltAngC}.')

if fltLadoA == fltLadoB and fltLadoB == fltLadoC:
   print('Classificação quanto aos lados: EQUILÁTERO.')
elif fltLadoA == fltLadoB or fltLadoA == fltLadoC or fltLadoB == fltLadoC:
   print('Classificação quanto aos lados: ISÓCELES.')
else:
   print('Classificação quanto aos lados: ESCALENO.')

if fltAngA >90 or fltAngB >90 or fltAngC >90:
      print('Classificação quanto aos ângulos: OBTUSO.')
elif fltAngA ==90 or fltAngB ==90 or fltAngC ==90:
      print('Classificação quanto aos ângulos: RETÂNGULO.')
else:
      print('Classificação quanto aos ângulos: AGUDO.')


