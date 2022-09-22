# Faça um algoritimo em python que leia o preço de uma produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Digite a volor do produto: '))
d = n*5/100
print(f'\n'
      f'Este produto de R$:{n:.2f} custará R$:{n-d:.2f} com 5% de desconto.\n')
print(f'Você terá uma economia de R$:{d:.2f}')
