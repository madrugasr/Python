#Escreva um programa que pergunte a quantidade de kilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 600 reais por dia e 0.15 reais por kilmetros rodados.^

print("\nALUGUEL DE CARROS")

d = float(input("\nDias: "))

km = float(input("\nKm: "))

dia = 60 * d
kilometro = km * 0.15

print("\nValor à pagar:",kilometro + dia)