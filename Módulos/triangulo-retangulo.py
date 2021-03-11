#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trinângulon retângulo, calcule e mostre o comprimento da hipotenusa.

#H = (raiz de A² + B²)


from math import hypot

print("\nTRIÂNGULO RETÂNGULO")

co = float(input("\nCATETO OPOSTO: "))
ca = float(input("\nCATETO ADJACENTE: "))

#h = (co**2 + ca**2) ** 0.5
h = hypot(co, ca)

print("\nHIPOTENUSA: {:.2f}".format(h))






