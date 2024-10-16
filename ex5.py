'''
Desenvolva um programa que receba 10 números inteiros e os armazene em uma lista. Em seguida, o programa deve encontrar o maior elemento e exibir sua posição (índice) na lista.
'''

lista_numeros = []

for i in range(10):
    lista_numeros.append(int(input("Digite um elemento da lista: ")))

maior = max(lista_numeros)
indice = lista_numeros.index(maior)

print(f"O maior elemento é {maior} e esta no indice {indice}")