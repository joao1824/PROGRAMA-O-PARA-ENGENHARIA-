# Ainda sobre o programa anterior, incremente-o, informando a quantidade de
# valores positivos, a quantidade de valores negativos e o percentual de valores
# negativos e positivos.


quantidade = 0
soma = 0
neg = 0
pos = 0
for numero in range(4):
    numb = float(input("Digite um nuemro ==> "))
    quantidade += 1
    soma = soma + numb
    if  numb < 0 :
        neg += 1
    if numb > 0:
        pos += 1

media_neg = (100 * neg)/quantidade
media_pos = (100 * pos)/quantidade
mediaari = soma/quantidade
print(f"média aritmética dos valores lidos é {mediaari}")
print(f"A quantidade de negativos é {neg} e a media deles é {media_neg}")
print(f"A quantidade de positivos é {pos} e a media deles é {media_pos}")

