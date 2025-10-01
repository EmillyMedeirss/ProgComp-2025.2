#Solicite ao usuário uma temperatura em graus Celsius.
#Converta para Fahrenheit.

celsius = float(input('Informe a temperatura atual em graus Celsius'))

fahrenheit = celsius * 9 /5 + 32

print(f'A temperatura atual está por volta de {celsius:.1f}°C e {fahrenheit}°F.')