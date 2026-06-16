# codigo para ler um numero positivo e imprimir o intervalo de 1 até o numero escolhido


num = int(input("Digite um numero: "))
indice = 1

while num <= 0:
    print("Número invalido, digite um número positivo.")
    num = int(input("Digite um numero: "))
while indice <= num:
    print(indice)
    indice += 1