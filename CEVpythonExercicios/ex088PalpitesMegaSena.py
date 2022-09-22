"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

print('==' * 20)
print(f'{"Jogo da MEGA SENA":^40}')
print('==' * 20)
total = []
jogada = []
vezes = int(input('Quantos jogos você deseja que eu sorteie? '))
print('-=' * 20)
print('Processando...')
sleep(2)
for c in range(0, vezes):
    for v in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogada:
                jogada.append(num)
                break
    total.append(jogada[:])
    jogada.clear()
    total[c].sort()
    print(f'Jogo n° {c + 1}: {total[c]}')
    if c != (vezes - 1):
        sleep(1)
print('-=' * 20)
print(f'{"Boa Sorte!":^40}')
print('-=' * 20)
