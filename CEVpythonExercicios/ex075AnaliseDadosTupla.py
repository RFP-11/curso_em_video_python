"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
"""

n1 = int(input('Digite o 1° valor inteiro: '))
n2 = int(input('Digite o 2° valor inteiro: '))
n3 = int(input('Digite o 3° valor inteiro: '))
n4 = int(input('Digite o 4° valor inteiro: '))
tpl = (n1, n2, n3, n4)
print(f'Você digitou os valores: {tpl}')
print(f'O úmero 9 apareceu {tpl.count(9)} vezes')
if 3 in tpl:
    print(f'O número 3 foi digitado na {tpl.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares foram: ', end='')
for c in tpl:
    if c % 2 == 0:
        print(f'{c}', end=' ')
