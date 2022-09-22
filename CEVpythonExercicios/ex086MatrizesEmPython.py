"""
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

lst = []
linha = []
for c in range(1, 4):
    for d in range(1, 4):
        linha.append(int(input(f'Digite um número inteiro para [{c}, {d}]: ')))
    lst.append(linha[:])
    linha.clear()
print('-=' * 20)
print(f'''
{lst[0]}
{lst[1]}
{lst[2]}
''')

# Outra forma de fazer:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor inteiro para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
