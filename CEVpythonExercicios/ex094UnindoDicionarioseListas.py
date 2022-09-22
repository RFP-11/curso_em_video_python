"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num dicionário e
todos os dicionários numa lista. No final, mostre:
    A) Quantas pessoas foram cadastradas;
    B) A média de idade;
    C) Uma lista com as mulheres;
    D) Uma lista de pessoas com idade acima da média.
"""

lst = list()
dic = dict()
somaidades = 0
while True:
    dic['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        dic['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dic['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dic['Idade'] = int(input('Idade: '))
    somaidades += dic['Idade']
    lst.append(dic.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if opcao != 'S':
        break
media = somaidades / len(lst)
print('==' * 20)
print(f'Foram cadastradas {len(lst)} pessoas;')
print(f'A média de idades foi de {media:.1f} anos;')
print('As mulheres cadastrada foram: ', end='')
for i, c in enumerate(lst):
    if c['Sexo'] == 'F':
        print(f'{c["Nome"]};', end=' ')
print()
print('As pessoas com idade acima da média são: ')
for i, c in enumerate(lst):
    if c['Idade'] >= media:
        for k, v in c.items():
            print(f'  {k} = {v};', end=' ')
        print()
print()
print('<<< ENCERRADO! >>>')
