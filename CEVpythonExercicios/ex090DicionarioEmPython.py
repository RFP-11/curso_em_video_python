"""
Faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

dic = {'nome': str(input('Nome: ')).strip().title()}
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
if dic['média'] >= 7:
    dic['situação'] = 'Aprovado'
elif 5 <= dic['média'] < 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
print('--' * 20)
for k, v in dic.items():
    print(f' - {k} é igual a {v}')
