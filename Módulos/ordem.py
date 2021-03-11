#O professor quer sortiar a ordem de apresentação do trabalho dos alunos. Faça um programa que leia a ordem dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print("\nSORTEIO")

n1 = str(input("\nPrimeiro ALUNO: "))
n2 = str(input("\nSegundo ALUNO: "))
n3 = str(input("\nTerceiro ALUNO: "))
n4 = str(input("\nQuarto ALUNO: "))

lista = [n1,n2,n3,n4]

shuffle(lista)

print("\nOrdem de APRESENTAÇÃO: {}".format(lista))