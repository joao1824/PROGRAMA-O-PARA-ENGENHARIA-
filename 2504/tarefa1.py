# 1) Desenvolva um script Python que lê vários números positivos via teclado. Quando o
# número lido for -1, o script deve parar e exibir a soma de todos os números positivos
# inseridos, a média desses números, o menor e o maior número digitado.

x = 0 #Variavel para poder ficar em loop
soma = 0 #Armazenar a soma dos numero inseridos
maior = 0 #Usado para salvar o numero maior
menor_aux1 = 0 #Usado para salvar o numero 
menor_aux3 = 0 #Usado para salvar o primeiro numero inserido
menor = 0 #Usado para slavar numero menor
while x == 0:
    numero = int(input("Numero => ")) #numero de entrada
    menor_aux1 = numero
    if numero != -1:
        soma = numero + soma    
        if numero > maior:
            maior = numero
        elif menor_aux3 == 0:
            menor = numero
            menor_aux3 = menor_aux3 + 1
        elif menor >= numero:
            menor = numero
    elif numero == -1:
        print("ACABOU -1 INDENTIFICADO")
        x = x + 1

    
media =  soma/2 
if numero == -1:
    x += 1    
    print(f"A soma dos numero inseridos é {soma}")
    print(f"A media dos nuemro inseriodos é {media}")
    print(f"O numero maior é {maior}")
    print(f"O numero menor é {menor}")