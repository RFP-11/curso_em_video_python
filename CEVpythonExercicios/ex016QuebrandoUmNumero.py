"""
Crie um programa em python que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

Ex:     Digite um número: 6.127
        O número 6.127 tem a parte Inteira 6.
"""

import math

n = float(input('Digite um número real: '))
print(f'O número {n} tem a parte inteira {math.floor(n)}\n')
# O comando "math.floor()" aredonda o valor para baixo. O que fará retornar sempre a parte inteira do número.

print(f'O número {n} tem a parte inteira {math.trunc(n)}\n')

print(f'O número {n} tem a parte inteira {int(n)}')

# Observe as diferentes maneiras de chegar ao mesmo resultado.
