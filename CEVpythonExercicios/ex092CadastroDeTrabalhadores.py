"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) num dicionário.
Se por acaso a CTPS diferir de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

atual = date.today().year
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = (atual - nasc)
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário R$:'))
    cadastro['Aposentadoria'] = (cadastro['Idade'] + ((cadastro['Ano de contratação'] + 35) - atual))
print('==' * 20)
for k, v in cadastro.items():
    print(f'  - {k} = {v}')
