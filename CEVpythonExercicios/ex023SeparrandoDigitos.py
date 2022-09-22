"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex.:    O número 1876 possui:
        Unidades: 6
        Dezenas: 7
        Centenas: 8
        Milhares: 1
"""

n = int(input('\nDigite um número inteiro entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Analisando o número {n}, obseramos que ele possui: ')
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhares: {m}')
