"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tpl = ('Lápis', 1.75, 'Borracha', 2, 'Caerno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
       'compasso', 9.90, 'Mochila', 120.32, 'Canetas', 22.50, 'Livros', 1970)

print('--' * 20)
print(f'{"Lista de Preços":^40}')
print('--' * 20)
for c in range(0, len(tpl)):
    if c % 2 == 0:
        print(f'{tpl[c]:.<30}', end='')
    else:
        print(f'R$:{tpl[c]:>7.2f}')
print('--' * 20)
