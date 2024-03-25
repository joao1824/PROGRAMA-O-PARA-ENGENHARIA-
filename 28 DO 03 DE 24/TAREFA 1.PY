#Desenvolva um script que solicite dois números quaisquer e mostre o maior entre eles


n_1 = (input("Digite um numero - "))
n_2 = (input("Digite um numero - "))

if (n_1 > n_2):
    print(f"{n_1} é maior que {n_2}")
elif (n_1 < n_2):
    print(f"{n_2} é maior que {n_1}")
elif (n_1 == n_2):
    print(f"{n_1} tem o mesmo valor de {n_2}")

