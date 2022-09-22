"""
Crie um programa em python que leia quanto dinheiro uma pessoa tem na carteira.
Depois, mostre quantos dólares ela pode comprar.

OBS: Como o dolar varia muito, considere: US$1,00 = R$3.27.
"""

n = float(input('Digite a quantia de dinheiro disponível: '))
print('\n'
      'A cotação do Dolar está em R$:3,27.\n')
print(f'Com a quantia de R$:{n:.2f}, poderá comprar-se U$:{n/3.27:.2f}.')
