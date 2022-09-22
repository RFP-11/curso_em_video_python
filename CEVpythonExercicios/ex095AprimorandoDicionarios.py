"""
Aprimore o desafio 93 para que ele funcione com vários jogadores.
Inclua um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

time = list()
jogador = dict()
gols = list()
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantidade de gols marcados no {c + 1}° Jogo: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        escolha = str(input('Deseja Cintinuar? [S/N]: ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if escolha != 'S':
        break
print('==' * 22)
print('N°   ', end='')
for c in jogador.keys():
    print(f'{c:<15}', end='')
print()
print('--' * 22)
for k, v in enumerate(time):
    print(f'{k:<3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('--' * 22)
    opc = int(input('Mostrar dados de qual Jogador? (999 interrompe). N°: '))
    if opc == 999:
        print('--' * 22)
        print('FINALIZANDO!')
        break
    if opc <= len(time) - 1:
        print(f'Levantamento do jogador {time[opc]["Nome"]}:')
        for i, c in enumerate(time[opc]["Gols"]):
            print(f' => Na {i + 1}° partida, fez {c} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {opc}')
print('==' * 22)
print('<<< VOLTE SEMPRE! >>>')
