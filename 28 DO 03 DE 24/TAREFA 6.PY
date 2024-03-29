#Um posto de abastecimento está comercializando combustíveis com a seguinte
#tabela de descontos:
#Álcool: até 20 litros, desconto de 2% por litro;
 #acima de 20 litros, desconto de 5% por litro;
#Gasolina: até 20 litros, desconto de 4% por litro;
 #acima de 20 litros, desconto de 6% por litro;
#Desenvolva um programa em Python que leia o número de litros vendidos e o tipo de
#combustível (codificado com A – Álcool e G – Gasolina), calcule e imprima o valor a ser
#pago pelo cliente, sabendo que o litro da gasolina está em R$ 5,57 e do álcool R$ 4,98.

tipo = input("Qual o tipo de gasolina (A - ÁLCOOL e G - GASOLINA) = ")
litros =  float(input("Quantos litros ? "))
#
# ÁLCOOL
#
if tipo == "A":
    if litros <= 20:
        resul1 = round(litros * 4.98 - ((litros* 4.98)* 0.02),2)
        print(f"Custo de {litros} litros de álcool é {resul1}")
    elif litros > 20:
        resul1 = round(litros * 4.98 - ((litros* 4.98)* 0.05),2)
        print(f"Custo de {litros} litros de álcool é {resul1}")
#
# GASOLINA
#
elif tipo == "G":
    if litros <= 20:
        resul1 = round(litros * 5.57 - ((litros* 5.57)* 0.04),2)
        print(f"Custo de {litros} litros de gasolina é {resul1}")
    elif litros > 20:
        resul1 = round(litros * 5.57 - ((litros* 5.57)* 0.06),2)
        print(f"Custo de {litros} litros de gasolina é {resul1}")

else :
    print("Entrada não esta de acordo com G e A")

