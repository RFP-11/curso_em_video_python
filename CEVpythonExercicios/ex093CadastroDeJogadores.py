"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado num dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados = dict()
gols = list()
dados['Nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantidade de gols marcados no {c + 1}° Jogo: ')))
dados['Gols'] = gols[:]
dados['Total de gols'] = sum(gols)
print('==' * 20)
print(dados)
print('==' * 20)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('==' * 20)
print(f'O Jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, c in enumerate(dados['Gols']):
    print(f' => Na {i + 1}° partida, fez {c} gols.')
print(f'Foi um total de {dados["Total de gols"]} gols.')
