"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lst = []
maior = menor = Pmaior = Pmenor = 0
for c in range(0, 5):
    lst.append(int(input(f'Digite um valor inteiro para a posição {c}: ')))
    if c == 0:
        maior = menor = lst[c]
    else:
        if lst[c] > maior:
            maior = lst[c]
        if lst[c] < menor:
            menor = lst[c]
print('=--=' * 12)
print(f'Você digitou os valores {lst}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lst):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lst):
    if v == menor:
        print(f'{i}...', end='')
print()
