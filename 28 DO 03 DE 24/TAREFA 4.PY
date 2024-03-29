#Escreva um programa que verifique se uma letra digitada é vogal ou consoante Ou ainda se não está nestes grupos.

letra = input("Digite uma letra ")

vogal = ["a" , " e", " i", " o", " u"
         ,"A","E","I","O","U"]
consoante = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
             ,"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
if letra in vogal:
    print("É vogal")
elif letra in consoante:
    print("É consoante")
else :
    print("Não foi possivel indentificar")