"""
Crie um programa que tenha a função "leiaInt()", que vai funcionar de forma semelhante à função "input()" do Python,
contudo fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('ERRO! Digite um número inteiro válido')
    return num


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
