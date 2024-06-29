# 1) Fazer uma função que receba três notas de um aluno e que retorne
# a média dessas 3 notas.

def nota_media():
    nota1 = float(input("Primeira nota = "))
    nota2 = float(input("Segunda nota = "))
    nota3 = float(input("Terceira nota = "))
    
    media = (nota1 + nota2 + nota3)/3

    return media

print(nota_media()," Media")