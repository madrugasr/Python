#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

print("\nMÉDIA NOTA")

nome = str(input("\nNome do ALUNO: "))
n = float(input("\nNota do 1º Bimestre: "));
n1 = float(input("\nNota do 2º Bimestre: "))

media = (n + n1) / 2

print("\nO {} teve a média de {}.".format(nome,media))

