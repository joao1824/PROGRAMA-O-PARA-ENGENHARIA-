# 15 - Elabore um código em Python que leia a temperatura média de cada mês
# do ano e guarde em uma lista. Com isso, efetue a média anual das
# temperaturas e mostre todas que estão acima da média anual e em que mês
# elas ocorreram (Ex.: 1 – Janeiro, 2 – Fevereiro, etc).

meses = ["Janeiro", "Fevereiro", "Março"]
dic = {}
for mes in meses:
    temp = float(input(f"{mes} = temperatura é >> "))
    dic.update({mes:temp})

media = sum(dic.values())/12

aux = 0
for tem,mes in zip(dic.values(),meses):
    if tem > media:
        print(f"acima da média anual = {tem} - {mes}")
    aux += 1
    
    
