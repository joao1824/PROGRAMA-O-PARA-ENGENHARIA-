# Faça um programa que apresente um menu de opções para o cálculo das
# seguintes operações entre dois números:
# • adição (opção 1)
# • subtração (opção 2)
# • multiplicação (opção 3)
# • divisão (opção 4)
# • saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a
# exibição do resultado e a volta ao menu de opções. O programa somente termina
# quando for escolhida a opção de saída (opção 5)


aux = 1
while aux == 1:
    ent = int(input(('\n • adição (opção 1) \n • subtração (opção 2) \n • multiplicação (opção 3) \n • divisão (opção 4) \n • saída (opção 5) ecolha =>  ')))
    num1,num2 = float(input("NUMERO (1) ==> ")), float(input("NUMERO (2) ==> "))
    if ent == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif ent == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif ent == 3:
        print(f"{num1} X {num2} = {num1 * num2}")
    elif ent == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif ent == 5:
        print("Saindo")
        break