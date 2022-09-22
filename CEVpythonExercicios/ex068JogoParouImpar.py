"""
Faça um programa para jogar par ou ímpar com o computador.
    — O jogo só será interrompido quando o jogador perder;
    — mostre o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('=-=' * 15)
print(f'{"Jogo de Par ou Ímpar!":^40}')
print('=-=' * 15)
c = 0
while True:
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    jogador = int(input('Digite um número entre 0 e 5: '))
    computador = randint(0, 5)
    total = jogador + computador
    resultado = ''
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('---' * 15)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total: {total}, DEU {resultado}!')
    print('---' * 15)
    if escolha == 'P' and resultado == 'PAR':
        print('Você GANHOU! \nVamos jogar novamente ...')
        c += 1
    elif escolha == 'I' and resultado == 'ÍMPAR':
        print('Você GANHOU! \nVamos jogar novamente ...')
        c += 1
    else:
        break
print('Você PERDEU!')
print('=-=' * 15)
print(f'GAME OVER! Você venceu {c} partidas.')
