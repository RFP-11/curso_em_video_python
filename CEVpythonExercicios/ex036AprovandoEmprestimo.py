"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    - Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    - A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

print('-=-' * 15)
print(f'{"Analisando Emprestimo!":^40}')
print('-=-' * 15)

imovel = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual sua renda mensal? '))
tempo = int(input('Em quanto anos pretende financiar? '))

mensalidade = imovel / (tempo * 12)
condicao = salario * 30 / 100

if mensalidade > condicao:
    print(f'Emprestimo NEGADO! Mensalidade: R$: {mensalidade:.2f}, excede 30% de sua renda mensal.')
else:
    print(f'Emprestimo APROVADO! Mensalidade: R$: {mensalidade:.2f}')
