"""
Escreva um programa que:
    - Faça o computador "pensar" em um número inteiro entre 0 e 5.
    - Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    - Escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

print('\nVou pensar em um número entre 0 e 5. Tente adivinhar.\n')
n = randint(0, 5)
d = int(input('Em que número eu pensei? '))

print('Processando...')
sleep(2)

if d == n:
    print('Parabéns! Você conseguiu me vencer.')
else:
    print(f'Ganhei! Eu pensei no número {n}, e não no {d}.')
