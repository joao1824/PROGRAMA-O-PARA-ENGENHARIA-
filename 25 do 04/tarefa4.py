# Para construir o programa a seguir, considere que os usuários só informarão
# números inteiros positivos. Crie um programa que receba 5 números digitados e, ao
# final, exiba a quantidade de números pares.
par = 0
for x in range (5):
    numero = int(input("Numero ==> "))
    if (numero%2) == 0:
        par += 1

print(f"Total de {par} vezes")