# 12 – Em um script Python com duas listas de seis elementos com números
# inteiros informados pelo usuário, crie uma nova lista onde cada elemento é a
# soma dos elementos de mesma posição nas duas primeiras listas.
# Exemplo: Lista1 = [1, 4, 6, ...] Lista2 = [2, 4, 3, ...] Lista_resultante = [3, 8, 9, ...]

Lista1 = [1, 4, 6]
Lista2 = [2, 4, 3]
Lista3 = []
for x in range(len(Lista1)):
    soma = Lista1[x] + Lista2[x]
    Lista3.append(soma)

print(Lista3)