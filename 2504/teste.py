from random import randint
number = -1
number_sort = 1
tentativas = 0
max = 10

while (tentativas < max) and ( number != number_sort ):
    number = int(input("Numero que voçê acha => "))
    if number < number_sort:
        print(f"{number} é menor")
    elif number > number_sort:
        print(f"{number} é maior")
        
    tentativas += 1
    x = 10
    res = x - tentativas
    if res != 0:
        print(f"Você tem mais {res} tentativas")


if number == number_sort:
    print(f"Boa você acertou em {tentativas} tentativas")
elif tentativas == 10:
    print('cabo')