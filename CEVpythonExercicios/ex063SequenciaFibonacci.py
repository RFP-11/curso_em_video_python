"""
Faça um programa que leia um número N inteiro qualquer e mostre os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

OBS: A sequência de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo
subsequente corresponde à soma dos dois anteriores. F_n = F_(n-1) + F_(n-2)
Ex.: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...
"""


print('-=-' * 15)
print(f'{"Sequância de Fibonacci!":^40}')
print('-=-' * 15)

n = int(input('Quantos termos você quer mostrar? '))

# Uma forma de fazer:
c = 0
lst = [0, 1]
print(f'Os {n} primeiros termos da sequência de Fibonacci são: \n0, 1, ', end='')
while c < n:
    if c > 1:
        f = lst[c - 1] + lst[c - 2]
        lst.append(f)
        print(f, end=', ')
    c += 1
print('...')

# Outra forma de fazer:
t1 = 0
t2 = 1
print(f'Os {n} primeiros termos da sequência de Fibonacci são: \n0, 1, ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(t3, end=', ')
    t1 = t2
    t2 = t3
    cont += 1
print('...')
