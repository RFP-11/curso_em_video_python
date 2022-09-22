"""
Modifique as funções criadas no "desafio 107" para elas aceitarem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado pela função "fmoeda()", desenvolvida no "desafio 108".
"""

from Exercicios_107_a_112 import moeda

num = float(input('Digite um valor R$:'))
print(f'A metade de {moeda.fmoeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.fmoeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10% de {moeda.fmoeda(num)} temos {moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 15% de {moeda.fmoeda(num)} temos {moeda.diminuir(num, 15, True)}')
