"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time do Atlético-MG.
"""

colocacao = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional', 'Atlético-MG',
             'América-MG', 'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará', 'Fortaleza', 'Cuiabá',
             'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('=--=' * 20)
print(f'Lista de times do Brasileirão: {colocacao}')
print('=--=' * 20)
print(f'Os 5 primeiros são: {colocacao[:5]}')
print('=--=' * 20)
print(f'Os 4 últimos são: {colocacao[-4:]}')
print('=--=' * 20)
print(f'Times em ordem alfabética: {sorted(colocacao)}')
print('=--=' * 20)
print(f'O Atlético-MG está na {colocacao.index("Atlético-MG") + 1}ª posição.')

print('\n')

# fazendo de outra forma:
print('=--=' * 20)
print('Lista de times do Brasileirão: ')
for c in colocacao:
    print(c, end=', ')
print('\n')
print('=--=' * 20)
print('Os 5 primeiros são: ')
for c in colocacao[:5]:
    print(c, end=', ')
print('\n')
print('=--=' * 20)
print('Os 4 últimos são: ')
for c in colocacao[-4:]:
    print(c, end=', ')
print('\n')
print('=--=' * 20)
print('Times em ordem alfabética: ')
for c in sorted(colocacao):
    print(c, end=', ')
print('\n')
print('=--=' * 20)
print(f'O Atlético-MG está na {colocacao.index("Atlético-MG") + 1}ª posição.')
