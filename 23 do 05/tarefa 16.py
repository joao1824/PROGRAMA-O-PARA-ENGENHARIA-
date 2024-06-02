# 16 - Elabore um script que crie um dicionário na qual cada chave seja um
# caractere e seu valor seja o número de vezes que o caractere aparece na frase.
# Exemplo:
# "Digite uma frase para contar as letras:“ – eu sei
# Resposta {'e': 2, 'u': 1,
# ' ': 1, 's': 1, 'i': 1}

frase = str(input("Digite uma frase para contar as letras: "))

lista = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ç","z","x","c","v","b","n","m"]
dic = {}
for letra in lista:
    quantidade = frase.count(letra)
    if frase.count(letra) != 0:
        dic.update({letra:quantidade})

print(dic)