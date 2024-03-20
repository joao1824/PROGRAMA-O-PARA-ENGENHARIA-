dinheiro_person = float(input("VALOR QUE IRA USAR = "))

litro_buy = dinheiro_person/4.95
km_road = 20 * litro_buy

print("PODE COMPRAR = ", round(litro_buy, 2),"L")
print("VAI PODER DIRIGIR POR = ",  round(km_road, 2),"KM")