# 2) Agora, faça uma função de acordo com a média da função anterior
# informe o status do aluno de acordo com a tabela a seguir:
# • Média acima de 6: “Aprovado”;
# • Média entre 4 e 6 :“Verificação Suplementar”;
# • Média abaixo de 4 : “Reprovado.

def nota_media():
    nota1 = float(input("Primeira nota = "))
    nota2 = float(input("Segunda nota = "))
    nota3 = float(input("Terceira nota = "))
    
    media = (nota1 + nota2 + nota3)/3

    if media >= 6:
        print("Aprovdo")
    if media >= 4 and media < 6:
        print("Verificação Suplementar")       
    if media < 4:
        print("Reprovado")
    return media

print(nota_media())