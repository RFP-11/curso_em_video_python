"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA — Progressão Aritimética.
No final, mostre os 10 primeiros termos dessa progressão.

OBS: uma progressão aritmética (P.A.) é uma sequência numérica em que cada termo, a partir do segundo, é igual à soma
do termo anterior com uma constante "r". O número "r" é chamado razão ou diferença comum da progressão aritmética.
    a_n = a_(n-1) + r, n > 1
    r = a_n - a_(n-1), n > 1
A formula geral para o n-ésimo termo é: a_n = a_1 + (n - 1).r
Ex.:
(1, 4, 7, 10, 13, ...) P.A. com a_1 = 1 e r = 3.
"""

a1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
print('Os 10 primeiros termos da PA são:')
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end=', ')
print('Fim!')
