#Um professor que sortiar um dos seus alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e o escrevendo o nome escolhido.

from random import choice

print("\nSORTEIO")

n1 = str(input("\nPrimeiro ALUNO: "))
n2 = str(input("\nSegundo  ALUNO: "))
n3 = str(input("\nTerceiro ALUNO: "))
n4 = str(input("\nQuarto ALUNO: "))

lista = [n1,n2,n3,n4]
#função RANDOM escolhe um dos varios elementos compostos da lista.
escolhido = choice(lista)

print("\n{}".format(escolhido))