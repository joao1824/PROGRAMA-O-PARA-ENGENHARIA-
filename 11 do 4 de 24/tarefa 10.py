# Escreva um script em linguagem Python para ler um número de unidade de
#comprimento (um fracionário) e mostre a área do círculo deste raio. Assuma com valor
#do pi 3.14159 (uma apropriada declaração deve ser dada a esta constante). A saída deveria
#ter a seguinte forma:
#A área do círculo de raio ___ unidades e ___ unidades.
#Se você desejar melhorar este código, exiba a mensagem: Erro: valores negativos não são
#permitidos. Se o valor de estrada for negativo.

raio1 = float(input("Valor do raio => "))

area1 = (raio1 ** 2) * 3.14159

if area1 >= 0 :
    print(f"A área do círculo de raio {raio1} unidades é {area1} unidades.")

if area1 < 0 :
    print("valores negativos não são permitidos")


