# João Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do Estado (50 quilos) deve pagar uma multa de
# R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
# os dados do programa com as mensagens adequadas.

kilos_peixe = float(input("Quantos kilos você trouxe ? "))

if kilos_peixe > 50:
    kilos_exe = kilos_peixe - 50
    multa = kilos_exe * 4
    print(f"Você exedeu o limite de 50 kilos em {kilos_exe} a multa a ser paga é {multa}")
else:
    print("Tudo certo esta dentro do limite")