#Faça um programa que leia a largura e a altura de uma parede em metros, calcula sua área e a quantidade de tinta necessária para pinta-lo. Sabendo que cada litro de tinta pinta uma area de 2 metros quadrados.

print("\nPAREDE")

h = float(input("\nAltura: "))
l = float(input("\nLargura: "))

area = (h * l)

tinta = area / 2

print("\nÁrea da PAREDE: {} m² \nTinta: {} litros".format(area, tinta))