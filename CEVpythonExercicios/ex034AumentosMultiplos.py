"""
Escreva um programa que:

    - pergunte o salário de um funcionário;
    - calcule o valor do seu aumento.

    - Para salários superiores a R$: 1.250,00, calcule um aumento de 10%;
    - Para os inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('Informe seu salário: '))

if s <= 1250:
    aumento = s * 15 / 100
else:
    aumento = s * 10 / 100

print(f'Você terá um aumento salarial de R$:{aumento:.2f} e passará a receber R$:{s + aumento:.2f}')
