'''
Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0.
'''

lista_medias = []
qtde_alunos = 0

for i in range(10):
    cp1 = float(input("Digite a nota do CP1: "))
    cp2 = float(input("Digite a nota do CP2: "))
    cp3 = float(input("Digite a nota do CP3: "))
    media = (cp2 + cp2 + cp3) / 3
    lista_medias.append(media)

for media in lista_medias:
    if media >= 7:
        qtde_alunos += 1

print(f"Quantidade de alunos com média maior que 6 {qtde_alunos}")
