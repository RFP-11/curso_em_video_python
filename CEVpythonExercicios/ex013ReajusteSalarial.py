# Faça um algoritimo em python que leia o salário  de um funcionário e mostra seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do salário recebido: '))
a = s*15/100
print(f'O salário de R$:{s:.2f} será de R$:{s+a:.2f} com 15% de aumento.\n')
print(f'Você terá R$:{a:.2f} de abono salarial.')
