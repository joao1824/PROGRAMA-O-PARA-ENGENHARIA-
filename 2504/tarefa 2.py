# Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 à 10. O usuário deve informar
# de qual número ele deseja ver a tabuada.

numero = float(input("Digite um numero => "))
multi = 0

for x in range (11):
    
    print(f"{numero} X {multi} = {numero * multi}")
    multi = multi + 1