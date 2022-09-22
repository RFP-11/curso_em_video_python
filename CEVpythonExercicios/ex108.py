"""
Adapte o código do "desafio #107", criando uma função adicional chamada "fmoeda()" que consiga mostrar os números
como um valor monetário formatado. Ex.: R$:500,00
"""

from Exercicios_107_a_112 import moeda

num = float(input('Digite um valor R$:'))
print(f'A metade de {moeda.fmoeda(num)} é {moeda.fmoeda(moeda.metade(num))}')
print(f'O dobro de {moeda.fmoeda(num)} é {moeda.fmoeda(moeda.dobro(num))}')
print(f'Aumentando 10% de {moeda.fmoeda(num)} temos {moeda.fmoeda(moeda.aumentar(num, 10))}')
print(f'Diminuindo 10% de {moeda.fmoeda(num)} temos {moeda.fmoeda(moeda.diminuir(num, 10))}')
