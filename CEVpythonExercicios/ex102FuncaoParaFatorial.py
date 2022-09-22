"""
Crie um programa que tenha uma função "fatorial()" que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
"""


def fatorial(f=0, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param f: número a ser calculado.
    :param show: [opcional] visualizar ou não o processo do cálculo do fatorial.
    :return: retorna o cálculo do fatorial de f.
    """
    from time import sleep
    resultado = 1
    for n in range(f, 0, -1):
        resultado *= n
        if show:
            print(f'{n}', 'x ' if n != 1 else '= ', end='')
            sleep(0.5)
    return resultado


print(fatorial(5, True))
print(fatorial(7))
print(fatorial(9, False))

help(fatorial)
