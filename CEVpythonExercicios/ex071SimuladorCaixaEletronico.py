"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=' * 40)
print('{:^40}'.format('Banco Python'))
print('=' * 40)

valor = int(input('Qual valor você quer sacar? R$:'))
total = valor
cedula = 50
c = 0
while True:
    if total >= cedula:
        total -= cedula
        c += 1
    else:
        if c > 0:
            print(f'Total de {c} cédulas de R$:{cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        c = 0
        if total == 0:
            break
print('=' * 30)
print('O Banco Python agradece!')
