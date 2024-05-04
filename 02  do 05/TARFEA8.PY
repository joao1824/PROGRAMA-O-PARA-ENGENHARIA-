# Em uma eleição existem quatro candidatos. Os votos são informados por meio
# de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte
# codificação:
# - 1, 2, 3, 4 = voto para os respectivos candidatos;
# - 5 = voto nulo;
# - 6 = voto em branco;
# Elabore um script em linguagem Python que leia o código do candidato em um
# voto. Calcule e mostre:
# - total de votos para cada candidato;
# - total de votos nulos;
# - total de votos em branco;
# Como finalizador do conjunto de votos, tem-se o valor 0.

print("/ (0) SAIR / (1) João / (2) Davi / (3) Jorge / (4) Marcela / (5) NULO / (6) VOTO EM BRANCO")
joao,davi,jorge,marcela,nulo,branco = 0,0,0,0,0,0
while True:
    voto =  int(input("Seu voto ==> " ))
    if voto == 1:
        joao +=1
    elif voto == 2:
        davi +=1
    elif voto == 3:
        jorge +=1
    elif voto == 4:
        marcela +=1
    elif voto == 5:
        nulo +=1
    elif voto == 6:
        branco +=1
    elif voto == 0:
        break 
    else:
        print("Voto sem informção")

print(f"//João teve {joao} votos")
print(f"//Davi teve {davi} votos")
print(f"//Jorge teve {jorge} votos")
print(f"//Marcela teve {marcela} votos")
print(f"//Teve {nulo} votos nulo")
print(f"//Teve {branco} votos em branco")