"""
Crie um programa que mostre na tela todos os números pares e ímpares separadamente no intervalo entre 1 e 50.
"""

# Apenas os pares:
print('Os números pares entre 1 e 50 são:')
for n in range(2, 51, 2):
    print(n, end=' ')
print('Fim! \n')

# Apenas os ìmpares:
print('Os números ímpares entre 1 e 50 são:')
for m in range(1, 51, 2):
    print(m, end=' ')
print('Fim! \n')

# Fazendo o processo em simultâneo:
pares = []
impares = []
for c in range(1, 51):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Os números pares entre 1 e 50 são:\n{pares}')
print(f'\nOs números ímpares entre 1 e 50 são:\n{impares}')
