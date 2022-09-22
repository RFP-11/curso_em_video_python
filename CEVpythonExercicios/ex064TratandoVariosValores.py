"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag - 999).
"""

# Uma forma de fazer:
soma = n = c = 0
while n != 999:
    n = int(input('Digite um numero inteiro [999 para parar]: '))
    if n != 999:
        soma += n
        c += 1
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')

# Outra forma de fazer:
soma = n = c = 0
while n != 999:
    n = int(input('Digite um numero inteiro [999 para parar]: '))
    soma += n
    c += 1
print(f'Você digitou {c - 1} números e a soma entre eles foi {soma - 999}.')

# Ainda outra forma de fazer:
soma = c = 0
n = int(input('Digite um numero inteiro [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um numero inteiro [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')
