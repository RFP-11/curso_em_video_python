"""
Reescreva a função "leiaInt()" que fizemos no "desafio 104", incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.
"""


def leiaInt(msg='Digite um valor: '):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg='Digite um valor: '):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31m\nEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o real {m}')
