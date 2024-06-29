# 3) Escreva uma função para imprimir o nome e salário de um funcionário usando
# as seguintes condições.
# Deve aceitar o nome e o salário do funcionário.
# Se o salário estiver faltando na chamada de função, atribua o valor padrão 9000 ao
# salário.

def salario_função():
    funcionario = input("Nome =")
    salario = float(input("Salario = "))

    if salario == 0:
        salario = 9000
    
    return funcionario, salario

print(salario_função())        