#2) Desenvolva um script em linguagem Python que peça as quatro notas de 3
#alunos, calcule e armazene num vetor a média de cada aluno, imprima o
#número de alunos com média maior ou igual a 7

alunos = ["João", "Pedro" , "Ana"]
nota_alta = []
nota_baixa = []

for aluno in alunos:
    nome = aluno
    aluno = []
    print(nome)
    for notas in range(4):
        nota = float(input("Nota do aluno ==> "))
        aluno.append(nota)
    if (sum(aluno)) / 4 < 7:
        nota_baixa.append((sum(aluno)) / 4)
    if (sum(aluno)) / 4 >= 7:
        nota_alta.append((sum(aluno)) / 4)

print(f"O numero de aluno com media maior ou igual a 7 é {len(nota_alta)}")


 

