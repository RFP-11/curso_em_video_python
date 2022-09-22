"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

Km = float(input('Digite a kilometragem rodada: '))
dias = int(input('Digite a quantidade de dias alugados: '))

print(f'\n'
      f'Total a pagar: R$:{(dias*60)+(Km*0.15):.2f}')
