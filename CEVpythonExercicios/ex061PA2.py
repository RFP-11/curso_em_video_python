"""
Refaçe o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
    — usando agora a estrutura while.
"""

a1 = int(input('Informe o pirmeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))

# Uma forma de fazer é:
print('Os 10 primeiros termos da PA são: ')
n = 1
while n < 11:
    an = a1 + (n - 1) * r
    print(an, end=' ')
    n += 1

# Outra forma de fazer:
print('\nOs 10 primeiros termos da PA são: ')
termo = a1
cont = 1
while cont <= 10:
    print(f'{termo}, ', end='')
    termo += r
    cont += 1
print('Fim!')
