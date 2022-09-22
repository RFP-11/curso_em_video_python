"""
Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = maior2L = 0
for L in range(0, 3):
    for c in range(0, 3):
        matriz[L][c] = int(input(f'Digite um valor inteiro para a posição [{L}, {c}] da matriz 3x3: '))
        if matriz[L][c] % 2 == 0:
            somapar += matriz[L][c]
        if c == 2:
            soma3c += matriz[L][c]
        if L == 1:
            if c == 0:
                maior2L = matriz[L][c]
            elif matriz[L][c] > maior2L:
                maior2L = matriz[L][c]
print('-=' * 20)
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[L][c]:^5}]', end='')
    print()
print('-=' * 20)
print(f'A soma de todos os valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior2L}')
