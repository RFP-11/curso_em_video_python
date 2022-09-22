"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas "sorteia()" e "somaPar()".
    - A primeira função vai sortear 5 números e vai colocá-los dentro da lista;
    - A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint


def sorteia(v):
    lst = []
    for c in range(0, v):
        lst.append(randint(0, 1000))
    return lst[:]


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    return soma


numeros = sorteia(int(input('Quantidade de numeros aleatórios para sortear: ')))
print(f'Os números sorteados foram {numeros}')
print(f'A soma dos números pares é {somapar(numeros)}')

print()
print('==' * 20)
print()

# Outra forma de fazer o sorteio de 5 números na lista:


def Sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


Numeros = list()
Sorteia(Numeros)
print(Numeros)

print()
print('==' * 20)
print()

# Ainda outra forma elegante de construir o problama:


def sorteando(f1, f2):
    lst = []
    for c in range(0, f1):
        lst.append(randint(0, f2))
    return lst[:]


numbers = sorteando(int(input('Quantidade de numeros aleatórios para sortear: ')),
                  int(input('Sortear números no intervalo [0, n]. Informe "n": ')))
print(f'Os números sorteados foram {numbers}')
print(f'Outros números sorteados foram {sorteando(5, 100)}')
print(f'Ainda outros números sorteados foram {sorteando(10, 1000)}')
print(f'Para finalizar os testes. Números sorteados foram {sorteando(5, 10)}')
print()
