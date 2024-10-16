'''
Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas. Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em português nas respectivas posições. A inserção das palavras deverá ser executada até que o usuário digite uma opção de saída 0

(Deseja continuar (1-SIM / 0-NÃO). Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar.
'''

lista_ingles = []
lista_portugues = []

resp = 1

while (resp != 0):
    lista_ingles.append((input("Digite a palavra em inglês: ")))
    lista_portugues.append((input("Digite tradução em português: ")))
    resp = int(input("Deseja continuar? [1-SIM/0-NÃO]: "))
    print("\n")

palavra = input("Digite a palavra em inglês que deseja saber a tradução: ")

if palavra in lista_ingles:
    indice = lista_ingles.index(palavra)
    print(f"\nA tradução da palavra {palavra} para português é {lista_portugues[indice]}")