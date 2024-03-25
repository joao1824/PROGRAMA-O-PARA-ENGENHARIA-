#Elabore um código fonte que calcule a hipotenusa de um triângulo retângulo, cujos catetos serão fornecidos pelo usuário.

ctop = float(input("Informe o cateto oposto = "))
ctad = float(input("informe o cateto adjacente = "))

hipotenusa = ctop/ctad

print(f"A hipotenua é {round(hipotenusa,2)}")