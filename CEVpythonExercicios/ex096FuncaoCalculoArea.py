"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def area(m, n):
    """
    --> Calcula a área de um retângulo.
    :param m: indica a largura
    :param n: indica o comprimento
    :return: retorna área
    """
    a = m * n
    return a


print('<<< Controle de terrenos >>>')
print('--' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno ({largura} m) X ({comprimento} m) é de {area(largura, comprimento):.1f} m².')
