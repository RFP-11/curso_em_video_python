"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

lst = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° número inteiro positivo: '))
    if num % 2 == 0:
        lst[0].append(num)
    elif num % 2 == 1:
        lst[1].append(num)
print('-=' * 20)
lst[0].sort()
print(f'Pares: {lst[0]}')
lst[1].sort()
print(f'Ímpares: {lst[1]}')
