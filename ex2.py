#Exercicio 2 Tabuada


input_num = int(input("Digite um número para ver sua tabuada: "))
contador = 1
while contador <= 10:
    resultado = input_num * contador
    print(f"{input_num} x {contador} = {resultado}")
    contador += 1
    