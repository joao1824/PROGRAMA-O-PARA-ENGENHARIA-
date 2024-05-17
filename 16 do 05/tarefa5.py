# 5 – Desenvolva um script em linguagem Python, utilizando Dicionários, que
# solicite ao usuário inserir o nome de três produtos de mercado e seus
# respectivos preços e os mostre na tela.

produtos = {}

for x in range(3):
    produto = str(input("Nome do produto ==> "))
    valor = float(input("Valor do produto ==> "))
    produtos.update({produto : valor})
    print(produtos)