'''
Desenvolva um programa que recebe 10 números inteiros e os armazene em uma lista. Em seguida, exiba quantos números múltiplos de 3 ela possui.
'''

numeros = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

multiplos_de_3 = sum(1 for numero in numeros if numero % 3 == 0)

print(f"A lista contém {multiplos_de_3} números múltiplos de 3.")
