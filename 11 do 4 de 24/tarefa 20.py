#  Desenvolva um script em linguagem Python que peça os 3 lados de um triângulo. O
# programa deverá informar se os valores podem formar um triângulo. Indique, caso os
# lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o
# terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

lado1 = float(input("LADO 1 => "))
lado2 = float(input("LADO 2 => "))
lado3 = float(input("LADO 3 => "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1:
    print("forma um triangulo")
    if lado3 == lado2 == lado1 :
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Triângulo Isósceles")
    elif lado1 != lado2 != lado3 :
        print("Triângulo Escaleno")
else:
    print("Não forma um triangulo")