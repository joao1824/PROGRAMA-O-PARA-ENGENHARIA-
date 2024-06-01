# 6 - Dadas duas listas P1 e P2, ambas com n valores reais que representam as
# notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um
# script em linguagem Python que solicite o valor de n, leia as notas e calcule a
# média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
# obteve a melhor média. Exemplo:
# Tamanho da turma: 5
# P1: 7.0 8.3 10.0 6.5 9.3 P2: 8.5 6.9 5.0 7.5 9.8
# Resposta:
# Média da turma na prova 1: 8.22
# Média da turma na prova 2: 7.54
# A turma obteve a melhor média na prova 1.

P1 = [7.0, 8.3, 10.0, 6.5, 9.3] 
P2 = [8.5, 6.9, 5.0, 7.5, 9.8]



print(f"Media da turma 1 = {round(sum(P1)/5,2)}")
print(f"Media da turma 2 = {round(sum(P2)/5,2)}")

if sum(P1)/5 > sum(P2)/5:
    print("Prova 1 com maior nota media da turma")
if sum(P1)/5 < sum(P2)/5:
    print("Prova 2 com maior nota media da turma")