#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

print("\nDESCONTO")

p = float(input("\nPreço do PRODUTO: "))

desconto = (p / 100) * 5


print("\nDesconto de 5%:",p - desconto)