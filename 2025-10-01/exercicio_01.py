'''
   Fazer um programa que solicite ao usuário dois números. Esses números
   correspondem as coordenadas x e y de um ponto em um plano cartesiano.

   Após receber os números, o programa deve informar em qual quadrante
   o ponto se encontra. 

   Lembrete: O plano cartesiano é dividido em quatro quadrantes:
   - Quadrante 1: Ambas as coordenadas (x e y) são positivas;
   - Quadrante 2: A coordenada x é negativa e a coordenada y é positiva;
   - Quadrante 3: Ambas as coordenadas (x e y) são negativas;
   - Quadrante 4: c;
   - Se o ponto estiver sobre um dos eixos (x ou y), o programa deve informar
     que o ponto está sobre o eixo correspondente:
       - Sobre o eixo x: y = 0
       - Sobre o eixo y: x = 0
   - Se o ponto for a origem (0,0), o programa deve informar que o ponto está 
     na origem.
'''

intValor1 = float(input('Informe o valor de x:'))
intValor2 = float(input('Informe o valor de y:'))

if (intValor1 >= 0 and intValor2>=0):
    print('O ponto se encontra no Quadrante 1')
elif (intValor1 <0 and intValor2>0):
    print('O ponto se encontra no Quadrante 2')
elif (intValor1<0 and intValor2<0):
    print('O ponto se encontra no Quadrante 3')
elif (intValor1>0) and (intValor2 <0):
   print('O ponto se encontra no Quadrante 4')
elif (intValor1 == 0) and (intValor2 ==0):
    print('O ponto origem (0,0)')
elif (intValor2 ==0):
    print('O ponto se encontra no eixo X')
else:
    print ('O ponto se encontra no eixo Y')















