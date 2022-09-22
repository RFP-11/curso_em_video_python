"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
Pergunte ainda se o usuário deseja continuar, se não encerre o programa.
"""

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Entrada inválida! ', end='')
    print(f'Você digitou o número {extenso[num]}')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao != 'S':
        break
print('Programa finalizado!')
