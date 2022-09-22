def aumentar(valor=0, taxa=0, formatado=False):
    x = valor + (valor * taxa / 100)
    return x if formatado is False else fmoeda(x)


def diminuir(valor=0, taxa=0, formatado=False):
    x = valor - (valor * taxa / 100)
    return x if formatado is False else fmoeda(x)


def dobro(valor=0, formatado=False):
    x = valor * 2
    return x if formatado is False else fmoeda(x)


def metade(valor=0, formatado=False):
    x = valor / 2
    return x if formatado is False else fmoeda(x)


def fmoeda(valor=0.0, Reais='R$:'):
    return f'{Reais}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=0, queda=0):
    print('--' * 15)
    print('Resumo do valor'.center(30))  # Mesmo efeito que: "print(f'("Resumo do valor":^30)')"
    print('--' * 15)
    print(f'Valor analizado: \t{fmoeda(valor)}')  # O "\t" é utilizado para criar uma tabulação dos dados.
    print(f'Dobro do valor: \t{dobro(valor, True)}')
    print(f'Metade do valor: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{queda}% de redução: \t{diminuir(valor, queda, True)}')
    print('--' * 15)
