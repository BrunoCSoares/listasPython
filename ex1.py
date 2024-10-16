'''
Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista. Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas.
'''

lista_numeros = []
lista_par = []
lista_impar = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print("Lista de Números:", lista_numeros)
print("Lista de Números Pares:", lista_par)
print("Lista de Números Ímpares:", lista_impar)
