# 13 – Desenvolva um script em linguagem Python, utilizando Dicionários, que
# solicite ao usuário inserir a descrição de dois produtos de mercado e seus
# respectivos preços. Em seguida, mostre na tela o nome do produto mais caro.


dic = {}
for x in range(2):
    descricao = str(input("Descrição do produto => "))
    valor = float(input("Valor do produto => "))
    dic.update({descricao:valor})
    
    
    

print(max(dic, key=produtos.get))
