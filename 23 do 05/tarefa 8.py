# 8 - Construa um script em linguagem Python que utilize um dicionário
# cujas chaves são os códigos do produto e os valores são o nome do
# produto, o preço unitário e a quantidade comprada. A partir do
# dicionário, o programa deve imprimir os itens da compra e calcular o
# subtotal de cada um deles, ou seja, quantidade * preço unitário. Por fim,
# o programa deve apresentar o valor total da compra.

produtos = {}
subtotal = 0
while True:
    codigo = input("Codigo (q = sair )=> ")
    if codigo == "q" or codigo == "Q":
        break
    nome = input("Nome do produto => ")
    valor = float(input("Valor unitario => "))
    quantidade = int(input("Quantidade do produto => "))
    produto = nome
    produto = []
    produto.append(nome)
    produto.append(valor)
    produto.append(quantidade)

    produtos.update({codigo : produto})

for produto in produtos:
    subtotal += (produtos[produto][1]) * (produtos[produto][2])



print(subtotal)
print(produtos)
    