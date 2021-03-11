#Faça um programa que leia uma âlgulo qualquer e mostre o valor do seno, cosseno e tangente.

from math import radians, sin, cos, tan

print("\nSENO, COSSENO, TANGENTE")

an = float(input("\nÂNGULO: "))

seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print("\nSeno: {:.4f}".format(seno))
print("\nCosseno: {:.4f}".format(cosseno))
print("\nTângente: {:.4f}".format(tangente))

