# Crie um script python que leia o dia, o mês e o ano do nascimento de uma pessoa
# e mostre uma mensagem com a data formatada.

dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês do seu nascimento? ')
ano = input('Qual o ano do seu nascimento? ')

print('\n')  # Pula uma linha.

print('Então você nasceu em: ', dia, 'de', mes, 'de', ano, '.', 'Que legal.')

print('\n')  # Pula uma linha.

print(f'Então você nasceu em: {dia}/{mes}/{ano}. Que legal!')

# observe as diferentes formas de apresentar o resultado.
