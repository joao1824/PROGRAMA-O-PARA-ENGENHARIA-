# Elabore um programa que leia um número inteiro e indique se o número é primo
# ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele
# mesmo. No entanto, o número 1 não é primo.

numb = int(input("Numero ==> "))
aux = 2

for x in range(9):
    div = numb%aux
    aux += 1
    if numb == 1:
        print("Não é primo")
        break
    elif div != 0 or numb == 2 or numb == 3:
        print("É primo")
        break
    elif numb == aux:
        div = 1     
    elif div == 0 :
        print("Não é primo")
        break