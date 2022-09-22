"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.
"""

print('==' * 20)
print(f'{"Loja do Python!":^40}')
print('==' * 20)

tot = mais1000 = maisbarato = c = 0
nomemaisbarato = ''
while True:
    nome = str(input('Nome do Produto: ')).strip()
    valor = float(input('Valor R$:'))
    tot += valor
    c += 1
    if valor > 1000:
        mais1000 += 1
    if c == 1 or valor < maisbarato:  # O comando "or" = ou; se uma das condições forem verdadeiras o laço é executado.
        maisbarato = valor
        nomemaisbarato = nome
    print('--' * 20)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'\n{"Compra Finalizada!":-^40}\n')
print(f'Total de itens comprados: {c}. \nValor total da compra R$:{tot:.2f}')
print(f'Quantidade de produtos acima de mil reais: {mais1000}')
print(f'O produta mais barato foi {nomemaisbarato} que custa R$:{maisbarato:.2f}')
