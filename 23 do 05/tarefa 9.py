# 9 – Desenvolva um código em Python que adicione em um dicionário “d” os
# seguintes campos: nome, idade, endereço e telefone e mostre os dados no
# final.

dic = {}

while True:
    n = input("Nome ==> ")
    i = int(input("Idade ==> "))
    e = input("Endereço ==> ")
    t = input("Telefone ==> ")
    dic.update({"nome" : n})
    dic.update({"idade" : i})
    dic.update({"endereço" : e})
    dic.update({"telefone" : t})
    break

print(dic)
