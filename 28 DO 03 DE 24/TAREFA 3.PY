#Elabore um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M – Masculino ou Sexo Inválido.

print("M - masculino")
print("F - feminino")
genero = input("Qual é o seu gênero? = ")

match  genero:
    case "M":
        print("OK eu gênero é masculino")

    case "F":
        print("OK seu gênero é feminino")

    case _:
        print("não esta de acordo com as opções")