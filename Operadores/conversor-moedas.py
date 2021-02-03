#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar.

print("\nCARTEIRA EM DOLARES")

dolar = 3.27

real = float(input("\nQuantidade (reais) na CARTEIRA: "))

print("\nVocê tem {:.2f} dolares na carteira.".format(real / dolar))