"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

OBS: um número é chamado primo quando possui exatamente dois divisores, 1 e ele mesmo. Ou seja:
Se um número natural n > 1 não é divisível por nenhum primo p tal que p^{2} ≤ n, então ele é primo.
"""

print('==' * 22)
print(f'{"Analisando se é primo!":^40}')
print('==' * 22)

n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'("{c}")', end=', ')
        t += 1
    else:
        print(c, end=', ')
print('Fim!')
print(f'O número {n} foi divisível {t} vezes.')
if t == 2:
    print('Logo, ele É PRIMO!')
else:
    print('Logo ele NÂO É PRIMO!')
