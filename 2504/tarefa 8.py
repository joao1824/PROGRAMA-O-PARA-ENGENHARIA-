# Uma empresa, que presta serviço à companhia de energia
# elétrica do estado, necessita de um programa que auxilie os seus
# eletricistas no cálculo das principais grandezas da eletricidade
# que são: Tensão, Resistência e Corrente. Sabe-se que U=Ri, onde,
# U é a Tensão (em V), R é a Resistência (em Ώ) e i a Corrente (em A).
# Você foi contratado(a) pela empresa para atender a essa
# solicitação. Construa um programa que apresente o seguinte
#  menu:
# ************************************************
#        CÁLCULO DE GRANDEZAS ELÉTRICAS
# ************************************************
# 1. Tensão (em Volt)
# 2. Resistência (em Ohm)
# 3. Corrente (em Ampére)
# ************************************************
# Qual grandeza deseja calcular?
# Em seguida, o programa deve solicitar que o eletricista informe o
# valor das outras duas grandezas para realizar o cálculo. Quando o
# eletricista escolher:
# a. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente
# b. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente
# c. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência
# Por fim, o programa deve calcular e apresentar o valor
# encontrado para a grandeza escolhida.

aux = 1
while aux == 1:
    print("*" * 50)
    print("         CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("*" * 50)
    print("1. Tensão (em Volt)")
    print("2. Resistência (em Ohm)")
    print("3. Corrente (em Ampére)")
    print("*" * 50)
    grandeza = int(input("Qual grandeza deseja calcular? ==> "))
    if grandeza == 1:
        r,c = float(input("QUAL É A RESISTÊNCIA? = ")) , float(input("QUAL É A CORRENTE? = "))
        print(f"Tensão (em Volt) = {c * r}V")
        break
    elif grandeza == 2:
        t,c = float(input("QUAL É A TENSÃO? = ")) , float(input("QUAL É A CORRENTE? = "))
        print(f"Resistência (em Ohm) = {t/c}Ώ")
        break
    elif grandeza == 3:
        t,r = float(input("QUAL É A TENSÃO? = ")) , float(input("QUAL É A RESISTÊNCIA? = "))
        print(f"Resistência (em Ohm) = {t/r}A")
        break
    else:
        print("Valor incorreto")