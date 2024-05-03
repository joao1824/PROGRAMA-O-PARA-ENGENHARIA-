# Desenvolva um programa que o usuário necessita digitar a senha de um cofre,
# esta senha é numérica (987654), enquanto os valores digitais não forem corretos,
# o programa deverá pedir novamente informando que o valor está incorreto, assim
# que estiver correto, informar, cofre aberto.

x = -1

while x == -1:
    senha = str(input("Digite a senha ==> "))    
    if senha == "987654":
        print("COFRE ABERTO")
        x += 1
    elif senha != "987654":
        print("ERRADO")
        x = -1
        
    