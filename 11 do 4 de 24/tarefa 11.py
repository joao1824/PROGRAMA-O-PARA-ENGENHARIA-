#Elabore um script em linguagem Python que determine se um ano introduzido pelo
#usuário é ou não bissexto. Um ano é bissexto se for múltiplo de 4 sem ser de 100 ou se
#for múltiplo de 400.

x = int(input("ano => "))

bis1 = x % 4
bis2 = x % 400
nobis = x % 100


if bis1 == 0 and nobis != 0 or bis2 == 0 :
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

