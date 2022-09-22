"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” num número entre 0 e 10.
    — Contudo, agora o jogador vai tentar adivinhar até acertar;
    — Mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep

print('-=' * 20)
print(f'{"Jogo de Adivinhação!":^40}')
print('-=' * 20)

# Uma forma de resolver o exercício é:
print('Estou pensando em um número inteiro entre 0 e 10 ', end='')
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

num = randint(0, 10)
adivinha = int(input('Em que número eu pensei? '))
c = 1
while adivinha != num:
    adivinha = int(input('Errou! Tente adivinhar novamente: '))
    c += 1
print(f'Parabéns você VENCEU! na {c}ª tentativa.')

# Outra forma de resolver o exercício seria:
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou na {palpite}ª tentativa. Parabéns!')
