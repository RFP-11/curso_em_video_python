"""
Faça um programa que tenha uma função chamada "maior()", que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def Maior(*num):
    cont = maior = 0
    print('==' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1
    print(f'Foram informados {cont} números ao todo.')
    print(f'O maior valor informado foi {maior}')


Maior(1, 3, 56, 93, 0, 12, 38, -1)
Maior(2, 4, 52, 28)
Maior(3, 1)
Maior()


# Outra forma de fazer:

def maior(lista):
    lst = lista[:]
    maior = 0
    for c in lst:
        if c == 0 or c > maior:
            maior = c
    return maior


print()
print('==' * 20)
nums = []
while True:
    nums.append(int(input('Digite um número inteiro: ')))
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp != 'S':
        break
print('==' * 20)
print(f'Foram digitados os seguites números: {nums}')
print(f'O maior número digitado foi {maior(nums)}')
