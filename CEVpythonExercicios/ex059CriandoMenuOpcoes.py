"""
Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

# Uma forma de fazer o programa é:
# Nessa versão o usuario só pode escolher uma opção por compilação.
# Mais abaixo faremos uma versão que pode testar todas as opções numa única compilação.
a = float(input('Informe o 1° número: '))
b = float(input('Informe o 2° número: '))
repetir = True
while repetir:
    repetir = False
    escolha = int(input('''Você tem as seguintes opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    O que deseja fazer a seguir: '''))
    if escolha == 1:
        print(f'{a} + {b} = {a + b}')
    elif escolha == 2:
        print(f'{a} X {b} = {a * b}')
    elif escolha == 3:
        if a > b:
            print(f'Entre {a} e {b}, o maior é {a}')
        else:
            print(f'Entre {a} e {b}, o maior é {b}')
    elif escolha == 4:
        a = float(input('Informe o 1° número: '))
        b = float(input('Informe o 2° número: '))
        repetir = True
    elif escolha == 5:
            print('Tenha um bom dia!')
            exit()
    else:
        print('Opção inválida!')
        denovo = str(input(('Deseja tentar novamete [S/N]? '))).strip()[0]
        if denovo in 'Ss':
            repetir = True
        else:
            repetir = False
print('Obridago! \nFim da seção!')

# Uma outra forma de fazer o programa é:
# Nessa versão o usuario pode testar todas as opções com uma única compilação.
from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('''Você tem as seguintes opções!
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    escolha = int(input('>>>>> Informe a sua opção: '))
    if escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif escolha == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
    elif escolha == 4:
        print('Informe os números novamente.')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Finalissando...')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente.')
    print('-=' * 15)
print('Fim do programa. Volte sempre!')
