"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

n = int(input(('Informe um número para calcular seu fatorial: ')))

# Usando o comando "for":
fat = 1
for c in range(n, 0, -1):
    fat *= c
print(f'{n}! = {fat}')

# Usando o comando "while":
cont = 1
fat = 1
while cont < (n + 1):
    fat *= cont
    cont += 1
print(f'{n}! = {fat}')

# Outra forma usando "while":
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', 'x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)

# Usando função:
from math import factorial
print(f'{n}! = {factorial(n)}')
