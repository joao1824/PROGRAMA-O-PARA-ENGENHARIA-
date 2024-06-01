# 3 - Desenvolva um script em linguagem Python que peça as quatro
# notas de 3 alunos, calcule e armazene em uma lista a média de cada
# aluno, imprima o número de alunos com média maior ou igual a 7.

alunos = ["João", "Felipe", "André"]
nota_alta = []
nomes = []
for aluno in alunos:
    nome = aluno
    aluno = []
    for x in range(4):
        nota = float(input(f"Nota do {nome} = "))
        aluno.append(nota)
    if (sum(aluno)/4) >= 7:
        nota_alta.append(sum(aluno)/4)
        nomes.append(nome)
        

print(f"O Numero de alunos com nota maior ou igual a 7 são \{len(nota_alta)}/ ")
print(f"Alunos que passaram = {nomes}")