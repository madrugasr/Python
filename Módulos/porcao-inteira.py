#Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

#Autor: Daniel Marques

from math import trunc

print("\nARRENDODAMENTO SUPERIOR")

a = float(input("\nNúmero: "))

print("\nPORÇÃO INTEIRA: {}".format(trunc(a)))
