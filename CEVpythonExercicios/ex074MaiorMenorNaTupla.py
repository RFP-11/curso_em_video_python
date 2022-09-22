"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

tpl = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os valores sorteados foram: {tpl}')
maior = menor = 0
for c in range(0, 5):
    if c == 0:
        maior = tpl[c]
        menor = tpl[c]
    elif tpl[c] > maior:
        maior = tpl[c]
    elif tpl[c] < menor:
        menor = tpl[c]
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

print('\n')

# Outra forma de fazer:
print('Os valores sorteados foram: ', end='')
for c in tpl:
    print(f'{c}', end=' ')
print(f'\nO maior número é: {max(tpl)}')
print(f'O menor número é: {min(tpl)}')
