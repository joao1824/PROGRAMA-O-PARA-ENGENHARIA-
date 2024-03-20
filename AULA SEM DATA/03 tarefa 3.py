import math

raio = float(input("Raio do circulo - "))

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print("AREA = ", f"{round(area, 2)}")
print("PERIMETRO = ", f"{round(perimetro, 2)}")