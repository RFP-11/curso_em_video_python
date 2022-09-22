"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

n = float(input('Digite a distância da viagem em Km: '))
print(f'Você está prestes a começar uma viagem de {n} Km.')
if n <= 200:
    valor = n * 0.5
else:
    valor = n * 0.45
print(f'O valor a pagar será de R$:{valor:.2f}')
