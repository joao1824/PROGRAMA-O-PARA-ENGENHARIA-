# 10 – Elabore um script em linguagem Python, utilizando Dicionários, que
# contenha 4 funcionários, com o índice numérico, seu nome, sua função e
# tempo de serviço em anos. Em seguida, solicite do usuário demitir um dos
# funcionários conforme o número de cadastro e mostre na tela os
# funcionários restantes. O Script não deve permitir que um funcionário com a
# função “Programador” e com 3 anos ou mais seja demitido.

lista_de_funcionario = {0 : ["João","Programador",4], 1 : ["Ana","Caixa",4], 2 : ["Lucas","Gerente",2]}

while True:
    print(lista_de_funcionario)
    demitir = int(input("Qual funcionario deseja demitir ? (Escolaha um índice numérico) ==> "))
    if lista_de_funcionario[demitir][1] == "Programador" and lista_de_funcionario[demitir][2] >= 3:
        print("Funcionario não pode ser demitido devido aos seus requisitos")
        
    else:
        lista_de_funcionario.pop(demitir)    

print(lista_de_funcionario)