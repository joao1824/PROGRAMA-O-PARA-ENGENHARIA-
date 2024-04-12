import math


x1,y1 =  float(input("Valor de x (1) ")),float(input("Valor de y (1) "))
x2,y2 =  float(input("Valor de x (2) ")),float(input("Valor de y (2) "))

dis = round(math.sqrt(((x2 - x1)**2)+ ((y2 - y1)**2)),2)

print((f"A distancia entre os dois pontos é {dis}"))