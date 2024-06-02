# 14 - Desenvolver um script em linguagem Python que leia nome, altura e peso
# de 3 pessoas. Este programa deverá armazená-los em um Dicionário, bem
# como calcular e mostrar:
# a. A menor altura do grupo;
# b. O peso médio do grupo;
# c. Uma lista dos nomes das pessoas em ordem alfabética

dic = {}
soma_peso = 0
for x in range(3):
    nome = str(input("Nome => "))
    altura = float(input("Altura => "))
    peso = float(input("Peso => "))
    soma_peso += peso
    x = []
    x.append(altura)
    x.append(peso)
    dic.update({nome:x})


print(min(dic, key=lambda k:dic[k][0]))
print(f"Peso médio do grupo = {round(soma_peso/3,2)}")
print(f"Nomes em ordem alfabetica = {sorted(dic)}")
