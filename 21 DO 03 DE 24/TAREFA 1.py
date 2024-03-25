# Construa um programa que tem como dados de entrada dois pontos quaisquer no plano cartesiano: P1 e P2. Considere que P1 é definido 
# pelas coordenadas x1 e y1, enquanto P2 por x2 e y2 . O programa deve calcular e escrever a distância entre os pontos P1 e P2.

import math

x1 = int(input('Valor para calcular a ditancia (x1) = '))
y1 = int(input('Valor para calcular a ditancia (y1) = '))

x2 = int(input('Valor para calcular a ditancia (x2) = '))
y2 = int(input('Valor para calcular a ditancia (y2) = '))

# FORMULA - d=√((x_2-x_1)²+(y_2-y_1)²)

distancia =  math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'a distância entre os pontos {x1} {y1} e {x2} {y2} é {round(distancia,2)}')