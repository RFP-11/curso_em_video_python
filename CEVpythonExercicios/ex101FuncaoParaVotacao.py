"""
Crie um programa que tenha uma função chamada "voto()" que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(nascimento):
    from datetime import date   # Declarar o módulo na função economiza espaço da memória. Mas vira "varaável local".
    idade = (date.today().year - nascimento)
    if 16 <= idade < 18 or idade >= 70:
        situacao = 'VOTO OPCIONAL!'
    elif 18 <= idade < 70:
        situacao = 'VOTO OBRIGATÓRIO!'
    else:
        situacao = 'NÃO VOTA!'
    return print(f'Com {idade} anos: {situacao}')


voto(int(input('Informe o ano de nascimento: ')))
