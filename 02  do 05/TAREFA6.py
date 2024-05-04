# Execute um script que imprima na tela apenas os números ímpares entre 1 e
# 50.
numb = 1
for x in range(1,50):
    par = numb%2
    
    if par == 0:
        print(numb)
    numb += 1