'''
Faça um programa em Python que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das 2 listas.
'''

lista_A = []
lista_B = []
lista_C = []

for i in range(10):
    lista_A.append(int(input("Digite um elemento da lista A: ")))

for i in range(10):
    lista_B.append(int(input("Digite um elemento da lista B: ")))

for i in range(10):
    lista_C.append(lista_A[i])
    lista_C.append(lista_B[i])

print(lista_A)
print(lista_B)
print(lista_C)