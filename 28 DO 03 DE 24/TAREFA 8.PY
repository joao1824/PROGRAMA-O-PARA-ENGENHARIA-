#Criar um programa em Python que ajuda a verificar se um parafuso está apertado
#orretamente de acordo com o torque especificado. O torque é uma medida de força
#otacional aplicada a um objeto, e é especialmente importante na engenharia mecânica
#para garantir a segurança das montagens.
#Peça ao usuário para inserir o valor do torque aplicado (em Nm).
#Peça ao usuário para inserir o valor do torque de aperto recomendado (em Nm) para o parafuso em questão.
#Compare o torque aplicado com o torque de aperto recomendado.
#Se o torque aplicado estiver dentro de 10% acima ou abaixo do torque recomendado,
#exiba: "O parafuso está apertado corretamente." Caso contrário, exiba: "O parafuso não está apertado corretamente."

to = float(input("o valor do torque aplicado (em Nm) " ))
ta = float(input("o valor do torque de aperto recomendado (em Nm) para o parafuso em questão "))

x_acima = (ta * 0.1) + ta
x_abaixo = ta - (ta * 0.1)

if to > x_abaixo and to < x_acima:
    print("O parafuso está apertado corretamente.")

else :
    print("O parafuso não está apertado corretamente.")