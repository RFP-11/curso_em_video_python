"""
Crie um programa que faça o computador jogar Jokenpô com você.
Regras:
    - Pedra ganha da tesoura (amassando-a ou quebrando-a).
    - Tesoura ganha do papel (cortando-o).
    - Papel ganha da pedra (embrulhando-a).
"""

from random import randint
from time import sleep

print('-=-' * 20)
print(f'{"Jogando Pedra Papel Tesoura!":^60}')
print('-=-' * 20)

print('''Suas opções:
0 = Pedra;
1 = Papel;
2 = Tesoura.''')
jogada = int(input('Qual a sua jogada? '))
if jogada != 0 and jogada != 1 and jogada != 2:
    print('Entrada INVALIDA! tente novamente.')
    exit()
comput = randint(0, 2)
lst = ['Pedra', 'Papel', 'Tesoura']

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 12)
print(f'Computador jogou "{lst[comput]}"')
print(f'Jogador jogou "{lst[jogada]}"')
print('-=' * 12)

vencedor = ['JOGADOR VENCE!', 'COMPUTADOR VENCE!', 'EMPATE!']

# Para dar empate:
n = 2
# Para o jogador ganhar:
if jogada == 0 and comput == 2:
    n = 0
elif jogada == 2 and comput == 1:
    n = 0
elif jogada == 1 and comput == 0:
    n = 0
# Para o comprtador ganhar:
elif comput == 0 and jogada == 2:
    n = 1
elif comput == 2 and jogada == 1:
    n = 1
elif comput == 1 and jogada == 0:
    n = 1

print(f'{vencedor[n]}')

"""
Outra forma de definir o vencedor é:
"""
if comput == 0:
    if jogada == 0:
        print('Empate!')
    elif jogada == 1:
        print('JOGADOR VENCE!')
    elif jogada == 2:
        print('COMPUTADPR VENCE!')
elif comput == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('JOGADOR VENCE!')
elif comput == 2:
    if jogada == 0:
        print('JOGADOR VENCE!')
    elif jogada == 1:
        print('COMPUTADOR VENCE!')
    elif jogada == 2:
        print('EMPATE!')
