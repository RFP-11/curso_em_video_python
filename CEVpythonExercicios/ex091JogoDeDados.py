"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados num
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

dic = {}
for c in range(1, 5):
    dic[f'Jogador {c}'] = randint(1, 6)
print(f'{"<<< Valores Sorteados >>>":^40}')
for k, v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
lst = (sorted(dic.items(), key=itemgetter(1), reverse=True))
print('==' * 20)
print(f'{"<<< Ranking dos Jogadores >>>":^40}')
for i, c in enumerate(lst):
    print(f'{i + 1}° lugar: {c[0]} com {c[1]}')
    sleep(1)
