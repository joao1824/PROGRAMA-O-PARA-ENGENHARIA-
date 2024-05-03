# Crie um programa em linguagem Python que leia 4 números, calcule e mostre a
# média aritmética dos valores lidos.
quantidade = 0
soma = 0
for numero in range(4):
    numb = float(input("Digite um nuemro ==> "))
    quantidade += 1
    soma = soma + numb

mediaari = soma/quantidade
print(f"média aritmética dos valores lidos é {mediaari}")
    