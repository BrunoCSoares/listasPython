'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos;

a. Calcule e mostre a soma dos valores;

b. Calcule e mostre a média dos valores;

c. Calcule e mostre a quantidade de valores acima da média calculada;

d. Calcule e mostre a quantidade de valores abaixo de sete.
'''

lista_notas = []
qtdAcimMed = 0
qtdAbaiMed = 0

nota = float(input("Digite a nota do aluno (-1 para sair): "))

while (nota != -1):
    if 10 >= nota >= 0:
        lista_notas.append(nota)
    else:
        print("nota inválida")
    nota = float(input("Digite a nota do aluno (-1 para sair): "))

notas_lidas = len(lista_notas)
soma_notas = sum(lista_notas)
media_notas = soma_notas / notas_lidas

for nota in lista_notas:
    if nota > media_notas:
        qtdAcimMed += 1
    elif nota < 7.0:
        qtdAbaiMed += 1

print(f"A quantidade de valores lidos foi {notas_lidas}")
print(f"A soma das notas é {soma_notas:.2f}")
print(f"A média das notas é {media_notas:.2f}")
print(f"A quantidade de notas acima da média é {qtdAcimMed}")
print(f"A quantidade de motas abaixo de 7 é {qtdAbaiMed}")