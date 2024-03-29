
#Crie um programa em Python para calcular a média de três notas inseridas pelo
#usuário e dar feedback baseado na média calculada.
#Peça ao usuário para inserir as notas de três avaliações.
#Calcule a média das notas e arredonde-a para duas casas decimais.
#Exiba a média na tela.
#Dê um dos seguintes feedbacks de acordo com a média:
#Média maior ou igual a 7.0: "Parabéns! Sua média é alta."
#Média maior ou igual a 5.0: "Sua média é razoável."
#Média abaixo de 5.0: "Sua média é baixa. É uma boa oportunidade para melhorar. 

n1,n2,n3 = float(input("NOTA = ")), float(input("NOTA = ")),float(input("NOTA = "))

media = round( (n1 + n2 + n3) / 3, 2)
print(f"Sua média foi {media}")

if media >= 7.0:
    print("Parabéns! Sua média é alta.")
elif media >= 5.0:
    print("Sua média é razoável.")
elif media < 5.0:
     print("Sua média é baixa. É uma boa oportunidade para melhorar.")