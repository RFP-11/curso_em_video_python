"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.
"""

c = mais18 = homens = mulheresmenos20 = 0
while True:
    print('--' * 16)
    print(f'{f"CADASTRE UMA PESSOA":^30}')
    print('--' * 16)
    idade = int(input(f'Idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    print('--' * 16)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('Cadrastro finalizado!')
print(f'Cadastrados {mais18} pessoas maiores de 18 anos.')
print(f'Cadastrados {homens} homens.')
print(f'Cadastrados {mulheresmenos20} mulheres com menos de 20 anos.')
