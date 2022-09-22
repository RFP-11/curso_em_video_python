"""
Faça um programa que calcule a soma entre todos os números ímpares múltiplos de três no intervalo de 1 até 500.
"""

print('-=' * 30)
print(f'{"Somando ímpares multiplos de três entre 1 e 500!":^60}')
print('-=' * 30)

n = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        n += 1
print(f'A soma dos {n} númeors solicitados é {s}')
print('Fim')
