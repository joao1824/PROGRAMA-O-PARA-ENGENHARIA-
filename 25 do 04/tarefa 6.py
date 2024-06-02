# Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120.
numb = int(input("NUMERO PARA FATORAR => "))
aux = 1
aux2 = numb

for x in range(numb):
   
    fat = aux2 * (numb - aux)
    print (f"{numb}! {aux2} * {numb - aux}")
    aux2 = fat
    aux = 1 + aux
    
    if aux == numb + 1  :
        break    
    print(fat)

