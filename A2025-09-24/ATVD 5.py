#Peça ao usuário o valor da conta e a porcentagem de gorjeta que deseja dar.
#Calcule o valor total a pagar e exiba com uma mensagem.

conta = float(input("Digite o valor da conta: R$ "))
gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))

valor_gorjeta = conta * (gorjeta / 100)

total = conta + valor_gorjeta


print(f"Total a pagar: R$ {total:.2f}")