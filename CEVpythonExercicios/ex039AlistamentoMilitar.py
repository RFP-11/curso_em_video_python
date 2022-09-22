"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
    - se ele ainda vai se alistar ao serviço militar,
    - se é a hora exata de se alistar
    - se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

print('-=-' * 20)
print(f'{"Situação do Alistamento Militar":^60}')
print('-=-' * 20)

print('''Opções de Gênero:
M = masculino;
F = Feminino.''')
sexo = str(input('Indique seu Gênero: ')).strip().upper()

if sexo == 'F':
    print('Você tem ISENÇÃO do alistamento militar obrigatório!')
    escolha = str(input('Você gostaria de se voluntariar? (Opções: S = Sim; N = Não) ')).strip().upper()
    if escolha == 'N':
        print('Tenha um bom dia!')
        exit()
    else:
        print('Acesse o site oficial da força pretendida para maiores informações.')
else:
    ano = int(input('Ano de nascimento: '))
    hoje = date.today().year
    idade = hoje - ano

    print(f'Você nasceu em {ano}, tem {idade} em {hoje}.')

    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para o alistamento.\n'
              f'Seu alistamento será em {hoje + (18 - idade)}.')
    elif idade == 18:
        print('Este é o momento exato de se alistar!')
    else:
        print(f'Você já deveria ter se alistado a {idade - 18} anos.\n'
              f'Seu alistamento foi em {hoje - (idade - 18)}.')
