"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal
    – 3x ou mais no cartão: 20% de juros
"""

print('-=-' * 20)
print(f'{"Gerenciador de Pagamentos!":^50}')
print('-=-' * 20)

valor = float(input('Informe o valor do produto em R$: '))
print('''\nCondições de pagamento:
1 = à vista dinheiro/cheque: 10% de desconto;
2 = à vista no cartão: 5% de desconto;
3 = em até 2X no cartão: sem desconto;
4 = 3X ou mais no cartão: 20% de juros.''')
pag = int(input('Escolha uma das formas de pagamento acima: '))
if pag == 1:
    total = valor - (valor * 10 / 100)
    print(f'Total a pagar é de R$:{total:.2f} \nvocê obteve R$:{valor * 10 / 100:.2f} de desconto!')
elif pag == 2:
    total = valor - (valor * 5 / 100)
    print(f'Total a pagar é de R$:{total:.2f} \nVocê obteve R$:{valor * 5 / 100:.2f} de desconto!')
elif pag == 3:
    print(f'Total a pagar é de R$:{valor:.2f} em 2X de R$:{valor / 2:.2f}')
elif pag == 4:
    total = valor + (valor * 20 / 100)
    parcela = int(input('Em quantas vezes? '))
    print(f'Total a pagar é de R$:{total:.2f} em {parcela}X de R$:{total / parcela:.2f}'
          f'\nJuros adicionais de R$:{valor * 20 / 100:.2f}')
else:
    print('Opção INVALIDA! Tente novamente.')
    exit()
