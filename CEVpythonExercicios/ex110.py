"""
Adicione ao módulo "moeda.py" criado nos desafios anteriores, uma função chamada "resumo()",
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

from Exercicios_107_a_112 import moeda

num = float(input('Digite um valor R$:'))
moeda.resumo(num, 20, 15)
